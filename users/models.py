from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os


class Profile(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE)

    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        null=True,
        blank=True
    )

    img = models.ImageField(
        'Picture',
        default='default.png',
        upload_to='user_images'
    )

    allow_mailing = models.BooleanField(default=True)

    def __str__(self):
        return f'Profile user: {self.user.username}'

    def save(self, *args, **kwargs):
        # 🔹 Якщо об'єкт уже існує — перевіряємо старе зображення
        if self.pk:
            try:
                old = Profile.objects.get(pk=self.pk)
                if old.img and old.img != self.img:
                    if old.img.name != 'default.png' and os.path.isfile(old.img.path):
                        os.remove(old.img.path)
            except Profile.DoesNotExist:
                pass

        super().save(*args, **kwargs)

        # 🔹 Обробка зображення
        if self.img and os.path.isfile(self.img.path):
            image = Image.open(self.img.path)

            if image.height > 256 or image.width > 256:
                resize = (256, 256)
                image.thumbnail(resize)
                image.save(self.img.path)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'