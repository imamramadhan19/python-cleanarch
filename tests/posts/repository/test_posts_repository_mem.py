import pytest
from src.posts.repository.posts_repository_mem import PostsRepositoryMem as repository

def test_get_all():
    repo_init = repository(db=None).get_all({})
    assert repo_init['total'] > 0
    assert len(repo_init['result']) > 0
