from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
class answere(models.Model):
	class options(models.TextChoices):
		A = "A", _("A")
		B = "B", _("B")
		C = "C", _("C")
		D = "D", _("D")
	ans=models.CharField(max_length=1,choices=options.choices)
	question=models.ForeignKey(scq,on_delete=models.CASCADE)

class scq(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	question=models.CharField(max_length=200)
	A=models.CharField(max_length=100)
	B=models.CharField(max_length=100)
	C=models.CharField(max_length=100)
	D=models.CharField(max_length=100)
	ans=models.ForeignKey(answere,on_delete=models.CASCADE)

class mcq(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	question=models.CharField(max_length=200)
	A=models.CharField(max_length=100)
	B=models.CharField(max_length=100)
	C=models.CharField(max_length=100)
	D=models.CharField(max_length=100)
	ans=models.ManyToManyField(answere)

class true_false(models.Model):	
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	question=models.CharField(max_length=200)
	ans=models.BooleanField(default=False)

class ans_given_scq(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	question=models.ForeignKey(scq,on_delete=models.CASCADE)
	ans=models.ForeignKey(answere,on_delete=models.CASCADE)

class ans_given_mcq(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	question=models.ForeignKey(mcq,on_delete=models.CASCADE)
	ans=models.ManyToManyField(answere)

class ans_given_bool(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	question=models.ForeignKey(scq,on_delete=models.CASCADE)
	ans=models.BooleanField(default=False)


