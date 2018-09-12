from src.shared import helper
from src.articles.domain.article import Article
from src.articles.repository.abc_article_repository import ArticleRepository

class ArticleRepositoryOrator(ArticleRepository):
    def __init__(self, db):
        self.db = db

    def get_all(self, filters):
        
        query = self._filter_query(filters)
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
       
        return {
            'result': result
        }

    def get_by_id(self, pk):

        query = self.db.table('articles').where('id', pk).where('is_active',True).first()
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
    
    def create(self, adict):
        
        return self.db.table('articles').insert_get_id({
            'title': adict['title'],
            'content': adict['content'],
            'author_id': adict['author_id'],
            'category_id': adict['category_id'],
            'is_active':True,
            'created_at': helper.get_now_timestamp(),
            'updated_at': helper.get_now_timestamp(),
        })

    def update(self, adict):

        return self.db.table('articles').where('id', adict['id']).update({
            'title': adict['title'],
            'content': adict['content'],
            'author_id': adict['author_id'],
            'category_id': adict['category_id'],
            'is_active':adict['is_active'],
            'updated_at': helper.get_now_timestamp(),
        })

    def delete(self, adict): 
        return self.db.table('articles').where('id', '=', adict['id']).delete()

    def _filter_query(self, adict):
        
        query = self.db.table('articles')
     
        is_active = helper.get_value_from_dict(adict, 'is_active', '')
        if is_active != "":
            query = query.where('is_active','=','{}'.format(is_active) )
        
        title = helper.get_value_from_dict(adict, 'title', '')
        if title != "":
            query = query.where('title','=','{}'.format(title) )

        return query.get()
       