from django.db import models
# from django.contrib.auth import get_user_model


# User = get_user_model()

class Question(models.Model):
    # author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    question = models.TextField()
    upvotes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Question " + str(self.id)

class Answer(models.Model):
    # author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    answer = models.TextField()
    upvotes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Question " + str(self.question.id) + " Answer " + str(self.id)