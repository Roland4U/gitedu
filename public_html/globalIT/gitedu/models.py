from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class facultet(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(unique=True)
	sow_in_index = models.BooleanField(default = False)
	trainings = models.ManyToManyField('training', related_name='facultet')
	about = RichTextUploadingField()
	image = models.ImageField(upload_to="facultet/images/facimages")
	grad_color1 =  models.CharField(max_length=10, default = '#326b02')
	grad_color2 =  models.CharField(max_length=10, default = '#CEF9AB')

	class Meta:
		pass

	def __str__(self):
		return str(self.name)


class training(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(unique=True)
	status = models.CharField(max_length=50, default = 'Շուտով')
	about = RichTextUploadingField()
	image = models.ImageField(upload_to="facultet/images/trainingimages")

	def __str__(self):
		return str(self.name)

class subscribe(models.Model):
	email = models.EmailField()

	def __str__(self):
		return str(self.email)

class service(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(unique=True, default='order_')
	about = RichTextUploadingField()

	def __str__(self):
		return str(self.name)

class orderto(models.Model):
	name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	email = models.EmailField()
	date = models.DateTimeField(auto_now_add=True)
	fac = models.CharField(max_length=50)
	tra = models.CharField(max_length=50)

	def __str__(self):
		return '{0} - {1} - {2}'.format(self.name,self.fac,self.tra)

class ordertoserv(models.Model):
	name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	email = models.EmailField()
	date = models.DateTimeField(auto_now_add=True)
	serv = models.CharField(max_length=50)
	text = models.TextField(max_length=900)

	def __str__(self):
		return '{0} - {1}'.format(self.name,self.serv)