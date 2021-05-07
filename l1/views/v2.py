from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from ..models import scq,mcq,true_false,ans_given_scq,ans_given_mcq,ans_given_bool,answere
from django.contrib import auth
from ..serializers import scqserialize,mcqserialize,true_falseserialize
from django.contrib.auth.decorators import login_required
import json
class api_mcq(APIView):
	
	def get(self,request):
		if request.user.is_authenticated:
			p=scq.objects.filter(user=request.user)
			ser=scqserialize(p,many=True)
			return Response(ser.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)
	def post(self,request):
		if request.user.is_authenticated:
			p=json.loads(request.body)
			print(p)
			ans=answere(ans=p['ans'])
			ans.save()
			q=scq(user=request.user,question=p['question'],A=p['A'],B=p['B'],C=p['C'],D=p['D'],ans=ans)
			q.save()
			pq=scqserialize(q)
			return Response(pq.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)

class api_mcq_one(APIView):
	def get(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				p=scq.objects.get(id=id)
			except:
				return Response(status=status.HTTP_400_BAD_REQUEST)
			ser=scqserialize(p)
			return Response(ser.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				q=mcq.objects.get(id=id)
				if q.user!=request.user:
					return Response(status=status.HTTP_400_BAD_REQUEST)
				q.delete()
				return Response()
			except:
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def put(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				print("hello")
				q=scq.objects.get(id=id)
				if q.user!=request.user:
					return Response(status=status.HTTP_400_BAD_REQUEST)
				d=json.loads(request.body)
				if "question" in d:
					q.question=d['question']
				if "A" in d:
					q.A=d['A']
				if 'B' in d:
					q.B=d['B']
				if "C" in d:
					q.C=d['C']
				if 'B' in d:
					q.D=d['D']
				ans=q.ans
				if "ans" in d:
					ans.ans=d['ans']
					ans.save()
					q.ans=ans
				q.save()
				pq=scqserialize(q)
				return Response(pq.data)
			except:
				print("here")
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)
				



