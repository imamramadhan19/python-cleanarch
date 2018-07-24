import pytest
from src.app import connect_db
from src.posts.repository.posts_repository_psql import PostsRepositoryPSQL as Repository
from src.shared.helper import dict_to_obj

pytest.global_id = 1

@pytest.fixture(scope="module")
def db_con():
    db = connect_db()
    yield db
    db.disconnect()

def test_get_all(db_con):
    repository = Repository(db=db_con).get_all({})
    assert repository['total'] > 0
    assert len(repository['result']) > 0

def test_get_all_with_filters(db_con):
    repository = Repository(db=db_con).get_all({"is_active":True,"title":"blog"})
    assert len(repository['result']) > 0

def test_get_by_id(db_con):
    id = pytest.global_id
    repository = Repository(db=db_con)
    repository = repository.get_by_id(pk=id)

    assert repository.id == id
    assert repository.title == 'Belajar bikin blog 1'

def test_create(db_con):

    adict = {
        'title': 'Title blog',
        'content': 'Content blog',
        'category_id':1,
        'author_id':1,
    }

    obj = dict_to_obj(adict)

    id = Repository(db=db_con).create(obj)
    
    pytest.global_id = id

    assert isinstance(id, int)
    assert id > 0

def test_update(db_con):

    adict = {
        'id':pytest.global_id,
        'title': 'Title blog Update 21',
        'content': 'Content blog',
        'is_active':True,
        'category_id':1,
        'author_id':1,
    }

    obj = dict_to_obj(adict)

    id = Repository(db=db_con).update(obj)

    assert isinstance(id, int)
    assert id > 0

def test_delete(db_con):
    id = Repository(db=db_con).delete(pytest.global_id)
    assert id > 0

