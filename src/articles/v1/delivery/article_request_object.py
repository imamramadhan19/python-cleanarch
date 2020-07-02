from src.shared import helper
from src.shared.request_object import ValidRequestObject, InvalidRequestObject

class ListArticleRequestObject(ValidRequestObject):
    def __init__(self, title):
        self.title = title

    @classmethod
    def from_dict(cls, adict, validator):
        schema = {
            'title': {
                'type': 'string',
                'required': False,
            }
        }

        if not validator.is_valid(adict=adict, schema=schema):
            invalid_req = InvalidRequestObject()
            invalid_req.parse_error(errors=validator.get_errors())
            return invalid_req

        data = validator.get_valid_data()

        return ListArticleRequestObject(
            title=helper.get_value_from_dict(data, 'title', '')
        )

    def __nonzero__(self):
        return True

class CreateArticleRequestObject(ValidRequestObject):
    def __init__(self, title, content, category_id, author_id, created_at, updated_at):
        self.title = title
        self.content = content
        self.category_id = category_id
        self.author_id = author_id
        self.created_at = created_at
        self.updated_at = updated_at

class UpdateArticleRequestObject(ValidRequestObject):

    def __init__(self, id, title, content, category_id, author_id, created_at, updated_at):
        self.id = id
        self.title = title
        self.content = content
        self.category_id = category_id
        self.author_id = author_id
        self.created_at = created_at
        self.updated_at = updated_at

class DeleteArticleRequestObject(ValidRequestObject):
    def __init__(self, id):
        self.id = id
