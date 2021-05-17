from django.db import models


class Memo(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Tags(models.Model):
    memo = models.ForeignKey('Memo', on_delete=models.CASCADE)
    tag = models.ForeignKey('TagName', on_delete=models.CASCADE)


class TagName(models.Model):
    tag_id = models.IntegerField()
    tag_name = models.CharField(max_length=100)