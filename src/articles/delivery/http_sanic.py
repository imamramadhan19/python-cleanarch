from sanic import Blueprint
from sanic.response import json
from config.config import Config
from src.articles.repository.article_repository_orator import ArticleRepositoryOrator
from src.articles.use_cases.article_use_cases import ListArticleUsecase, CreateArticleUsecase
from src.articles.delivery.article_request_object import ListArticleRequestObject, CreateArticleRequestObject

bp_articles = Blueprint('Articles', url_prefix='articles')

@bp_articles.route('/',methods=['GET', 'POST'])
async def index(request):

    if request.method == 'GET':
        repo_init       = ArticleRepositoryOrator(db=request.app.db)
        use_cases       = ListArticleUsecase(repo=repo_init)
        request_object  = ListArticleRequestObject.from_dict(request.args.raw)
        response_object = use_cases.execute(request_object)
    
    if request.method == 'POST':
        repo_init       = ArticleRepositoryOrator(db=request.app.db)
        use_cases       = CreateArticleUsecase(repo=repo_init)
        request_object  = CreateArticleRequestObject.from_dict(request.args.raw)
        response_object = use_cases.execute(request_object)

    
    return json(response_object.value, status=Config.STATUS_CODES[response_object.type])
        

