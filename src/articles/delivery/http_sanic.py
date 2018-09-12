from sanic import Blueprint
from sanic.response import json
from config.config import Config
from src.articles.repository.article_repository_orator import ArticleRepositoryOrator
from src.shared.request.request_sanic import RequestSanicDict
from src.articles.use_cases.article_use_cases import ListArticleUsecase, CreateArticleUsecase
from src.articles.delivery.article_request_object import ListArticleRequestObject
from src.articles.delivery.serializers.article_serializers import ListArticle
from src.shared.validator.validator_cerberus import ValidatorCerberus

bp_articles = Blueprint('Articles', url_prefix='articles')

@bp_articles.route('/',methods=['GET', 'POST'])
async def index(request):
    obj_dict = RequestSanicDict(request).parse_all_to_dict()

    if request.method == 'GET':

        validator       = ValidatorCerberus()
        repo_init       = ArticleRepositoryOrator(db=request.app.db)
        use_cases       = ListArticleUsecase(repo=repo_init)
        request_object  = ListArticleRequestObject.from_dict(adict=request.raw_args, validator=validator)
        response_object = use_cases.execute(request_object)
        serialize       = ListArticle.dump(response_object.value).data
    
    return json(serialize, status=Config.STATUS_CODES[response_object.type])
        

