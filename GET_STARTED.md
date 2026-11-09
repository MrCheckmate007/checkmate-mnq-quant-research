# Publish safely to GitHub

1. Review `README.md`, `docs/VALIDATION_PROTOCOL.md`, `.gitignore`, and all code before publishing.
2. Extract this folder and verify tests locally: `python -m unittest discover -s tests -v`.
3. Create a fresh GitHub repository named `checkmate-mnq-quant-research`. The recommended visibility for this sanitized portfolio is **public**, after review. The proprietary strategy should remain in a **separate private repository**.
4. In the terminal from this folder:

```bash
git init
git add README.md GET_STARTED.md .gitignore .env.example pyproject.toml checkmate_quant tests examples docs data/README.md .github/workflows/tests.yml
git commit -m "Initial public-safe quant research portfolio"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/checkmate-mnq-quant-research.git
git push -u origin main
```

5. On the GitHub repository page, verify that **no actual brokerage data, TradingView exports, Pine strategy, broker tokens, or private order logic** appears. Check that GitHub Actions passes.
6. Pin the repository on your GitHub profile, then link it from your Quant/FinTech TPM résumé.

Use GitHub's documented `Create a new repository` flow, or the GitHub CLI (`gh repo create`) if your account is already authenticated. Nothing in this ZIP has been automatically pushed to a GitHub account.
