import pytest
from src.app import connect_db
from src.posts.repository.posts_repository_psql import PostsRepositoryPSQL as Repository
from src.shared.helper import dict_to_obj

@pytest.fixture(scope="module")
def db_con():
    db = connect_db()
    yield db
    db.disconnect()

def test_post_repository_get_all(db_con):
    repository = Repository(db=db_con).get_all({})
    assert repository['total'] > 0
    assert len(repository['result']) > 0

def test_post_repository_get_all_with_filters(db_con):
    repository = Repository(db=db_con).get_all({"is_active":True,"title":"blog"})
    assert len(repository['result']) > 0

def test_post_repository_get_by_id(db_con):
    id = 1
    repository = Repository(db=db_con)
    repository = repository.get_by_id(pk=id)

    assert repository.id == id
    assert repository.title == 'Belajar bikin blog 1'

def test_post_repository_create(db_con):

    adict = {
        'title': 'Title blog',
        'content': 'Content blog',
        'category_id':1,
        'author_id':1,
    }

    obj = dict_to_obj(adict)

    id = Repository(db=db_con).create(obj)
  
    assert isinstance(id, int)
    assert id > 0

# @pytest.mark.skip(reason="not run this test because data needed for testing list")
# def test_article_repository_delete(db_con):
#     id = pytest.global_id
#     article_repo = GetPosts(db=db_con)
#     article_deleted = article_repo.delete(id)
#     assert isinstance(article_deleted, int)
#     assert article_deleted == 1



# def test_article_repository_create(db_con):
#     author_repo = PostsRepositoryPSQL(db=db_con)
#     author_use_cases = AuthorUseCases(repo=author_repo)
#     author = author_use_cases.get_by_id(pk=1)

#     article_data = Article(
#         id=None,
#         title='Boncel petualang',
#         content='Boncel berpetualang kesana kesini sama betty',
#         author=author,
#         created_at=helper.get_now_timestamp(),
#         updated_at=helper.get_now_timestamp()
#     )

#     article_repo = ArticleRepositoryPSQL(db=db_con)
#     id = article_repo.create(article=article_data)
#     pytest.global_id = id

#     assert isinstance(id, int)
#     assert id > 0


# def test_article_repository_get_by_id(db_con):
#     id = pytest.global_id
#     article_repo = ArticleRepositoryPSQL(db=db_con)
#     article = article_repo.get_by_id(pk=id)

#     assert article.id == id
#     assert article.author.id == 1


# def test_article_repository_update(db_con):
#     id = pytest.global_id
#     article_repo = ArticleRepositoryPSQL(db=db_con)
#     article = article_repo.get_by_id(pk=id)
#     article.title = 'Di update jadi judul lain'

#     article_updated = article_repo.update(article)

#     assert isinstance(article_updated, int)
#     assert article_updated == 1



