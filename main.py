from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="staic")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def name(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "name": "Andy"})


@app.get("/my-reminders")
async def my_reminders():
    return templates.TemplateResponse("my-reminders.html", {})


if __name__ == "__main__":
    pass
