# 08 — Packages, pip and Virtual Environments

The Python standard library ships with Python. Third-party packages add functionality but also add maintenance and software supply-chain risk. Prefer the standard library while learning.

## pip commands
~~~bash
python -m pip --version
python -m pip list
python -m pip show requests
~~~

Install only required packages in the project's virtual environment and from trusted sources:

~~~bash
python -m pip install requests
~~~

Record dependencies in requirements.txt and pin tested versions for reproducibility.

## Supply-chain safety
- Check package spelling to avoid typo-squatting.
- Prefer maintained projects and official documentation.
- Do not run install commands copied from unknown sources.
- Avoid installing packages as administrator.
- Never commit .venv, package caches or secrets.
- Treat installed package code as executable code.

## Exercise
Create a fresh virtual environment, inspect installed packages, install one trusted package only if needed, inspect its version and recreate the environment. Record what you did.
