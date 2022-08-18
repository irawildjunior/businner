from pydantic import BaseModel

from .article_type import ArticleType

class Article(BaseModel):
    id: int | None = None
    type: str
    date: str
    name: str
    call: str
    content: str
    visible: bool

