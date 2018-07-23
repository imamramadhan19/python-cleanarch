from abc import ABC, abstractmethod


class PostsRepository(ABC,object):

    @abstractmethod
    def get_all(self, filters): pass

    @abstractmethod
    def get_by_id(self, pk): pass
    
    @abstractmethod
    def create(self, adict): pass

    @abstractmethod
    def update(self, adict): pass

    @abstractmethod
    def delete(self, adict): pass
