from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, verbose_name='사용자명')
    useremail = models.EmailField(max_length=100, verbose_name='사용자 이메일')
    password = models.CharField(max_length=100, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간') #auto_now_add=True : 객체가 저장되는 시점의 시간이 자동을 저장

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'djangojang' # 테이블명 지정
        verbose_name = '커뮤니티 사용자'
        verbose_name_plural='커뮤니티 사용자 '
