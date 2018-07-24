import pytest
from src.posts.use_cases.get_posts_usecase import GetPostsUsecase as usecase
from src.posts.repository.posts_repository_mem import PostsRepositoryMem as repository
from src.posts.use_cases.get_posts_request_object import GetPostsRequestObject as ro
from src.shared.helper import dict_to_obj

def test_execute():
    
    repo_init       = repository(db=None)
    use_case        = usecase(repo_init)
    request_object  = ro.from_dict({})
    response_object = use_case.execute(request_object)

    assert bool(response_object) is True
    assert response_object.value['total'] > 0

def test_execute_with_filters():
    
    repo_init       = repository(db=None)
    use_case        = usecase(repo_init)
    request_object  = ro.from_dict({"filters":{"title":"blog"}})
    response_object = use_case.execute(request_object)

    assert bool(response_object) is True
    assert response_object.value['total'] > 0
