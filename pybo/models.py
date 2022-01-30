from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    # User모델은 django.contrib.auth앱이 제공하는 사용자 모델, # on_delete=models.CASCADE는 계정이 삭제되면 이 계정이 작성한 질문을 모두 삭제하라는 의미이다.
    # author 속성에 저장해야 하는 사용자 객체는 로그인 후 request객체를 통해 얻을 수 있다.
    # 모델을 변경하면 반드시 makemigrations와 migrate를 통해 데이터베이스를 변경해 주어야 한다.
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question') # 추천인 추가

    def __str__(self):
        return self.subject
    # 장고 셸에서 데이터값 조회시 id 대신 제목 표시


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    modify_date = models.DateTimeField(null=True, blank=True) # 데이터베이스와 데이터검사시 값이 없어도 된다는 의미. 수정했을때만 수정
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Question을 foreignkey로 연결, on_delete는 질문삭제하면 답변도 삭제
    content = models.TextField()
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_answer')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 댓글 쓴이
    content = models.TextField() # 댓글 내용
    create_date = models.DateTimeField() # 댓글 작성일시
    modify_date = models.DateTimeField(null=True, blank=True) # 댓글 수정일시
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE) # 이 댓글이 달린 질문
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE) # 이 댓글이 달린 답변변