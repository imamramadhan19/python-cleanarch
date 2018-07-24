from sanic.response import json

SERVED_BY = 'Shipment-Service'

class Success(object):

    def __init__(self, data, meta=None,code = 200, message=None):
        self.data = data
        self.message = message
        self.code = code
        self.meta = meta
    
    def format(self):

        output = {
            "data": self.data
        }

        if self.meta is not None:

            output["meta"] = {
                   'count': self.meta['count'],
                   'currentPage': self.meta['currentPage'],
                   'hasMorePages': self.meta['hasMorePages'],
                   'lastPage': self.meta['lastPage'],
                   'nextPage': self.meta['nextPage'],
                   'perPage': self.meta['perPage'],
                   'prevPage': self.meta['prevPage'],
                   'total': self.meta['total'],
               }
        

        if self.message is not None:
            output['data']['message'] = self.message

        return json(output, headers={'X-Served-By': SERVED_BY}, status=self.code)

class Failure(object):

    def __init__(self,data, code=400, message=None, internalMessage=None):
        self.data = data
        self.message = message
        self.internalMessage = internalMessage
        self.code = code

    def format(self, errors="", message=None):

        output = {
            "error": {
                "code": self.code,
                "userMessage":self.message,
                "internalMessage":self.internalMessage
            }
        }

        if len(errors) > 0:
            output['error']["errors"]=errors
        
        return json(output, headers={'X-Served-By':SERVED_BY}, status=self.code)