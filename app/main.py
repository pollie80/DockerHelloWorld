from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"title": "FAST API APP HAHA updated B)"}

# endpoint for printing a message given through query string
@app.get("/message")
def message(message: str):
	return {"message": message}

# automate message for each of the endpoints
print("Endpoints:")
for route in app.routes:
	print(f"'{route.name}' endpoint is running on http://localhost:8000{route.path}")

print("Done. App is running.")