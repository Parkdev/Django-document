from django.db import models

__all__ = (
    'InstagramUser',
)

class InstagramUser(models.Model):
    # - 누군가를 follow 하는사람 목록
    #   followers
        #팔로워 목록
    # - 자신이 다름사람을 folow한 사람 목록
    #   following
        #팔로우 목록
    # A, B
    #A가 B를 Follow한 경우
    #   A는 B의 follower
    #   B는 A의 followee
    name = models.CharField(max_length=50)
    #내가 follow를 한 유저 목록
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers'
    )

    def __str__(self):
        return self.name