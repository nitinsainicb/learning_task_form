from django.urls import path
from .import views
urlpatterns = [
	path('api_scq',views.api_scq.as_view(),name='api_scq'),
	path('api_scq/<int:id>',views.api_scq_one.as_view(),name='api_scq_one'),
]