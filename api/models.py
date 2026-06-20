from django.db import models


class Question(models.Model):
    CATEGORY_CHOICES = [
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('JS', 'JS'),
        ('c++', 'c++'),
        ('html', 'html'),
        ('css', 'css'),
        ('sql', 'sql'),
    ]

    question = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    answer = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.question


class InterviewQuestion(models.Model):

    CATEGORY_CHOICES = [
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('JS', 'JS'),
        ('CSS', 'CSS'),
    ]

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )

    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class ApptitudeQuestion(models.Model):

    CATEGORY_CHOICES = [
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('JS', 'JS'),
        ('CSS', 'CSS'),
    ]

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )

    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class Users(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username