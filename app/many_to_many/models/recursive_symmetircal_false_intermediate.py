from django.db import models

__all__ = (

    'TwitterUser',
    'Relation',
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

    @property
    def followers(self):
        """

        :return: 나를 follow하는 다른 TwitterUser Queryset
        """
        pass

    @property
    def block_list(self):
        """

        :return: 내가 block하는 다른 TwitterUser Queryset
        """
        pass

    def follow(self, user):
        """
        user를 follow하는 Relation을 생성
        이미 존재한다면 만들지 않는다.
        :param user:  TwitterUser
        :return: tuple(Relation instance, created(생성여부 True/False))
        """
        pass

    def block(self, user):
        """
        user를 block하는 Relation을 생성
            1. 이미 존재한다면 만들지 않는다.
            2. user가 following에 속한다면 해제시키고 만든다.
        :param user: TwitterUser
        :return: tuple(Relation instance, created(생성여부 True/False))
        """
        pass

    @property
    def follower_relations(self):
        """

        :return: 나를 follow하는 Relation QuerySet
        """
    @property
    def followee_relations(self):
        """

        :return: 내가 follow하는 Relation Queryset
        """


class Relation(models.Model):
    CHOICES_RELATION_TYPE = (
        ('f', 'Follow'),
        ('b', 'Block'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='from_user_relations',
        related_query_name='from_user_relation',
        # related_name='group_set',
        # related_query_name='relation_by_from_user' 이 자동으로 들어있다. (기본형태는 클래스 이름의 소문자형; related name이 있을경우 해당이름을 따라간다.)
        # .filter(키=값)름
        #   에서 '키'에 다른 특정'테이블'을 가리키고 싶을 때
        #   MTM필드를 정의한 테이블의 경우에는 해당 필드명을 사용 (Membership의 경우에는 'members')
        #    Group의 경우에 해당 -> 'members'로 Person의 내용을 필터링 가능
        #   MTM필드의  target테이블의 경우에는 필드가 정의되어 있지 않으므로, 이때 사용하는 이름이 related_quesry_name
        #   Person의 경우에 해당 0> 자동 생선된 기본이름 'group"으로 Group의 내용을 필터링 가능
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='to_user_relations',
        related_query_name='to_user_relation',
    )
    relation_type = models.CharField(
        choices = CHOICES_RELATION_TYPE,
        max_length=1,
    )
    created_at = models.DateTimeField(auto_now_add=True)