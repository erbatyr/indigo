from django.urls import path

from django.urls import include

from . import views

urlpatterns = [
    path('', views.SortView.as_view(), name='index'),
    path('sort_by=<str:sort_data>', views.index, name='index_sorted'),
    path('<int:pk>/', views.CompanyDetail.as_view(), name='detail'),
    path('<int:pk>/edit', views.CompanyEdit.as_view(), name='edit'),
    path('<int:pk>/delete/', views.CompanyDelete.as_view(), name='delete'), 
    path('new_company/', views.CompanyCreate.as_view(), name='new_company'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('data.json', views.download, name="download"),
]