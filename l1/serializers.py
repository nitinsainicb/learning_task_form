from rest_framework import serializers
from .models import answere,mcq,true_false,ans_given_mcq,ans_given_bool
from django.contrib.auth.models import User
class UserSerialize(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=['username','email']

class ansserialize(serializers.ModelSerializer):
	class Meta:
		model=answere
		fields='__all__'
class mcqserialize(serializers.ModelSerializer):
	
	class Meta:
		model=mcq
		fields=['id','question','A','B','C','D']
class true_falseserialize(serializers.ModelSerializer):
	class Meta:
		model=true_false
		fields='__all__'



