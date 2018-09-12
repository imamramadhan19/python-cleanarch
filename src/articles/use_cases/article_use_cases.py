from src.articles.use_cases.abc_article_use_cases import ArticleUsecase
from src.shared import response_object as ro

class CreateArticleUsecase(ArticleUsecase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        process = self.repo.create(request_object.filters)

        if process:
            return ro.ResponseSuccess("Data berhasil dibuat")           
 
        return ro.ResponseFailure.build_resource_error("Data gagal dibuat")

class DeleteArticleUsecase(ArticleUsecase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        process = self.repo.delete(request_object.filters)
        if process:
            return ro.ResponseSuccess("Data berhasil dihapus")

        return ro.ResponseFailure.build_resource_error("Data gagal dihapus")

class ListArticleUsecase(ArticleUsecase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        
        process = self.repo.get_all(filters=request_object.filters)
        if len(process['result']) > 0:
            return ro.ResponseSuccess("Data berhasil ditampilkan")
            
        return ro.ResponseFailure.build_resource_error("Data tidak ditemukan")

class UpdatePostsUsecase(ArticleUsecase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        
        process = self.repo.update(request_object.filters)

        if process:
            return ro.ResponseSuccess("Data berhasil diupdate")

        return ro.ResponseFailure.build_resource_error("Data gagal diupdate")
            

