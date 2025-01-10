from django.db import models
from accounts.models import Profile

# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile")
	img = models.ImageField(upload_to='post-img/', blank=True)
	content = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(Profile, related_name="post_like")

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.user.username

	def number_of_likes(self):
		return self.likes.count()

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
	user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments")
	text = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.text
