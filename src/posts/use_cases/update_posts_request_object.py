import collections
from src.shared.request_object import ValidRequestObject, InvalidRequestObject

class UpdatePostsRequestObject(ValidRequestObject):

    def __init__(self, filters):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()

        if 'id' not in adict:
            invalid_req.add_error('id',"required")
        
        if 'title' not in adict:
            invalid_req.add_error('Title',"required")
        
        if 'content' not in adict:
            invalid_req.add_error('content',"required")
        
        if 'author_id' not in adict:
            invalid_req.add_error('author_id',"required")

        if 'category_id' not in adict:
            invalid_req.add_error('category_id',"required")

        if invalid_req.has_errors():
            return invalid_req
        
        return UpdatePostsRequestObject(filters=adict)