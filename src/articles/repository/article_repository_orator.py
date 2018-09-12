from src.shared import helper
from src.articles.domain.article import Article
from src.articles.repository.abc_article_repository import ArticleRepository

class ArticleRepositoryOrator(ArticleRepository):
    def __init__(self, db):
        self.db = db

    def get_all(self, request_objects):
        
        query = self.db.table('articles')
     
        if request_objects.title != "":
            query = query.where('title','like','%{}%'.format(request_objects.title) )
    
        query = query.get()

        result = []
        for row in query:
            data = Article.from_dict({
                'id': row['id'],
                'title': row['title'],
                'content': row['content'],
                'category_id': row['category_id'],
                'author_id': row['author_id'],
                'created_at': row['created_at'],
                'updated_at':row['updated_at']
            })
            result.append(data)
       
        return result
    
    def get_total(self, request_objects):
        
        query = self.db.table('articles')
     
        if request_objects.title != "":
            query = query.where('title','=','{}'.format(request_objects.title) )
    
        return query.count()

    def get_by_id(self, request_objects):

        query = self.db.table('articles').where('id', request_objects.id).first()
        if query:
            return Article.from_dict({
                'id': query['id'],
                'title': query['title'],
                'content': query['content'],
                'category_id': query['category_id'],
                'author_id': query['author_id'],
                'created_at': helper.get_now_timestamp(),
                'updated_at': helper.get_now_timestamp()
            })
        return query
    
    def create(self, request_objects):
        
        return self.db.table('articles').insert_get_id({
            'title': request_objects.title,
            'content': request_objects.content,
            'author_id': request_objects.author_id,
            'category_id': request_objects.category_id,
            'is_active':True,
            'created_at': helper.get_now_timestamp(),
            'updated_at': helper.get_now_timestamp(),
        })

    def update(self, request_objects):

        return self.db.table('articles').where('id', request_objects.id).update({
            'title': request_objects.title,
            'content': request_objects.content,
            'author_id': request_objects.author_id,
            'category_id': request_objects.category_id,
            'is_active':request_objects.is_active,
            'updated_at': helper.get_now_timestamp(),
        })

    def delete(self, request_objects): 
        return self.db.table('articles').where('id', '=', request_objects.id).delete()

