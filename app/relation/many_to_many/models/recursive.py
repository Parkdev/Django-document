from django.db import models

__all__ = (
    'FacebookUsers',
)

class FacebookUsers(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField(
        'self',
    )

    def __str__(self):
        # 이한영 (친구: a, b, c)
        # QuerySet순회 및 문자열 포매팅
        friend_list = self.friends.all()
        friend_list_str = ', '.join([friend.name for friend in self.friends.all()])
        return '{} (친구: {})'.format(self.name, friend_list_str)