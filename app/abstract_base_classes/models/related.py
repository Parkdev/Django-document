from django.db import models

__all__ = (
    'RelatedUser',
    'PhotoPost',
    'TextPost',

)




class RelatedUser(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostBase(models.Model):
    author = models.ForeignKey(
        RelatedUser,
        on_delete=models.CASCADE,
        # 유저(Person) 입장에서
        # 자신이 특정 Post의 'author'인 경웨 해당하는 모든 PostBase객체를 참조하는 역방향 매니저 이
        related_name='%(class)s_set',
        related_query_name='%(class)s',
    ) # '%(class)s'는 상속받은 클래스 이름을 따라간다.
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class PhotoPost(PostBase):
    #related_name ='photopost_set
    photo_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Post (author: {self.author.name}'


class TextPost(PostBase):
    text = models.TextField(blank=True)

    def __str__(self):
        return f'Post (author: {self.author.name}'

#데이터를 직접바꿨을때는 장고에서 인식한 migrate를 fake로 처리
#   ./manage.py migrate (이름) 0002 --fake
#이후 db랑 내용이 같게 수정후 사용하면된다.
