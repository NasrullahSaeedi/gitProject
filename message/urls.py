from django.urls import path
from .views import messageView

urlpatterns = [
    path('',messageView.as_view(),name='message'),
]
