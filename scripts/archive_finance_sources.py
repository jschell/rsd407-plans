#!/usr/bin/env python3
"""Request Wayback captures and verify PDF bytes; never claim an unverified capture."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]

def capture(source):
    result = {'evidence_id': source['evidence_id'], 'requested_at': datetime.now(timezone.utc).isoformat(),
              'request_url': 'https://web.archive.org/save/' + source['url'],
              'status': 'unconfirmed', 'capture_url': None}
    try:
        with urlopen(result['request_url'], timeout=60) as response:
            final_url = response.geturl()
            location = response.headers.get('Content-Location')
            response.read(1)
        if re.match(r'https://web\.archive\.org/web/\d+/', final_url):
            result['capture_url'] = final_url
        elif location and re.match(r'/web/\d+/', location):
            result['capture_url'] = 'https://web.archive.org' + location
        else:
            result['status'] = 'request_returned_without_capture_reference'
            return result
        result['status'] = 'capture_returned_unverified'
        raw_url = re.sub(r'/web/(\d+)/', r'/web/\1id_/', result['capture_url'])
        with urlopen(raw_url, timeout=60) as response:
            body = response.read()
        result['archived_sha256'] = hashlib.sha256(body).hexdigest()
        result['status'] = ('capture_verified' if body.startswith(b'%PDF-') and
                            result['archived_sha256'] == source['sha256'] else 'capture_hash_mismatch')
    except Exception as error:
        result['error'] = type(error).__name__ + ': ' + str(error)
        if result['capture_url'] is None:
            result['status'] = 'submission_failed'
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--manifest', default='data/manifests/finance-sources.json', help='Repository-relative source manifest')
    parser.add_argument('--evidence-id', help='Limit submission to one manifest source')
    args = parser.parse_args()
    sources = json.loads((ROOT / args.manifest).read_text())
    selected = [s for s in sources if not args.evidence_id or s['evidence_id'] == args.evidence_id]
    if not selected:
        parser.error('Unknown evidence ID')
    results = []
    for source in selected:
        results.append(capture(source))
        print(source['evidence_id'], results[-1]['status'], flush=True)
        args.output.write_text(json.dumps(results, indent=2) + '\n')
