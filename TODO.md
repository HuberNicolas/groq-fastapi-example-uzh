# TODO

Open tasks before the repository is shared further. See also [Known issues](README.md#known-issues).

## 1. Run again

- [x] Add `pyproject.toml` and `uv.lock` with the versions from September 2024 (same as `requirements.txt`)
- [x] Replace the shut-down model `llama3-8b-8192` with `openai/gpt-oss-20b`, configurable via `GROQ_MODEL`
- [x] Test `/`, `/version`, `/fastapi-version`, `/llm/groq/poem/{country}` and `groq_example.py` against the Groq API
- [x] Test the `pip install -r requirements.txt` path in a fresh Python 3.12 environment

## 2. Clean up

- [x] Return `502` instead of `200` with an error field when the Groq API fails
- [x] Resolve the prompt file and `.env` independent of the working directory
- [x] Rename the duplicate `version()` handler
- [x] Add Ruff and format the code
- [x] Add `.env.example` with the variable names the code uses

## 3. Before publishing

- [x] Choose and add a license (MIT)
- [x] Add the project context (IVDA course, UZH, fall 2024, IVDA group) to the README
- [x] Credit third parties (Groq)
- [ ] Rename the GitHub repository to `groq-fastapi-example-uzh` and update `origin`
- [ ] Rewrite the old university address in the commit metadata, then force-push
- [ ] Check for secrets in the files and the git history, right before pushing
- [ ] Revoke the Groq key in the local `.env` if it is no longer needed
- [ ] Check that the Mermaid diagram renders on GitHub
