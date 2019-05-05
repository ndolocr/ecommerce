
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

def category_feature_image_name(instance, filename):
	#Get file expension
	ext = filename.split('.')[-1]
	#Getting current time
	current_time = datetime.datetime.now()

	filename = '{}.{}'.format(current_time, ext)
	return os.path.join('category_featued_image', filename)

def product_feature_image_name(instance, filename):
	#Get file expension
	ext = filename.split('.')[-1]
	#Getting current time
	current_time = datetime.datetime.now()

	filename = '{}.{}'.format(current_time, ext)
	return os.path.join('product_featued_image', filename)

class Category(models.Model):
	category_name = models.CharField(_('Name'), max_length=255, blank=False, null=False, unique=True)
	description = models.TextField(_('Description'), blank=True, null=True)
	image = models.ImageField(_('Featured Image - 100px x 100 px'), upload_to=category_feature_image_name, blank=True, null=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)	
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.category_name


class Product(models.Model):
	product_name = models.CharField(_('Name'), max_length=255, blank=False, null=False,  unique=True)
	category = models.OneToOneField(Category, on_delete=models.CASCADE)
	brand = models.CharField(_('Brand'), max_length=255, blank=False, null=False, unique=False)
	size = models.CharField(_('size'), max_length=255, blank=False, null=False, unique=False)
	color = models.CharField(_('Color'), max_length=255, blank=False, null=False, unique=False)
	description = models.TextField(_('Description'), blank=True, null=True)
	image = models.ImageField(_('Featured Image - 100px x 100 px'), upload_to=product_feature_image_name, blank=True, null=True)
	stock_level = models.IntegerField(_('Stock Level'), blank=True, default = 0, null=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)

	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Products'

	def __str__(self):
		return self.product_name


class Restock(models.Model):
	product = models.OneToOneField(Product, on_delete=models.CASCADE)
	supplier = models.CharField(_('Supplier'), max_length=255, blank=False, null=False, default=None)
	buying_price = models.FloatField(_('Buying Price'), blank=False, null=False, default=None)
	selling_price = models.FloatField(_('Selling Price'), blank=False, null=False, default=None)
	units_bought = models.IntegerField(_('Units Purchased'), blank=False, null=False, default=None)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)

	class Meta:
		verbose_name = 'Restock'
		verbose_name_plural = 'Restock'

	def __str__(self):
		restock_name = self.product
		return restock_name