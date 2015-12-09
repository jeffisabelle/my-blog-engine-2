# -*- coding: utf-8 -*-
from mongoengine import Document, StringField, DateTimeField, connect

connect("muhammetcan")


class Post(Document):
    title = StringField()
    slug = StringField()
    publish_date = DateTimeField()
    content = StringField()
    excerpt = StringField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "post"
