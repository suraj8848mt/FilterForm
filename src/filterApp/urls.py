
from django.urls import path

from .views import bootstrapfilter

urlpatterns = [
    path('', bootstrapfilter, name='bootstrap')
]

