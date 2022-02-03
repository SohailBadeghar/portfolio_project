from django.db import models


# Create your models blog.
# title.
# pub date.
# image
# body

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to = 'images/')
    body = models.TextField()

# add the blog app to the setting
# create a migrations
# migirate
# add app to admin

def  summary(self):
    print(self.body[:100])
    return self.body[:100]

def pub_date_pretty(self):
    return self.pub_date.strftime('%b %e %Y' )

def __str__(self):
    return self.title

