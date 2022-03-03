from django.urls import path
import core.views

urlpatterns = [
    path('', core.views.main_page),
]