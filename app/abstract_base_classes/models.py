# 1. AbstractBaseClasses
# 자식테이블만 존재
# 2. Multi table  inheritance
# 부모, 자식태이블만 존재
# 3. 부모 테이블몬 존재'

from django.db import models

# Create your models here.

class CommonInfo(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name'] #이걸 사용하는것보다 db_index값을 주는것이 좋다.

    def __str__(self):
        return self.name

class Student(CommonInfo):
    #commoninfo클래스 테이블도 안만들지고shell에서 가져오지않는다.
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta): #(커먼인포에 메타를 상속받는다라는뜻 없으면 커먼인포 메타를 덮어씌워서 커먼인포의 옵션이 적용되지않는다.)

        verbose_name = '학생'
        verbose_name_plural = '학생 목록'