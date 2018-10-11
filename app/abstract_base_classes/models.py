# 1. AbstractBaseClasses
# 자식테이블만 존재
# 2. Multi table  inheritance
# 부모, 자식태이블만 존재
# 3. 부모 테이블몬 존재'

from django.db import models

# Create your models here.

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class student(CommonInfo):
    home_group = models.CharField(max_length=5)