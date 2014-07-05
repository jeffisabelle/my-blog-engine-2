# -*- coding: utf-8 -*-
from mongoengine import *

connect('muhammetcan')

class Post(Document):
    title = StringField()
    slug = StringField()
    publish_date = DateTimeField()
    content = StringField()

    def __str__(self):
        return self.title
