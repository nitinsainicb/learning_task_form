from rest_framework import serializers
from .models import scq,mcq,true_false,ans_given_scq,ans_given_mcq,ans_given_bool
from django.contrib.auth.models import User
class UserSerialize(serializers.ModelSerializer):
	class Meta:
		mdoel=User
		fields=['username','email']
class scqserialize(serializers.ModelSerializer):
	ans=serializers.SerializerMethodField()
	
	class Meta:
		model=scq
		fields=['id','question','A','B','C','D','ans']
	def get_ans(self,instance):
		return instance.ans.ans
class mcqserialize(serializers.ModelSerializer):
	class Meta:
		model=mcq
		fields='__all__'

class true_falseserialize(serializers.ModelSerializer):
	class Meta:
		model=true_false
		fields='__all__'



