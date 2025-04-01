# code-quality-reusable

# 📦 Reusable Java Code Quality Workflow

This repository provides a **reusable GitHub Actions workflow** for Java projects that:

- Runs **PMD** (v7.12.0) and **SpotBugs** (v4.8.3)
- Combines violations into a single SARIF report
- Uploads results to **GitHub Code Scanning**
- Generates a **markdown job summary**
- Supports **multi-module projects**
- Enforces a **violation threshold** to fail builds

---

## 📥 How to Use This Workflow

In your Java project repository:

1. Create a `.github/workflows/code-lint.yml` file.
2. Add the following content:

```yaml
name: Java Lint via Reusable Workflow

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  lint:
    uses: bhuva123/code-quality-reusable/.github/workflows/reusable-code-lint.yml@main
```

> Replace `bhuva123/code-quality-reusable` with your actual repo name if different.

---

## 📁 Repository Structure

```
.github/
└── workflows/
    └── reusable-code-lint.yml     # The reusable workflow

scripts/
├── pmd_to_sarif.py                # Converts PMD JSON to SARIF
└── combine_sarif_with_fingerprints.py  # Combines SARIF with fingerprints
```

---

## 🛠 Prerequisites in Your Project Repo
- Java + Maven project with `src` directories
- Compilable with `mvn clean compile -DskipTests`

---

## 📋 Features
- ✅ PMD Static Analysis with caching
- ✅ SpotBugs compiled bytecode scanning
- ✅ Combined SARIF upload to GitHub Security Tab
- ✅ Markdown summary shown in Actions UI
- ✅ Quality gate fails job if too many violations

---

## 📞 Need Help?
Raise an issue or tag `@bhuva123` in your team chat for support 🚀

