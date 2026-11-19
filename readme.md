### Step 1:
```bash
source "venv\Scripts\activate"
```


---


### Step 2:
```bash
python.exe -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```


---


### Step 3:
```bash
uvicorn src.main:app --reload
```


---


### Step 4:
```bash
curl http://localhost:8000/health
```
Expected:
```json
{"status":"ok"}.
```