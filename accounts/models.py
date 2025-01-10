from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(AbstractUser):
    photo = models.ImageField(
        upload_to='profile-img/',
        default='profile-img/default-img.png', 
        )
    bio = models.TextField(max_length=100, blank=True, null=True)
    # los seguidores tienen un campo de tipo ManyToMany (El usuario puede seguir a muchos usuarios y muchos usuarios pueden seguir al usuario.)
    follows = models.ManyToManyField(
        # La relacion es con el mismo modelo.
        "self",
        # Permite que sea opcional, un usuario no necesita seguir a otros al ver su perfil
        blank=True, 
        # Indita que si el usuario B sigue al usuario A, A no necesariamente tiene que seguir a B
        symmetrical=False,
        # Es un nombre para acceder a los usuarios que siguen al perfil
        related_name="followed_by")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk':self.pk})

    # Devuelve la cantidad de perfiles que el usuario sigue
    def count_followers(self):
        return self.follows.count()

    # Devuelve la cantidad de perfiles que siguen al usuario actual
    def count_following(self):
        # Busca en el usuario actual, todos los usuarios que lo tienen en su follows
        return Profile.objects.filter(follows=self).count()
