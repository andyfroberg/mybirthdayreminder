from fastapi import Form
from pydantic import BaseModel


class AddReminderForm(BaseModel):
    birthday_name: str
    birthday_month: str
    birthday_day: str

    @classmethod
    def as_form(
        cls,
        birthday_name: str = Form(...),
        birthday_month: str = Form(...),
        birthday_day: str = Form(...)
    ):
        return cls(
            birthday_name=birthday_name,
            birthday_month=birthday_month, 
            birthday_day=birthday_day
        )