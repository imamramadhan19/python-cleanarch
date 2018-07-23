

class Posts(object):
    def __init__(self, id, title, content, category_id, author_id, created_at, updated_at):
        self.id             = id
        self.title          = title
        self.content        = content
        self.category_id    = category_id
        self.author_id      = author_id
        self.created_at     = created_at
        self.updated_at     = updated_at

    @classmethod
    def from_dict(self, adict):
        posts = Posts(
            id=adict['id'],
            title=adict['title'],
            content=adict['content'],
            category_id=adict['category_id'],
            author_id=adict['author_id'],
            created_at=adict['created_at'],
            updated_at=adict['updated_at']
        )

        return posts
