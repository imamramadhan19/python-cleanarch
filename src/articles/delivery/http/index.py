from sanic import Blueprint
from sanic.response import json
from sanic.log import logger

from src.posts.repository.posts_repository_psql import PostsRepositoryPSQL as repository
from src.posts.use_cases.get_posts_usecase import GetPostsUsecase as usecase
from src.posts.use_cases.get_posts_request_object import GetPostsRequestObject as ro
from src.shared.responses.json import Success, Failure
from src.shared.responses.status_code import STATUS_CODES

bp_posts = Blueprint('Posts', url_prefix='v1/posts')

@bp_posts.route('/')
async def index(request):

    try:

        request.args.get('q')

        filters = {
                    "filters":{}
                    }

        repo_init       = repository(db=request.app.db)
        use_cases       = usecase(repo=repo_init)
        request_object  = ro.from_dict(filters)
        response_object = use_cases.execute(request_object)
        
        if response_object.type:
            return Failure([],message=response_object.message,code=STATUS_CODES[response_object.type] ).format()

        return Success(data=response_object.value['result'],meta=response_object.value).format()

    except Exception as e:

        logger.error(
			"ERROR 500" , exc_info=True, 
		)

        return Failure([],message="Internal Server Error",code=500).format()

   