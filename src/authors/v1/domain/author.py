class Author(object):

    def __init__(self, id, name, email, created_at, updated_at):
        self.id = id
        self.name = name
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_dict(self, adict):
        return Author(
            id=adict['id'],
            name=adict['name'],
            email=adict['email'],
            created_at=adict['created_at'],
            updated_at=adict['updated_at'])
