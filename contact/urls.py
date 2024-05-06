from django.urls import path
from .views import contact_form


urlpatterns = [
    path('x.html', contact_form, name='contact_form'),
]
