from fastapi import FastAPI

app = FastAPI()

# Documentation
app.title = "Platzi - Introduction to FastAPI"
app.version = "0.0.1"


@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello World"}
