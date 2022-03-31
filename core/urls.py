from django.urls import path, include
import core.views
app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view(), name='index'),
    path('rating/', core.views.Company.as_view(), name='company_list'),
    path('rating/<int:pk>/', core.views.CompanyDetail.as_view(), name='company_detail'),
    path('rating/create/', core.views.CompanyCreate.as_view(), name='company_create'),
    path('rating/<int:pk>/update', core.views.CompanyUpdate.as_view(), name='company_update'),
    path('rating/<int:pk>/delete', core.views.CompanyDelete.as_view(), name='company_delete'),
]
