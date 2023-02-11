from django.db import models


class student(models.Model):
    studeny_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    games_completed = models.IntegerField(default=0)
    birth_date = models.DateField(blank=True, null=True)
    # categorie validé en défaut " n'a pas validé"
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name


class qrcode(models.Model):
    qrcode_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=255)
    games_completed = models.IntegerField(default=0)
