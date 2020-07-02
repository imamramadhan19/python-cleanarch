import pytest
import json

from schemas.json.loader import JSONSchemaLoader
from src.articles.v1.domain.article import Article
from src.articles.v1.repository.article_repository_orator import ArticleRepositoryOrator
from src.articles.v1.delivery.article_request_object import ListArticleRequestObject
from src.app import connect_db
from src.shared.validator.validator_jsonschema import JSONSchemaValidator

@pytest.fixture(scope="module")
def db_con():
    db = connect_db()
    yield db
    db.disconnect()

def test_get_all(db_con):
    JSONSchemaLoader.load(path='schemas/json/', filename="article-schema.json")

    validator = JSONSchemaValidator()
    adict = {'q': '', 'page': '1', 'limit': '2', 'orderBy': 'name', 'sortBy': 'desc'}
    request_object = ListArticleRequestObject.from_dict(adict, validator)
    result = ArticleRepositoryOrator(db=db_con).get_all(request_object)
    assert isinstance(result, list)
    assert isinstance(result[0], Article)

def test_get_by_id(db_con):
    positive_case = ArticleRepositoryOrator(db=db_con).get_by_id("1")
    assert positive_case is not None
    assert positive_case.id == 1

    negative_case = ArticleRepositoryOrator(db=db_con).get_by_id("999999")
    assert negative_case is None
