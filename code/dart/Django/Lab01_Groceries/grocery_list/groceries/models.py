from django.db import models

# Create your models here.

class GroceryItem(models.Model):
    # class Meta: # used to make the plural name better in the admin panel (Citys vs Cities)
    #     verbose_name_plural = 'cities'

    description = models.CharField(max_length=100)
    created_date = models.DateField(auto_now=True)
    completed_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField()

    # item = GroceryItem.objects.create()

    # id = 1
    # item = GroceryItem.objects.get(id=id)
    # item.completed = True
    # item.completed_date = timezone.now()
    # item.save()



    def __str__(self):
        return self.name 