from django.db import models





from django.contrib.postgres.operations import CreateExtension
from django.db import migrations

class Migration(migrations.Migration):

    operations = [
        CreateExtension('postgis'),
        
    ]


class place(models.Model):
    city = models.CharField(max_length=50)
    id = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    benchmark_node = models.PointField()
   

