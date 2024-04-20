from django.views.generic import ListView
from .models import message
class messageView(ListView):
   model=message
   template_name='home.html'
   
