import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def name(request: Request):
    page_title = "My Birthday Reminder"
    logged_in = False
    return templates.TemplateResponse(request=request, name="home.html", context={"page_title": page_title, "logged_in": logged_in})

@app.get("/my-reminders")
async def reminders(request: Request):
    return templates.TemplateResponse("reminders.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)