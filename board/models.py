from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=200,verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='작성자')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록 시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Commuinty_board'
        verbose_name = '커뮤니티 게시글'
        verbose_name_plural = '커뮤니티 게시글'