# django_template_urls


## Description
Free Fruit and Vegetable shop website template is cut into different html templates files
and are organized in directories with the help of django templates, tags and inheritance.
The Project uses Django and sqlite3 database for testing the migrations and models. 
There are several records for fruits and vegetables.

## **Components** ##
* **store** - This app contains the 4 models(Product, Category, ProductReviews and ShopReviews). Models are self-explanatory. Has 4 views for homepage, contact, product detail and shop.
* **order** - This app contains the models(Checkout(which is the order basically), Cart and CartItems) and 2 views for the cart and checkout.
* **media** - All user uploaded images go to the media folder.
* **static** - for static files: JS, CSS, Images that is being used are all stored there.
* **templates** - avaialable templates.
* **db.sqlite3** - Database file.


### Templates
  * cart - in this directory there are components for cart, base_cart.html and cart.html.
  * checkout - in this directory there are components for checkout and base_checkout.html and checkout.html.
  * contact - in this directory there are components for contact and base_contact.html and contact.html.
  * homepage - in this directory there are components for homepage and base_index.html and index.html.
  * product_detail - in this directory there are components for product_detail and base_detail.html and shop-detail.html.
  * shop - in this directory there are components for shop and base_shop.html and shop.html.
  * reusable_components - Here are some reusable components that I'm using through templates and apps such as navbar, spinner and search.
  * base.html - The main base html file where all the shared code is which then is inherited in other templates.
  * footer.html - Footer component

### Urls
  * Home - is accessible on route `/`
  * Shop - is accessible on route `/category/kategoriebi/`
  * Detail - is accessible on route `/product/slug/`. Change the slug with product name. there are several products. Default is 'raspberry'.
  * Contact - is accessible on route `/contact/`
  * Cart - is accessible on route `/cart/`
  * Checkout - is accessible on route `/checkout/`
  * Admin Panel - is accessible on `/admin/`. Username is 'admin' and password is 'admin'.


## Dependencies
* **Python 3.X**
* **Django 5.1.1**
* **Pillow 10.4.0** - Python Imaging Library adds image processing capabilities to your Python interpreter.
* **Django-debug-toolbar** - Configurable set of panels that display various debug information about the current request/response.
* **Django-mptt** - Reusable Django app which aims to make it easy for you to use MPTT(a technique for storing hierarchical data in a database).


## Usage
Clone the repository:
```bash
git clone https://github.com/hella753/django_template_urls.git
cd django_template_urls
```
To install the dependencies, use the following command in your terminal:
```bash
pip install -r requirements.txt
```
To run the development server, use the following command in your terminal:
```bash
python manage.py runserver
```
To access the application, open your browser and go to http://127.0.0.1:8000/
