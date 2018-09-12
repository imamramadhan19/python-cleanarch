from marshmallow import Schema, fields

class ListArticle(Schema):

    id=fields.Str(attribute="id")
    title=fields.Str(attribute="title")
    categoryId=fields.Str(attribute="category_id")
    authorId=fields.Str(attribute="author_id")
    content=fields.Str(attribute="content")
    isActive=fields.Bool(attribute="is_active")


