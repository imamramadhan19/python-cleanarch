from src.shared.request_object import ValidRequestObject, InvalidRequestObject

class ListArticleRequestObject(ValidRequestObject):
    def __init__(self,title,is_active):
        self.title = title
        self.is_active = is_active

class CreateArticleRequestObject(ValidRequestObject):
    def __init__(self, title, content, category_id, author_id, created_at, updated_at):
        self.title          = title
        self.content        = content
        self.category_id    = category_id
        self.author_id      = author_id
        self.created_at     = created_at
        self.updated_at     = updated_at

class UpdateArticleRequestObject(ValidRequestObject):

    def __init__(self, id, title, content, category_id, author_id, created_at, updated_at):
        self.id             = id
        self.title          = title
        self.content        = content
        self.category_id    = category_id
        self.author_id      = author_id
        self.created_at     = created_at
        self.updated_at     = updated_at

class DeleteArticleRequestObject(ValidRequestObject):
    def __init__(self,id):
        self.id = id
