from pydantic import BaseModel

class ArticleData(BaseModel):
    article_type: str
    general_topic: str
    tone: str
    writing_style: str
    questions: str
    information: str
