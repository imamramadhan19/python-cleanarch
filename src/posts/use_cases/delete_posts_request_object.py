import collections
from src.shared.request_object import ValidRequestObject, InvalidRequestObject

class DeletePostsRequestObject(ValidRequestObject):

    def __init__(self, filters):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()
        
        if 'id' not in adict:
            invalid_req.add_error('id',"required")

        if invalid_req.has_errors():
            return invalid_req
        
        return DeletePostsRequestObject(filters=adict)