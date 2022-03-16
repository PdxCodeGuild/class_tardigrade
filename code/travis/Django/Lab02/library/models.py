from django.db import models



class Author(models.Model):

    author_name = models.CharField(max_length=30)

    def __str__(self):
        return self.author_name



class Book(models.Model):
    title = models.CharField(max_length=30)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)  
    author_name = models.ForeignKey("Author", on_delete=models.CASCADE)
    is_checked_out = models.BooleanField(default = False, blank=True)
    user = models.CharField(max_length=30, null=True, blank=True )   
    time_stamp = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    def __str__(self):
        return self.title


#class CheckoutBook(models.Model):
  #  title = models.ForeignKey("Book", on_delete=models.CASCADE)
  #  user = models.CharField(max_length=30, null=True,)   
   # time_stamp = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
  

  #  def __str__(self):
  #      return str(self.title)