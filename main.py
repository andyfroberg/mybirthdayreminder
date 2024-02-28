import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="staic")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def name(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "logged_in": False})

@app.get("/my-reminders")
async def reminders(request: Request):
    return templates.TemplateResponse("reminders.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)