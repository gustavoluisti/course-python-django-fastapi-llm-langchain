from django.urls import path
from . import views

urlpatterns = [
    path('business/', views.BusinessCreateListView.as_view() , name='business-create-list')
]