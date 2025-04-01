import json, hashlib, os, sys

def fingerprint(file, line, rule, message):
    base = f"{file}:{line}:{rule}:{message}"
    return hashlib.sha256(base.encode()).hexdigest()

def load(path):
    return json.load(open(path)) if os.path.exists(path) else {"runs": []}

def clean_and_patch_results(runs):
    for run in runs:
        run.pop("taxonomies", None)
        run.pop("automationDetails", None)
        for result in run.get("results", []):
            loc = result["locations"][0]["physicalLocation"]
            file = loc["artifactLocation"]["uri"]
            line = loc["region"]["startLine"]
            rule = result.get("ruleId", "unknown")
            message = result["message"]["text"]
            result["partialFingerprints"] = {
                "default": fingerprint(file, line, rule, message)
            }
    return runs

def combine(pmd_sarif, spot_sarif, out_path):
    pmd = load(pmd_sarif)
    spot = load(spot_sarif)

    pmd["runs"] = clean_and_patch_results(pmd.get("runs", []))
    spot["runs"] = clean_and_patch_results(spot.get("runs", []))

    combined = {
        "version": "2.1.0",
        "runs": pmd.get("runs", []) + spot.get("runs", [])
    }

    with open(out_path, "w") as f:
        json.dump(combined, f, indent=2)

if __name__ == "__main__":
    combine(sys.argv[1], sys.argv[2], sys.argv[3])
