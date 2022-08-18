from curses.ascii import HT
from http.client import ResponseNotReady, responses
from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
from models.article import Article
from controllers import article_type, article
from pydantic import BaseModel
from pages import home

app = FastAPI()

@app.get("/")
def read_root():
    return {"Articles": "List of articles"}

@app.get("/article-types/{type}")
def get_article_types(type: str | None = None):
    return article_type.get_article_types(type)

@app.get("/article-types")
def get_article_types():
    return article_type.get_all()

@app.get("/articles/")
def get_articles_list(type = None):
    if type is None:
        return article.get_all()
    
    return article.get_from_type(type)

@app.post("/article/")
def post_article(article_received: Article):
    return article.post(article_received)

@app.get("/articles/{id}", response_model=Article)
def get_article(id: int = 0, type: str = None):
    return article.get(id)

@app.get("/home", response_class=HTMLResponse)
async def get_root_page():
    return home.get_home_page_html()