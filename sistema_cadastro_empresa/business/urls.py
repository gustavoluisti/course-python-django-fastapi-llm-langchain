# from django.urls import path
# from . import views

# urlpatterns = [
#     path('business/', views.BusinessCreateListView.as_view() , name='business-create-list'),
#     path('business/<uuid:pk>', views.BusinessRetrieveUpdateDestroyView.as_view(), name='business-detail-view')
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from business import views

router = DefaultRouter()
router.register('business', views.BusinessViewSet, basename='business')

urlpatterns = [
    path('', include(router.urls))
]