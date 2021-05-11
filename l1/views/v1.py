from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from ..models import answere,mcq,true_false,ans_given_mcq,ans_given_bool
from django.contrib import auth
from ..serializers import ansserialize,mcqserialize,true_falseserialize
from django.contrib.auth.decorators import login_required
import json
class api_scq(APIView):
	
	def get(self,request):
		if request.user.is_authenticated:
			p=mcq.objects.filter(user=request.user)
			ser=mcqserialize(p,many=True)
			return Response(ser.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)
	def get_ans(self,request):
		if request.user.is_authenticated:
			p=mcq.objects.filter(user=request.user)
			ser=mcqserialize(p,many=True)
			return Response(ser.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)
	
	def post(self,request):
		if request.user.is_authenticated:
			p=json.loads(request.body)
			if 'question' not in p or 'A' not in p or 'B' not in p or 'C' not in p or 'D' not in p or 'ans' not in p:
				return Response(status=status.HTTP_400_BAD_REQUEST)
			q=mcq(user=request.user,question=p['question'],A=p['A'],B=p['B'],C=p['C'],D=p['D'])
			q.save()
			for i in p['ans']:
				print(i)
				if i not in ['A','B','C','D']:
					return Response(status=status.HTTP_400_BAD_REQUEST)
				a=answere(ans=i,question=q)
				a.save()
			pq=mcqserialize(q)
			return Response(pq.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)

class api_scq_one(APIView):
	def get(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				p=mcq.objects.get(id=id)
			except:
				return Response(status=status.HTTP_400_BAD_REQUEST)
			ser=mcqserialize(p)
			return Response(ser.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				q=mcq.objects.get(id=id)
				a=answere.objects.filter(question=q)
				for i in a:
					i.delete()
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
				q=mcq.objects.get(id=id)
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
				if 'ans' in d:
					aold=answere.objects.filter(question=q)
					for i in aold:
						i.delete()
					for i in d['ans']:
						a=answere(ans=i,question=q)
						a.save()
				q.save()
				pq=mcqserialize(q)
				return Response(pq.data)
			except:
				print("here")
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)
				



