from random import randint
from docxtpl import DocxTemplate


def set_template(date, time, people, username, email, number, items, total, preferences):
    operation = randint(10 ** 8, 10 ** 9 - 1)
    context = {
        "check_number": operation,
        "date": date,
        "time": time,
        "people": people,
        "username": username,
        "email": email,
        "number": number,
        "items": items,
        "total": total,
        "preferences": preferences
    }
    
    template = DocxTemplate("templates//template.docx")
    template.render(context)
    file_name = f"checks//check_{operation}.docx"
    template.save(file_name)

    return file_name
