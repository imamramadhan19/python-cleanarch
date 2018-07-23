import pytest

from src.posts.domain.posts import Posts


def test_post_model_init():
    id = 1
    post = Posts(
        id=id,
        title='Title blog',
        content='Content blog',
        category_id=1,
        author_id=1,
        created_at='2018-07-11',
        updated_at='2018-07-12'
    )

    assert post.id  == id
    assert post.title == 'Title blog'
    assert post.content == 'Content blog'
    assert post.category_id == 1
    assert post.author_id == 1
    assert post.created_at == '2018-07-11'
    assert post.updated_at == '2018-07-12'

def test_post_model_from_dict():
    id = 1
    post = Posts.from_dict({
        'id': id,
        'title': 'Title blog',
        'content': 'Content blog',
        'category_id':1,
        'author_id':1,
        'created_at': '2018-07-11',
        'updated_at': '2018-07-12'
    })

    assert post.id == id
    assert post.title == 'Title blog'
    assert post.category_id == 1
    assert post.author_id == 1
    assert post.content == 'Content blog'
    assert post.created_at == '2018-07-11'
    assert post.updated_at == '2018-07-12'
