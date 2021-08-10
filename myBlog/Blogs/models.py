from django.db import models
from django.contrib.auth.models import User



# Model for blog posts
class blogPost(models.Model):
    title=models.CharField(max_length=200,unique=True)
    author=models.CharField(max_length=200)
    content=models.TextField()
    pub_date =models.DateTimeField(auto_now_add=True)

class meta:
    ordering=['pub_date']

def _str_(self):
    return  self.title

#Model for comments with a foreign key
class comment_post(models.Model):
    blogpost=models.ForeignKey(blogPost,on_delete=models.CASCADE,related_name='comments',null='True')
    name=models.CharField(max_length=200)
    email=models.EmailField()
    comments=models.TextField();
    posted_on=models.DateTimeField(auto_now_add=True);
    status=models.BooleanField(default='False')                         #For admin approval

class meta:
        ordering =['posted_on']

def _str_(self):
    return 'Comment by {}'.format(self.name)




