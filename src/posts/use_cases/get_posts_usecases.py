from src.shared import use_case as uc
from src.shared import response_object as ro
from src.shared.messages import en


class GetPosts(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        process = self.repo.get_all(filters=request_object.filters)

        if process['total'] == 0:
            return ro.ResponseFailure.build_resource_error(en.ERROR_NOT_FOUND)
            
        return ro.ResponseSuccess(process)
