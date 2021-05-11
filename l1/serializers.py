from rest_framework import serializers
from .models import mcq_answere,mcq,true_false,tf_answere
from django.contrib.auth.models import User
class UserSerialize(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=['username','email']

class mcq_ansserialize(serializers.ModelSerializer):
	class Meta:
		model=mcq_answere
		fields='__all__'
class mcqserialize(serializers.ModelSerializer):
	
	class Meta:
		model=mcq
		fields=['id','question','A','B','C','D','is_mcq']
class true_falseserialize(serializers.ModelSerializer):
	class Meta:
		model=true_false
		fields='__all__'
class tf_answereserialize(serializers.ModelSerializer):
	class Meta:
		model=tf_answere
		fields='__all__'



