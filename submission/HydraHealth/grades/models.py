from django.db import models

# Create your models here.
class Grade(models.Model):
    grade_name = models.IntegerField()
    def __str__(self):
        return self.grade_name

class Page(models.Model):
    grade= models.ForeignKey(Grade, on_delete=models.CASCADE)
    name = models.TextField() #this is the name of the page
    link = models.TextField() #this stores the link to the page

    def __str__(self):
        return self.name
