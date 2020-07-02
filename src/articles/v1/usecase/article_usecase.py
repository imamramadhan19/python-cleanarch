from config.config import Config

from src.articles.v1.usecase.abc_article_usecase import ArticleUsecase
from src.shared import response_object as ro
from src.articles.v1.serializers.article_serializers import ListArticle

class ListArticleUsecase(ArticleUsecase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_objects):
        articles = self.repo.get_all(request_objects)
        total = self.repo.get_total(request_objects)
        schema = ListArticle()
        serialize = schema.dump(articles, many=True)

        response = {
            'success': True,
            'code': Config.STATUS_CODES[Config.SUCCESS],
            'message': Config.SUCCESS.lower(),
            'data': serialize.data
        }

        return ro.ResponseSuccess(response)

class CreateArticleUsecase(ArticleUsecase): pass

class DeleteArticleUsecase(ArticleUsecase): pass

class UpdatePostsUsecase(ArticleUsecase): pass
