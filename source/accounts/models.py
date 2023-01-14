
from django.contrib.auth import get_user_model
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='man', on_delete=models.CASCADE,
                                verbose_name='Пользователь')




    def __str__(self):
        return f"{self.user}"


    class Meta:
        db_table = 'profile'
        verbose_name = 'Профиль'

