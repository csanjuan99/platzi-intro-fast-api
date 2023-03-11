# platzi-intro-fast-api

## 01 

### Registering dependencies
```sh
pip3 freeze > requirements.txt
```

### Installing dependencies
```sh
if requirements.txt
  pip install -r requirements.txt
else
    pip install fastapi
    pip install uvicorn
```

### Running the server
```sh
uvicorn main:app --reload
```
