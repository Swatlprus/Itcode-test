from django.urls import path
import core.views
app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view(), name='index'),
    path('rating/', core.views.Company.as_view(), name='company_list'),
    path('rating/<int:pk>/', core.views.CompanyDetail.as_view(), name='company_detail'),
]