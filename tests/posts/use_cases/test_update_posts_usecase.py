import pytest
from src.posts.use_cases.update_posts_usecase import UpdatePostsUsecase as usecase
from src.posts.repository.posts_repository_mem import PostsRepositoryMem as repository
from src.posts.use_cases.update_posts_request_object import UpdatePostsRequestObject as ro
from src.shared.helper import dict_to_obj

def test_execute():
    
    repo_init       = repository(db=None)
    use_case        = usecase(repo_init)
    request_object  = ro.from_dict({
        "id":1,
        "title":"TEST INSERT TITLE POST",
        "content":"CONTENT TEST",
        "author_id":1,
        "category_id":1
    })
    response_object = use_case.execute(request_object)
    assert bool(response_object) is True

def test_execute_invalid_validation():
    
    repo_init       = repository(db=None)
    use_case        = usecase(repo_init)
    request_object  = ro.from_dict({
        "title":"TEST INSERT TITLE POST",
        "content":"CONTENT TEST",
        "author_id":1,
        "category_id":1
    })
    response_object = use_case.execute(request_object)
    assert bool(response_object) is False

