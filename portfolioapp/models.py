from django.db import models
from django.contrib.auth.models import User

class BlogEntry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edit_permission = models.BooleanField(default=False)  # Edit yetkisi alanı
    
    def __str__(self):  
        return self.content

    class Meta:
        ordering = ['-created_at']
    
    # Kullanıcı adını almak için bir method
    def get_author_username(self):
        return self.author.username  # Kullanıcının kullanıcı adını döndürür
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edit_permission = models.BooleanField(default=False)  # Edit yetkisi alanı

    def __str__(self):  
        return self.content

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_entry = models.ForeignKey(BlogEntry, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
