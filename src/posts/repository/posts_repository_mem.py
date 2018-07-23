from src.posts.domain.posts import Posts
from src.posts.repository.posts_repository import PostsRepository

class PostsRepositoryMem(PostsRepository):
    def __init__(self, db):
        self.db = db
        super(PostsRepositoryMem, self).__init__()

    def get_all(self, adict):

        result = []
   
        data = Posts.from_dict({
            'id': 1,
            'title': 'Title blog 1',
            'content': 'Content blog 1',
            'category_id':1,
            'author_id':1,
            'created_at': '2018-07-11',
            'updated_at': '2018-07-12'
        })
        
        result.append(data)

        data = Posts.from_dict({
            'id': 2,
            'title': 'Title blog 2',
            'content': 'Content blog 2',
            'category_id':1,
            'author_id':1,
            'created_at': '2018-07-11',
            'updated_at': '2018-07-12'
        })
        
        result.append(data)

        data = Posts.from_dict({
            'id': 3,
            'title': 'Title blog 3',
            'content': 'Content blog 3',
            'category_id':1,
            'author_id':1,
            'created_at': '2018-07-11',
            'updated_at': '2018-07-12'
        })
        
        result.append(data)

        data = Posts.from_dict({
            'id': 4,
            'title': 'Title blog 4',
            'content': 'Content blog 4',
            'category_id':1,
            'author_id':1,
            'created_at': '2018-07-11',
            'updated_at': '2018-07-12'
        })
        
        result.append(data)

        data = Posts.from_dict({
            'id': 5,
            'title': 'Title blog 5',
            'content': 'Content blog 5',
            'category_id':1,
            'author_id':1,
        })
        
        result.append(data)

        return {
            'result': result,
            'total': len(result),
        }

    def get_by_id(self, pk): pass
