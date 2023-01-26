from rest_framework import serializers
from .models import Product,Category,SubCategory,ProductImages


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = (
            'id',
            'get_image',
            'get_thumbnail',
            'get_small_thumbnail'
        )


class ProductSerializerList(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    def get_image(self,obj):
        image = obj.get_image()
        serializer =  ProductImagesSerializer(image)
        return serializer.data

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'price',
            'get_summary',
            'get_category',
            'get_subCategory',
            'get_relative_url',
            'image'
        )


class ProductSerializerDetail(serializers.ModelSerializer):
    images = ProductImagesSerializer(many=True)
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'slug',
            'price',
            'description',
            'subCategory',
            'get_relative_url',
            'images'
        )


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = (
            'id',
            'name',
            'slug',
            'category',
            'get_absolute_url',
            'get_relative_url',
            'get_products_absolute',
            'get_products_relative'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = (
            'id',
            'name',
            'slug',
            'get_absolute_url',
            'get_relative_url',
            'get_subCategories_absolute',
            'get_subCategories_relative'
        )


class NavSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = (
            'id',
            'name',
            'get_products_relative'
        )

class NavCategorySerializer(serializers.ModelSerializer):
    subCategories = NavSubCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = (
            'name',
            'subCategories'
        )
        