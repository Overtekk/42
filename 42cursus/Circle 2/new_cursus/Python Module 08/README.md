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


---

### ❗ For 42, because we can't install pip

```
python3 -m venv .venv --without-pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
rm get-pip.py
```
