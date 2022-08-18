from models.article_type import ArticleType
from typing import Union
import json

def get_list():
    with open('data/article_types.json', 'r') as types_file:
        json_file = json.load(types_file)
    
    return json_file

def get_all():
    types_list = get_list()
    return_list = []
    for article_type in types_list:
        return_list.append(article_type)
    
    return return_list