from django.db import models

# Create your models here.
from random import choices


class AppModel(models.Model):
    main_url = models.TextField()
    code = models.CharField(max_length=5)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.main_url

    @staticmethod
    def generate_referral_code():
        s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return ''.join(choices(s, k=5))

    def save(self, *args, **kwargs):
        if self.pk is None:
            code = self.generate_referral_code()
            model_objects = AppModel.objects.filter(code=code)
            if model_objects:
                return self.save(*args, **kwargs)
            self.code = code
        super(AppModel, self).save(*args, **kwargs)
