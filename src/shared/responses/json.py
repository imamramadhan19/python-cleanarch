from sanic.response import json

SERVED_BY = 'Shipment-Service'

class Success(object):

    def __init__(self, data, code = 200, message=None):
        self.data = data
        self.message = message
        self.code = code
    
    def format(self):

        output = {
            "status": True,
            "code":self.code,
            "message": "OK",
            "data": self.data
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
            "status": False,
            "code":self.code,
            "message": self.message,
            "data": None
        }
        
        return json(output, headers={'X-Served-By': SERVED_BY}, status=self.code)
        
        # output = {
        #     "error": {
        #         "code": code,
        #         "userMessage":message if message is not None else STATUS_CODES.get(code),
        #         "internalMessage":internalMessage if internalMessage is not None else STATUS_CODES.get(code)
        #     }
        # }

        # if len(errors) > 0:
        #     output['error']["errors"]=errors
        
        return json(output, headers={'X-Served-By':SERVED_BY}, status=self.code)