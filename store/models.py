from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User


class Category(MPTTModel):
    category_name = models.CharField("სახელი", max_length=100, null=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="ზეკატეგორია",
        related_name="children"
    )
    slug = models.SlugField(default="", null=False)

    class MPTTMeta:
        order_insertion_by = ['category_name']

    def __str__(self):
        return f"{self.category_name}"


class Product(models.Model):
    product_name = models.CharField("სახელი", max_length=100)
    product_price = models.DecimalField(
        "ფასი",
        max_digits=10,
        decimal_places=2
    )
    product_description = models.TextField("აღწერა", null=True, blank=True)
    product_rating = models.IntegerField("შეფასება")
    product_image = models.ImageField(
        "სურათი",
        help_text="ატვირთეთ ფოტოსურათი",
        blank=True,
        null=True
    )
    # ბაზაში ხელით რო არ ავტვირთო
    image_url = models.CharField("დროებითი სურათი", max_length=150)
    product_category = models.ManyToManyField(
        "Category",
        verbose_name="კატეგორია"
    )
    product_quantity = models.IntegerField("მარაგშია:", null=True, blank=True)
    is_organic = models.BooleanField("organic", default=False)
    on_sale = models.BooleanField("sale", default=False)
    country = models.CharField("country", default="Agro Farm", max_length=150)
    weight = models.PositiveIntegerField("წონა", default=1)
    slug = models.SlugField(default="", null=False)
    related_products = models.ManyToManyField("Product", verbose_name="მსგავსი პროდუქტები", blank=True)
    def __str__(self):
        return f"{self.product_name}"


class ProductReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ავტორი")
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name="პროდუქტი")
    review = models.TextField("რევიუ")

    def __str__(self):
        return f"{self.user}"


class ShopReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ავტორი")
    review = models.TextField("რევიუ")
    date = models.DateField(auto_now_add=True)

