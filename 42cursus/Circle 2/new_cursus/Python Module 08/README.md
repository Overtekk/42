### 🖥️ Create a virtual environment

```bash
python3 -m venv .venv
```
### 🚀 Activate the virtual environment
```bash
source .venv/bin/activate
```
### 📤 Disable the virtual environment
```bash
deactivate
```
### 📜 Create the requirements file with all packages installed and needed
```bash
pip freeze > requirements.txt
```
### 📜 Install packages INSIDE a virtual environment
```bash
pip install -r requirements.txt
```

### 🐐 Install poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
#### 🐐 Launch poetry
```bash
poetry init
```
#### 🐐 Install dependecy with poetry
```bash
poetry install
```
#### 🐐 Run program with poetry
```bash
poetry run python3 *.py
```

---

### ❗ For 42, because we can't install pip

```
python3 -m venv .venv --without-pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
rm get-pip.py
```
