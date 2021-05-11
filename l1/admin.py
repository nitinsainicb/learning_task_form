from django.contrib import admin

from .models import mcq,mcq_answere,true_false,tf_answere
admin.site.register(mcq)
admin.site.register(mcq_answere)
admin.site.register(true_false)
admin.site.register(tf_answere)
