import pytest

from src.articles.v1.domain.article import Article

def test_init():
    id = 1
    article = Article(
        id=id,
        title='Title blog',
        content='Content blog',
        category_id=1,
        author_id=1,
        created_at='2018-07-11',
        updated_at='2018-07-12'
    )

    assert article.id  == id
    assert article.title == 'Title blog'
    assert article.content == 'Content blog'
    assert article.category_id == 1
    assert article.author_id == 1
    assert article.created_at == '2018-07-11'
    assert article.updated_at == '2018-07-12'

def test_from_dict():
    id = 1
    article = Article.from_dict({
        'id': id,
        'title': 'Title blog',
        'content': 'Content blog',
        'category_id':1,
        'author_id':1,
        'created_at': '2018-07-11',
        'updated_at': '2018-07-12'
    })

    assert article.id == id
    assert article.title == 'Title blog'
    assert article.category_id == 1
    assert article.author_id == 1
    assert article.content == 'Content blog'
    assert article.created_at == '2018-07-11'
    assert article.updated_at == '2018-07-12'
