from fastapi import FastAPI

app = FastAPI()


books = [
    {
        "title": "Книга Один",
        "author": "Франсуа Франсуа Фраесуа",
        "genre": "Научная фантастика",
    },
    {
        "title": "Хорошие автомобили",
        "author": "автоваз",
        "genre": "Научная фантастика",
    },
    {
        "title": "Книга три",
        "author": "третий",
        "genre": "Научная фантастика",
    },
]


@app.get("/")
def get_service_info():
    return {
        "api_name": "Апи нейм",
        "books_endpoint": "/books",
    }


@app.get("/books")
def get_books():
    return books
