from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def starting():
	return {"message": "Hello World!!"}


@app.get("/hello/{name}")
async def print_hello(name: str):
	return {"message": f"Hello {name}"}
