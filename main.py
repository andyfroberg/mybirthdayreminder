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
    """
    assert user logged in
    """
    logged_in = True
    reminders = [
        Reminder("mom", "May 12"),
        Reminder("dad", "August 13"),
        Reminder("jenna", "August 15"),
        Reminder("sophia", "July 3"),
        Reminder("aunt candy", "December 28")
    ]
    user1 = User("andy", reminders)

    return templates.TemplateResponse(request=request, name="my-reminders.html", context={"logged_in": logged_in, "reminders": user1.reminders})


class Reminder:
    def __init__(self, name: str=None, day: str=None):
        self.name = name
        self.day = day


class User:
    def __init__(self, username: str=None, reminders: list[Reminder]=[]):
        self.username = username
        self.reminders = reminders

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)