from unittest import mock

from math import ceil

from config.config import Config
from schemas.json.loader import JSONSchemaLoader
from src.articles.v1.domain.article import Article
from src.articles.v1.serializers.article_serializers import ListArticle
from src.articles.v1.usecase.article_usecase import ListArticleUsecase
from src.shared.validator.validator_jsonschema import JSONSchemaValidator

def domain_article():
    article_1 = Article.from_dict(
        {
            'id': 1,
            'title': 'Title blog 1',
            'content': 'Content blog',
            'category_id': 1,
            'author_id': 1,
            'created_at': '2018-07-11',
            'updated_at': '2018-07-12'
        }
    )

    article_2 = Article.from_dict(
        {
            'id': 1,
            'title': 'Title blog 2',
            'content': 'Content blog',
            'category_id': 1,
            'author_id': 1,
            'created_at': '2018-07-11',
            'updated_at': '2018-07-12'
        }
    )

    return [article_1, article_2]

def test_article_get_all():
    total = len(domain_article())

    repo = mock.Mock()
    repo.get_all.return_value = domain_article()
    repo.get_total.return_value = total

    article_get_all_usecase = ListArticleUsecase(repo=repo)
    request_objects = True
    total_page = 1

    response_object = article_get_all_usecase.execute(request_objects)
    serialize = ListArticle(many=True).dump(domain_article())
    expected_return = {
        'success': True,
        'code': Config.STATUS_CODES[Config.SUCCESS],
        'message': Config.SUCCESS.lower(),
        'data': serialize.data
    }

    assert response_object.value == expected_return
