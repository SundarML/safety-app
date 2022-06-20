from django.db import models

# Create your models here.

# Create your models here.
class equipments(models.Model):
	eqp_id = models.IntegerField('equipment id', primary_key=True)
	eqp_name = models.CharField('equipment name', max_length=30)
	department = models.CharField('equipment department', max_length=30)

	class meta:
		db_table = 'equipments'

	def __str__(self):
		return eqp_name
