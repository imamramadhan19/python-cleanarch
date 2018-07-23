from sanic import Blueprint
from sanic.response import json
from sanic.log import logger

from src.posts.repository.posts_repository_psql import PostsRepositoryPSQL as Repository
from src.posts.use_cases.posts import ListShipmentProviderUsecases as Usecases
from src.posts.use_cases.list_shipment_provider_request_object import ListShipmentProviderRequestObject
from src.shared.responses.json import Success, Failure
from src.shared.responses.status_code import STATUS_CODES

bp_post = Blueprint('Posts', url_prefix='v1/posts')

@bp_post.route('/')
async def index(request):

    try:

        adict           = request.raw_args

        repository      = Repository(db=request.app.db)
        use_cases       = Usecases(repo=repository)
        request_object  = ListShipmentProviderRequestObject.from_dict({})
        response_object = use_cases.execute(request_object)

        if response_object.type:
            return Failure([],message=response_object.message,code=STATUS_CODES[response_object.type] ).format()

        return Success(response_object.value['result']).format()

    except Exception as e:

        logger.error(
			"ERROR 500" , exc_info=True, 
		)

        return Failure([],message="Internal Server Error",code=500).format()

   