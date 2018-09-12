from src.articles.use_cases.abc_article_use_cases import ArticleUsecase
from src.shared import response_object as ro
from src.articles.serializers.article_serializers import ListArticle

class ListArticleUsecase(ArticleUsecase): 

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_objects):
        articles  = self.repo.get_all(request_objects)
        total     = self.repo.get_total(request_objects)
        schema    = ListArticle()
        serialize = schema.dump(articles, many=True)

        response  = {
            'success': True,
            'code':200,
            'message':'Sukses',
            'data': serialize.data
        }

        return ro.ResponseSuccess(response)

class CreateArticleUsecase(ArticleUsecase): pass

class DeleteArticleUsecase(ArticleUsecase): pass

class UpdatePostsUsecase(ArticleUsecase): pass
