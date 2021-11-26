from django.db import models

class User(models.Model):
	user_id=models.AutoField(auto_created=True,primary_key=True)
	fname=models.CharField(max_length=30)
	lname=models.CharField(max_length=30)
	email=models.CharField(max_length=50)
	number=models.IntegerField()
	user_name=models.CharField(max_length=30)
	password=models.CharField(max_length=50)
	repassword=models.CharField(max_length=50)

	class Meta:
		db_table="user"

class Games(models.Model):
	game_id=models.AutoField(auto_created=True,primary_key=True)
	name=models.CharField(max_length=30)
	shift_choices = (
			('Morning','Morning'),
			('Day','Day'),
			('Evening','Evening'),
		)
	shift=models.CharField(max_length=30, choices= shift_choices)
	package_choice = (
			('Basic','Basic'),
			('Medium','Medium'),
			('Standard','Standard'),
		)
	package=models.CharField(max_length=30, choices= package_choice)

	class Meta:
		db_table="games"


class Admin(models.Model):
	id=models.AutoField(auto_created=True,primary_key=True)
	fname=models.CharField(max_length=30)
	lname=models.CharField(max_length=30)
	username=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	class Meta:
		db_table="admin"


class Book(models.Model):
	id=models.AutoField(auto_created=True,primary_key=True)
	fname=models.CharField(max_length=30)
	lname=models.CharField(max_length=30)
	game=models.CharField(max_length=30)
	shift_choices = (
			('Morning','Morning'),
			('Day','Day'),
			('Evening','Evening'),
		)
	shift=models.CharField(max_length=30, choices= shift_choices)
	package_choice = (
			('Basic','Basic'),
			('Medium','Medium'),
			('Standard','Standard'),
		)
	package=models.CharField(max_length=30, choices= package_choice)
	number=models.CharField(max_length=30)
	username=models.CharField(max_length=30)
	class Meta:
		db_table="book"		

class Message(models.Model):
	id=models.AutoField(auto_created=True,primary_key=True)
	message=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	class Meta:
		db_table="message"

