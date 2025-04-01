import json
import sys

def convert(pmd_json_path, sarif_output_path):
    with open(pmd_json_path, "r") as f:
        pmd_data = json.load(f)

    if not pmd_data or "files" not in pmd_data:
        pmd_data = {"files": []}

    sarif_report = {
        "version": "2.1.0",
        "runs": [{
            "tool": {
                "driver": {
                    "name": "PMD",
                    "informationUri": "https://pmd.github.io/",
                    "rules": []
                }
            },
            "results": [
                {
                    "ruleId": v["rule"],
                    "message": {"text": v["description"]},
                    "locations": [{
                        "physicalLocation": {
                            "artifactLocation": {"uri": f["filename"]},
                            "region": {"startLine": v["beginline"]}
                        }
                    }]
                } for f in pmd_data["files"] for v in f.get("violations", [])
            ]
        }]
    }

    with open(sarif_output_path, "w") as f:
        json.dump(sarif_report, f, indent=2)

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
