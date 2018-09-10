from src.shared import helper
from src.articles.domain.article import Article
from src.articles.repository.abc_article_repository import ArticleRepository

class ArticleRepositoryMem(ArticleRepository):
    def __init__(self, db):
        self.db = db
        super(ArticleRepositoryMem, self).__init__()

    def get_all(self, filters):
        result = []
   
        data = Article.from_dict({
            'id': 1,
            'title': 'Title blog 1',
            'content': 'Content blog 1',
            'category_id':1,
            'author_id':1,
            'created_at': '2018-07-11',
            'updated_at': '2018-07-12'
        })
        
        result.append(data)

        data = Article.from_dict({
            'id': 2,
            'title': 'Title blog 2',
            'content': 'Content blog 2',
            'category_id':1,
            'author_id':1,
            'created_at': '2018-07-11',
            'updated_at': '2018-07-12'
        })
        
        result.append(data)

        data = Article.from_dict({
            'id': 3,
            'title': 'Title blog 3',
            'content': 'Content blog 3',
            'category_id':1,
            'author_id':1,
            'created_at': '2018-07-11',
            'updated_at': '2018-07-12'
        })
        
        result.append(data)

        data = Article.from_dict({
            'id': 4,
            'title': 'Title blog 4',
            'content': 'Content blog 4',
            'category_id':1,
            'author_id':1,
            'created_at': '2018-07-11',
            'updated_at': '2018-07-12'
        })
        
        result.append(data)

        data = Article.from_dict({
            'id': 5,
            'title': 'Title blog 5',
            'content': 'Content blog 5',
            'category_id':1,
            'author_id':1,
            'created_at': '2018-07-11',
            'updated_at': '2018-07-12'
        })
        
        result.append(data)
    
        return {
            'count': len(result),
            'currentPage': 0,
            'hasMorePages': 0,
            'lastPage': 0,
            'nextPage': 0,
            'perPage': 0,
            'prevPage': 0,
            'result': result,
            'total': len(result),
        }

    def get_by_id(self, pk): pass

    def create(self, adict): 
        
        create = {
            'title': adict['title'],
            'content': adict['content'],
            'author_id': adict['author_id'],
            'category_id': adict['category_id'],
            'is_active':True,
            'created_at': helper.get_now_timestamp(),
            'updated_at': helper.get_now_timestamp(),
        }

        return True

    def update(self, adict): 

        update = {
            'id': adict['id'],
            'title': adict['title'],
            'content': adict['content'],
            'author_id': adict['author_id'],
            'category_id': adict['category_id'],
            'is_active':True,
            'created_at': helper.get_now_timestamp(),
            'updated_at': helper.get_now_timestamp(),
        }

        return True

    def delete(self, adict): 

        adict['id']
        return True
