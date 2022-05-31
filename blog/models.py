from django.db import models
from users.models import User
from django.template.defaultfilters import slugify
import uuid



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True,)
    image = models.ImageField(upload_to='images/', blank=False)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='post_crated')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse("blog/post_detail", kwargs={"id": self.id})
    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)+"-"+str(uuid.uuid4())
    #     return super().save(*args, **kwargs)
    
    def get_comments(self):
        comments = self.comment_set.all()
        return self.comments.filter(active=True)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Like {} by {}'.format(self.post, self.user)
     

