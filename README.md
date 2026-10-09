# vuln-test-repo

Test fixture for the vulnerability patching pipeline. It contains **no exploit
code**, only dependencies pinned to old releases that have published advisories.
Do not deploy it.

| File | Ecosystem | Vulnerable pins | Control (should not be flagged) |
|------|-----------|-----------------|--------------------------------|
| `requirements.txt` | PyPI | flask, django, requests, pyyaml, jinja2, urllib3, pillow | certifi |
| `package.json` | npm | lodash, minimist, express, axios, node-fetch, moment | none |

## Use with the pipeline

```bash
python main.py sync --eco PyPI npm
python main.py scan /path/to/vuln-test-repo --test-cmd "python app.py"
```

Expected: most pins flagged, upgraded to fixed versions, verifier reports 0 left.
Exact counts change as new advisories are published.
