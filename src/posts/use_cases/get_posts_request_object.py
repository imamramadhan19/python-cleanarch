import collections
from src.shared.request_object import ValidRequestObject, InvalidRequestObject

class PostsRequestObject(ValidRequestObject):

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()

        if 'filters' in adict and not isinstance(adict['filters'], collections.Mapping):
            invalid_req.add_error('filters', 'Is not iterable')
        
        # if 'name' not in adict:
        #     invalid_req.add_error('name',"required")

        if invalid_req.has_errors():
            return invalid_req

        return PostsRequestObject(filters=adict.get('filters', None))