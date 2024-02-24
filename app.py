from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="staic")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def name(request: Request):
    return templates.TemplateRespons("home.html", {"request": request, "name": "Andy"})