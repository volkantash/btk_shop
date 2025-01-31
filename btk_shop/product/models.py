from django.db import models
class Category(models.Model):
    STATUS = ( ('True', 'Evet'),('False', 'Hayir') )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null= True, related_name='children',
                               on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class Product(models.Model):
    STATUS = (('True', 'Evet'),
        ('False', 'Hayir'), )
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #many to one relation with Category
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(blank=True, upload_to='images/')
    # price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    price= models.FloatField()
    amount=models.IntegerField(default=0)
    # detail=RichTextUploadingField()
    detail = models.TextField()
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def category_tag(self):
        return self.category
    category_tag.short_description = "Kategori"

    def __str__(self):
        return self.title

class Url(models.Model):
    url = models.SlugField()

    def __str__(self):
        return self.url