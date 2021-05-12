from django.urls import path
from .import views
urlpatterns = [
	path('api_mcq',views.api_mcq_question.as_view(),name='api_mcq'),
	path('api_mcq/<int:id>',views.api_mcq_one.as_view(),name='api_mcq_one'),
	path('api_tf',views.api_tf_question.as_view(),name='api_tf_one'),
	path('api_tf/<int:id>',views.api_tf_one.as_view(),name='api_tf_question'),

	path('api_mcq_ans',views.api_mcq_answere.as_view(),name='api_mcq_answere'),
	path('api_mcq_ans/<int:id>',views.api_mcq_answere_one.as_view(),name='api_mcq_answere_one'),
	path('api_tf_ans',views.api_tf_answere.as_view(),name='api_tf_answere'),
	path('api_tf_ans/<int:id>',views.api_tf_answere_one.as_view(),name='api_tf_answere_one'),
	path('user',views.user.as_view(),name='user'),
]
