from django.db import models
from abstract_base_classes.models import PostBase

# Create your models here.

class PhotoPost(PostBase):
    # author의 related_name이 겹친다.
    pass
