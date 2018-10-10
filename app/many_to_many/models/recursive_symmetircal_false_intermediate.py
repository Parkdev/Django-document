from django.db import models

__all__ = (
    'Relation'
    'TwitterUser'
)

class TwitterUser(models.Model):
    """
    특정 유저가 다른 유저를 (인스터트 메서드)
        follow (팔로우하기)
        block (차단하기)

    중간모델이 저장하는 정보
        from_user
            어떤 유저가 '만든'관계인지
        to_user
            관계의 '대상이'되는 유저
        relation_type
            follow또는 block (팔로우 또는 차단)

    용어 정리
     - 자신을 follow하는 다름 사람목록
        followers (팔로우 목록)
     - 자신이 다름사람을 folow한 사람 목록
        following (팔로우 목록)
     - 자신이 다른사람을 block한 목록
        block_list
     - A가 B를 Follow한 경우
        A는 B의 follower (팔로워)
        B는 A의 followee (팔로우)
    """
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        through='Relation',
        symmetrical=False,
    )
    def __str__(self):
        return self.name

class Relation(models.Model):
    CHOICES_RELATION_TYPE = (
        ('f', 'Follow'),
        ('b', 'Block')
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_from user'
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_to user'
    )
    relation_type = models.CharField(
        choices = CHOICES_RELATION_TYPE,
        max_length=1,
    )
    created_at = models.DateTimeField(auto_now_add=True)