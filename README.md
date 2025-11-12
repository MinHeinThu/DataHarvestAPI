# Web scraping API with FastAPI

## Project setup

Follow these steps to set up and run the project. Run each command from your project root.

1. Create (if needed) and enter the project directory

```bash
mkdir my_project        # optional if you already have the repo folder
cd my_project
```

1. Create a Python virtual environment

```bash
python3 -m venv .venv   # you can name the venv anything; `.venv` is common
```

1. Activate the virtual environment

```bash
source .venv/bin/activate
# verify: which python or python --version
```

1. (Optional) Upgrade pip

```bash
pip install --upgrade pip
```

1. Install project dependencies

```bash
pip install "fastapi[standard]" uvicorn requests beautifulsoup4
```

1. If a `requirements.txt` exists or to save installed packages

```bash
pip install -r requirements.txt   # install from file
pip freeze > requirements.txt     # save current environment packages
```

1. Create `main.py` if it doesn't exist

```bash
touch main.py
```

1. Run the application (development server)

```bash
uvicorn main:app --reload
```

Notes

- On macOS/Linux use `python3` if `python` points to Python 2.x.
- If you prefer a single install command from a requirements file, use step 6.
- Replace `my_project` and `.venv` names to match your local conventions.
