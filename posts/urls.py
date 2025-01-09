from django.urls import path
from .views import home, post_detail, post_update, post_delete

urlpatterns = [
	path('', home, name="home"),
	path('post/<int:pk>', post_detail, name="detail-post"),
	path('post-update/<int:pk>', post_update, name="update-post"),
	path('post-delete/<int:pk>', post_delete, name="delete-post")
]