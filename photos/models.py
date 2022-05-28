from django.db import models

# Create your models here.     
class Location(models.Model):
    name = models.CharField(max_length=255)
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
        
    def __str__(self):
        return self.name  
        
class Category(models.Model):
    name = models.CharField(max_length=255)
        
    class Meta:
        verbose_name_plural = ('categories')
        
    def __str__(self):
        return self.name  

        
class Image(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=700)
    image_file = models.ImageField(upload_to='uploads/')
    dated = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='images')
    
    class Meta:
        ordering = ('-dated',)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def __str__(self):
        return self.name       

        