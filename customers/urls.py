from django.urls import path
from . import views as Views

urlpatterns = [
    path('RequestPage/', Views.RequestPage),
    path('ViewRequestPage/', Views.ViewRequestPage),
    path('', Views.RequestPage),
]