from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
	listing = models.CharField(max_length=200)
	listing_id = models.IntegerField()
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	message = models.TextField(blank=True)
	contact_date = models.DateTimeField(default=datetime.now, blank = True)
	user_id = models.IntegerField(blank =True)
	def __str__(self):
		return self.name
	
""" To add Contacts to database; The following needs to be done:

1. Make migrations in terminal, using the following command:	python manage.py makemigrations contacts
	This creates a migration file as shown in the terminal	
		Migrations for 'contacts':
	  	contacts/migrations/0001_initial.py
	    - Create model Contact

2. Run the migration file in terminal using:	Python manage.py migrate

3. Check database by opening pgAdmin4 and Navigating to the path:
	dbserver->Databases->barriedb->Schemas->public->Tables->contacts_contact(right click)

4. Register on admin site using admin.py	
"""
