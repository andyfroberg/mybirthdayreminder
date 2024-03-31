import uvicorn
from fastapi import FastAPI, Request, Form, Depends, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from typing import Type
from datetime import date
from schemas import AddReminderForm


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Set up mock user for testing
class Reminder:
    def __init__(self, name: str=None, day: str=None):
        self.name = name
        self.day = day

class User:
    def __init__(self, username: str=None, reminders: list[Reminder]=[]):
        self.username = username
        self.reminders = reminders

reminders = [
        Reminder("mom", "May 12"),
        Reminder("dad", "August 13"),
        Reminder("jenna", "August 15"),
        Reminder("sophia", "July 3"),
        Reminder("aunt candy", "December 28")
    ]

user1 = User("andy", reminders)


@app.get("/")
async def name(request: Request):
    page_title = "My Birthday Reminder"
    logged_in = False
    return templates.TemplateResponse(
        request=request, name="home.html", 
        context={
            "page_title": page_title, 
            "logged_in": logged_in, 
            "footer_year": get_current_year()
        }
    )

@app.get("/my-reminders")
async def reminders(request: Request):
    """
    assert user logged in
    """
    page_title = "My Reminders"
    logged_in = True

    return templates.TemplateResponse(
        request=request, 
        name="my-reminders.html", 
        context={
            "page_title": page_title,
            "logged_in": logged_in, 
            "reminders": user1.reminders, 
            "footer_year": get_current_year()
        }
    )

@app.get("/add-reminder")
async def get_add_reminder(request: Request):
    page_title = "Add a Reminder"
    logged_in = True  # replace later with check_user_logged_in()
    
    # Handle errors

    # If successful, send user back to my-reminders page

    return templates.TemplateResponse(
        request=request,
        name="add-reminder.html",
        context={
            "page_title": page_title,
            "logged_in": logged_in, 
            "reminders": user1.reminders, 
            "footer_year": get_current_year()
        }
    )

@app.post("/add-reminder")
async def post_add_reminder(request: Request, form_data: AddReminderForm=Depends(AddReminderForm.as_form)):
    page_title = "Add a Reminder"
    logged_in = True  # replace later with check_user_logged_in()
    
    # handle form input
    day = f"{form_data.birthday_month} {form_data.birthday_day}"
    user1.reminders.append(Reminder(form_data.birthday_name, day))


    # add reminder to user's reminders

    # handle errors

    # if successful
    return RedirectResponse(
        request.url_for("reminders"), 
        status_code=status.HTTP_302_FOUND, 
        # headers={"x-error": "Invalid credentials"}
    )


@app.get("/account")
async def account(request: Request):
    page_title = "My Account"
    logged_in = True
    return templates.TemplateResponse(
        request=request, 
        name="account.html", 
        context={
            "page_title": page_title, 
            "logged_in": logged_in, 
            "footer_year": get_current_year()
        }
    ) 


### Helper functions ###
def get_current_year():
    return date.today().year


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)