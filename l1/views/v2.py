from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from ..models import mcq_answere,mcq,true_false,tf_answere
from django.contrib import auth
from django.db.models import Q

from django.contrib.auth.models import User
from ..serializers import UserSerialize,mcqserialize,mcq_ansserialize,true_falseserialize,tf_answereserialize
from django.contrib.auth.decorators import login_required
import json
class api_mcq_answere(APIView):
	
	def get(self,request):
		if request.user.is_authenticated:
			teacher=request.GET.get("teacher")
			user=User.objects.get(username=teacher)
			q=mcq.objects.filter(user=user)
			p=[]
			# for i in q:
			# 	x=mcq_answere.objects.filter(user=request.user,question=i)
			# 	for j in x:
			# 		p.append(j)
			p=mcq_answere.objects.filter(user=request.user,question__in=q)
			ser=mcq_ansserialize(p,many=True)
			return Response(ser.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request):
		if request.user.is_authenticated:
			q=mcq_answere.objects.filter(user=request.user)
			for i in q:
				i.delete()
			return Response({"success":"all answeres are deleted"})
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class api_mcq_answere_one(APIView):

	def delete(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				q=mcq.objects.get(id=id)
				ans=mcq_answere.objects.filter(user=request.user,question=q)
				for i in ans:
					i.delete()
				return Response()
			except:
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)
	def post(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				q=mcq.objects.get(id=id)
				a=mcq_answere.objects.filter(user=request.user,question=q)
				if len(a)!=0 and q.is_mcq==False:
					return Response({"error":"you already responded try to update or delete response"})
				print(q)
				print("hello")
				d=request.data
				print(d['ans'])
				if 'ans' in d:
					i=d['ans']
					if i in ['A','B','C','D']:
						for x in a:
							if x.ans==i:
								return Response({"error":"already responded"})
						ans=mcq_answere(user=request.user,question=q,ans=i)
						ans.save()
					return Response({"success":"saved"})

			except:
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)

class api_tf_answere(APIView):
	
	def get(self,request):
		if request.user.is_authenticated:
			p=tf_answere.objects.filter(user=request.user)
			ser=tf_answereserialize(p,many=True)
			return Response(ser.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request):
		if request.user.is_authenticated:
			q=tf_answere.objects.filter(user=request.user)
			for i in q:
				i.delete()
			return Response({"success":"all t/f answeres are deleted"})
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class api_tf_answere_one(APIView):

	def delete(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				q=true_false.objects.get(id=id)
				ans=tf_answere.objects.filter(user=request.user,question=q)
				for i in ans:
					i.delete()
				return Response()
			except:
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)
	def post(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				print("hello")
				q=true_false.objects.get(id=id)
				a=tf_answere.objects.filter(user=request.user,question=q)
				print(q)
				for i in a:
					i.delete()
				d=request.data
				if 'ans' in d:
					if bool(d['ans']) in [True,False]:
						ans=tf_answere(user=request.user,question=q,ans=bool(d['ans']))
						ans.save()
						a=tf_answereserialize(ans)
						return Response(a.data)

			except:
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)

