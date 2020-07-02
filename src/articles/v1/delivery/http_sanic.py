from sanic import Blueprint
from sanic.response import json
from config.config import Config
from src.articles.v1.repository.article_repository_orator import ArticleRepositoryOrator
from src.shared.request.request_sanic import RequestSanicDict
from src.articles.v1.usecase.article_usecase import ListArticleUsecase, CreateArticleUsecase
from src.articles.v1.delivery.article_request_object import ListArticleRequestObject
from src.shared.validator.validator_cerberus import ValidatorCerberus

bp_articles = Blueprint('Articles V1', url_prefix='v1/articles')

@bp_articles.route('/', methods=['GET', 'POST'])
async def index(request):
    obj_dict = RequestSanicDict(request).parse_all_to_dict()

    if request.method == 'GET':

        validator = ValidatorCerberus()
        repo_init = ArticleRepositoryOrator(db=request.app.db)
        usecase = ListArticleUsecase(repo=repo_init)
        request_object = ListArticleRequestObject.from_dict(adict=request.raw_args, validator=validator)
        response_object = usecase.execute(request_object)

    return json(response_object.value, status=Config.STATUS_CODES[response_object.type])
