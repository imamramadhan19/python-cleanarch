class Article(object):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.content = kwargs.get('content')
        self.category_id = kwargs.get('category_id')
        self.author_id = kwargs.get('author_id')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')

    @classmethod
    def from_dict(self, adict):
        article = Article(**{
            "id": adict.get('id'),
            "title": adict.get('title'),
            "content": adict.get('content'),
            "category_id": adict.get('category_id'),
            "author_id": adict.get('author_id'),
            "created_at": adict.get('created_at'),
            "updated_at": adict.get('updated_at')
        })

        return article
