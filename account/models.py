from django.db import models


TYPE = (
    ( 'admin','admin' ),
    ( 'manager','manager' ),
    ( 'employee','employee' )
)
class Account(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    type = models.CharField(choices=TYPE, max_length=30)
    avatar = models.ImageField(upload_to='avatar')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

