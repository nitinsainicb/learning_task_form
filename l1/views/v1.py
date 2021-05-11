from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from ..models import mcq_answere,mcq,true_false,tf_answere
from django.contrib import auth
from django.contrib.auth.models import User
from ..serializers import UserSerialize,mcqserialize,mcq_ansserialize,true_falseserialize,tf_answereserialize
from django.contrib.auth.decorators import login_required
import json
class api_mcq_question(APIView):
	
	def get(self,request):
		if request.user.is_authenticated:
			try:
				print("hello")
				teacher=self.request.GET.get("teacher")
				print(teacher)
				t=User.objects.get(username=teacher)
				print(t)
				p=mcq.objects.filter(user=t)
			except:
				return Response({"error":"invalid teacher name"},status=status.HTTP_400_BAD_REQUEST)
			ser=mcqserialize(p,many=True)
			return Response(ser.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def post(self,request):
		if request.user.is_authenticated:
			print("hello")
			question=self.request.data.get('question')
			A=self.request.data.get('A')
			B=self.request.data.get('B')
			C=self.request.data.get('C')
			D=self.request.data.get('D')
			
			is_mcq=False
			try:
				is_mcq=self.request.data.get('is_mcq')
			except:
				is_mcq=False
			q=mcq(user=request.user,question=question,A=A,B=B,C=C,D=D,is_mcq=is_mcq)
			q.save()
			pq=mcqserialize(q)
			return Response(pq.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)
	def delete(self,request):
		if request.user.is_authenticated:
			q=mcq.objects.filter(user=request.user)
			for i in q:
				i.delete()
			return Response({"success":"all question deleted"})
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class api_mcq_one(APIView):
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
				if q.user!=request.user:
					return Response({"error":"you are not the crator of this question so you cant do this"},status=status.HTTP_400_BAD_REQUEST)
				q.delete()
				return Response()
			except:
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def patch(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				q=mcq.objects.get(id=id)
				if q.user!=request.user:
					return Response({"error":"you are not the crator of this question so you cant do this"},status=status.HTTP_400_BAD_REQUEST)
				if "question" in self.request.data:
					q.question=self.request.data.get('question')
				if "A" in self.request.data:
					q.A=self.request.data.get('A')
				if 'B' in self.request.data:
					q.B=self.request.data.get('B')
				if "C" in self.request.data:
					q.C=self.request.data.get('C')
				if 'D' in self.request.data:
					print(self.request.data.get('D'))
					q.D=self.request.data.get('D')
				if 'is_mcq' in self.request.data:
					q.is_mcq=self.request.data.get('is_mcq')
				q.save()
				pq=mcqserialize(q)
				return Response(pq.data)
			except:
				print("here")
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)
				



class api_tf_question(APIView):
	
	def get(self,request):
		if request.user.is_authenticated:
			try:
				teacher=self.request.GET.get("teacher")
				t=User.objects.get(username=teacher)
				p=true_false.objects.filter(user=t)
			except:
				return Response({"error":"invalid teacher name"},status=status.HTTP_400_BAD_REQUEST)
			ser=true_falseserialize(p,many=True)
			return Response(ser.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)
	def post(self,request):
		if request.user.is_authenticated:
			p=self.request.data
			if 'question' not in p:
				return Response({"error":"provide question and all options"},status=status.HTTP_400_BAD_REQUEST)
			
			q=true_false(user=request.user,question=p['question'])
			q.save()
			pq=true_falseserialize(q)
			return Response(pq.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)
	def delete(self,request):
		if request.user.is_authenticated:
			q=true_false.objects.filter(user=request.user)
			for i in q:
				i.delete()
			return Response({"success":"all question deleted"})
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class api_tf_one(APIView):
	def get(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				p=true_false.objects.get(id=id)
			except:
				return Response(status=status.HTTP_400_BAD_REQUEST)
			ser=true_falseserialize(p)
			return Response(ser.data,status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				q=true_false.objects.get(id=id)
				if q.user!=request.user:
					return Response({"error":"you are not the crator of this question so you cant do this"},status=status.HTTP_400_BAD_REQUEST)
				q.delete()
				return Response()
			except:
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)

	def patch(self,request,id,*args,**kwargs):
		if request.user.is_authenticated:
			try:
				q=true_false.objects.get(id=id)
				if q.user!=request.user:
					return Response({"error":"you are not the crator of this question so you cant do this"},status=status.HTTP_400_BAD_REQUEST)
				d=request.data
				if "question" in d:
					q.question=d['question']
				q.save()
				pq=true_falseserialize(q)
				return Response(pq.data)
			except:
				print("here")
				pass
		return Response(status=status.HTTP_400_BAD_REQUEST)
				


