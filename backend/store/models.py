from uuid import uuid4
from django.core.files import File
from PIL import Image
from io import BytesIO
from django.db import models
from django_extensions.db.models import TitleSlugDescriptionModel,TimeStampedModel,AutoSlugField
# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    id = models.UUIDField(default=uuid4,editable=False,primary_key=True,null=False , unique=True)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=('name'))

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/categories/{self.slug}'

    def get_relative_url(self):
        return f'/categories/{self.slug}'

    def get_subCategories_absolute(self):
        return f'http://127.0.0.1:8000/categories/{self.slug}/subCategories'

    def get_subCategories_relative(self):
        return f'/categories/{self.slug}/subCategories'

    def __str__(self):
        return self.name
    


class SubCategory(models.Model):
    class Meta:
        verbose_name_plural = "subCategories"

    
    id = models.UUIDField(default=uuid4,primary_key=True,null=False, unique=True,editable=False)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,related_name='subCategories',on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from=('name'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/categories/{self.category.slug}/subCategories/{self.slug}'
    def get_relative_url(self):
        return f'/categories/{self.category.slug}/subCategories/{self.slug}'
    
    def get_products_absolute(self):
        return f'http://127.0.0.1:8000/categories/{self.category.slug}/subCategories/{self.slug}/products'
    
    def get_products_relative(self):
        return f'/categories/{self.category.slug}/subCategories/{self.slug}/products'

class Product(TitleSlugDescriptionModel,TimeStampedModel,models.Model):
    class Meta:
        verbose_name_plural = "Products"

    id = models.UUIDField(default=uuid4,primary_key=True , unique=True,editable=False)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    subCategory = models.ForeignKey(SubCategory,related_name='products',on_delete=models.CASCADE)

    def get_image(self):
        return self.images.all()[0]
    
    def get_summary(self):
        return self.description[:100]+'...'

    def get_subCategory(self):
        return self.subCategory.name
    def get_category(self):
        return self.subCategory.category.name

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/categories/{self.subCategory.category.slug}/subCategories/{self.subCategory.slug}/products/{self.slug}'
    
    def get_relative_url(self):
        return f'/categories/{self.subCategory.category.slug}/subCategories/{self.subCategory.slug}/products/{self.slug}'


class ProductImages(models.Model):
    id = models.UUIDField(unique=True,editable=False,default=uuid4,primary_key=True)
    product = models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True)
    thumbnail = models.ImageField(blank=True,null=True)
    small_thumbnail = models.ImageField(blank=True,null=True)

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000'+self.image.url
        else:
            return  ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000'+self.image.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000'+self.thumbnail.url
            else:
                return ''
    
    def get_small_thumbnail(self):
        if self.small_thumbnail:
            return 'http://127.0.0.1:8000'+self.image.url
        else:
            if self.image:
                self.small_thumbnail = self.make_thumbnail(image=self.image,size=(60,60))
                self.save()

                return 'http://127.0.0.1:8000'+self.small_thumbnail.url
            else:
                return ''

    def make_thumbnail(self,image,size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io,'JPEG',quality=85)


        thumbnail = File(thumb_io,name=image.name)

        return thumbnail