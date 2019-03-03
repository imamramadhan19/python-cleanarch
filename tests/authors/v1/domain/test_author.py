import pytest

from src.authors.v1.domain.author import Author

def test_init():
    id = 1
    author = Author(
        id=id,
        name='John Doe',
        email='johndoe@mail.com',
        created_at='2018-07-11',
        updated_at='2018-07-12'
    )

    assert author.id == id
    assert author.name == 'John Doe'
    assert author.email == 'johndoe@mail.com'
    assert author.created_at == '2018-07-11'
    assert author.updated_at == '2018-07-12'

def test_from_dict():
    id = 1
    author = Author.from_dict({
        'id': id,
        'name': 'John Doe',
        'email': 'johndoe@mail.com',
        'created_at': '2018-07-11',
        'updated_at': '2018-07-12'
    })

    assert author.id == id
    assert author.name == 'John Doe'
    assert author.email == 'johndoe@mail.com'
    assert author.created_at == '2018-07-11'
    assert author.updated_at == '2018-07-12'
