from django.db import models
from users.models import User
# from django.template.defaultfilters import slugify
# import uuid

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)  
    image = models.ImageField(upload_to='images/', blank=True)
    imageUrl = models.URLField(blank=False, default='https://picsum.photos/seed/picsum/200/300')
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='post_crated')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    STATUS = (
    (0,"Draft"),
    (1,"Publish")
    )

    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200, unique=True, null=True,)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("post_detail", kwargs={"slug": self.slug})
    
    # def save(self, *args, **kwargs):  # new
    #     if not self.slug:
    #         self.slug = slugify(self.title)+str(uuid.uuid4())
    #     return super().save(*args, **kwargs)
    
    def get_comments(self):
        comments = self.comment_set.all()
        return self.comments.count()

    def get_likes(self):
        return Like.objects.filter(post=self).count()

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.user)

''' class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)    

    def __str__(self):
        return self.post.title '''
     

