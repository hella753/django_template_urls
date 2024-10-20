from django.db.models import Count
from django.shortcuts import render
from store.models import Product, ProductReviews, Category, ShopReviews


def index(request):
    fruits = Product.objects.filter(product_category__category_name="fruit")
    veggies = Product.objects.filter(product_category__category_name="vegetable")
    reviews = ShopReviews.objects.all().select_related("user")
    fruit_dict = {}
    veggy_dict = {}
    fruit_list = []
    veggy_list = []
    for prod in fruits:
        fruit_dict = {
            "product_name": prod.product_name,
            "product_price": prod.product_price,
            # იტერაცია რომ შევძლო თემფლეითში
            "product_quantity": range(0,prod.product_quantity),
            "product_desc": prod.product_description,
            "product_category": prod.product_category,
            "image": prod.image_url,
            "slug": prod.slug
        }
        fruit_list.append(fruit_dict)
    for prod in veggies:
        veggy_dict = {
            "product_name": prod.product_name,
            "product_price": prod.product_price,
            # იტერაცია რომ შევძლო თემფლეითში
            "product_quantity": range(0,prod.product_quantity),
            "product_desc": prod.product_description,
            "product_category": prod.product_category,
            "image": prod.image_url,
            "slug": prod.slug

        }
        veggy_list.append(veggy_dict)
    context = {
        "fruits": fruit_list,
        "veggies": veggy_list,
        "reviews": reviews,
        "range": range(0,4)
    }
    print(context)
    return render(request, "homepage/index.html", context)

def category_listings(request, slug):
    categories=Category.objects.all()
    products=Product.objects.all()
    categories=categories.annotate(count=Count("product"))
    context = {
        "categories": categories,
        "products": products,
        "featured_prod_iterator": range(0,3)
    }
    return render(request, "shop/shop.html", context)

def product(request, slug):
    individual_product = Product.objects.get(slug=slug)
    product_reviews = ProductReviews.objects.filter(product=individual_product).select_related("user")
    related = individual_product.related_products.all().prefetch_related("product_category")
    categories=Category.objects.all()
    categories=categories.annotate(count=Count("product"))
    context={
        "product": individual_product,
        "categories": categories,
        "featured_prod_iterator": range(0, 3),
        "related": related,
        "product_reviews": product_reviews
    }
    return render(request, "product_detail/shop-detail.html", context)

def contact(request):
    return render(request, "contact/contact.html")