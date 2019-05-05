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

class Category(models.Model):
	category_name = models.CharField(_('Name'), max_length=255, unique=True, null=False, blank=False)
	description = models.TextField(_('Description'), blank=True, null=True)
	image = models.ImageField(_('Featured Image - 100px x 100 px'), upload_to=category_feature_image_name, blank=True, null=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)	
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.category_name