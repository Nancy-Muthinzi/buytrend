from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =25, blank= True)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()    

    def __str__(self):
        return self.name
   

class Image(models.Model):
    image = models.ImageField(upload_to = 'media/')
    description = models.CharField(max_length =250)
    category = models.ManyToManyField(Category)
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['image']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()  

    @classmethod
    def search_by_category(cls,search_term):
        buy = cls.objects.filter(category__name__icontains=search_term)
        return buy      

    @classmethod
    def retrive_all_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        images = cls.objects.get(pk=id)
        return images

class Product(models.Model):
    image = models.ImageField(upload_to = 'media/')
    description = models.CharField(max_length =250)
    category = models.ManyToManyField(Category)
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.description

    class Meta:
        ordering = ['image']

    def save_product(self):
        self.save()

    def delete_product(self):
        self.delete()  

    @classmethod
    def search_by_category(cls,search_term):
        buy = cls.objects.filter(category__name__icontains=search_term)
        return buy      

    @classmethod
    def retrive_all_images(cls):
        product = Product.objects.all()
        return products

    @classmethod
    def get_product_by_id(cls, id):
        products = cls.objects.get(pk=id)
        return products

class Produce(models.Model):
    image = models.ImageField(upload_to = 'media/')
    description = models.CharField(max_length =250)
    category = models.ManyToManyField(Category)
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.description

    class Meta:
        ordering = ['image']

    def save_produce(self):
        self.save()

    def delete_produce(self):
        self.delete()  

    @classmethod
    def search_by_category(cls,search_term):
        buy = cls.objects.filter(category__name__icontains=search_term)
        return buy      

    @classmethod
    def retrive_all_images(cls):
        produce = Produce.objects.all()
        return produce

    @classmethod
    def get_produce_by_id(cls, id):
        Produce = cls.objects.get(pk=id)
        return produce
