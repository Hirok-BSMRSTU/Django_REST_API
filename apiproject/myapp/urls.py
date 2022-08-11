from django.urls import path
from myapp import views

urlpatterns = [
    #path('myapi/', views.api_list),
    #path('apidetails/<int:pk>/', views.api_detail),
    path('myapi/', views.BlogList.as_view()),
    path('apidetails/<int:pk>/', views.BlogDetail.as_view()),
    path('gav/', views.ContractList.as_view()),
    path('gavdetails/<int:pk>/', views.ContractDetail.as_view()),
]