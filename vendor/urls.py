from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('vendor-list/', views.taskList, name="vendor-list"),
	path('vendor-detail/<str:pk>/', views.taskDetail, name="vendor-detail"),
	path('vendor-create/', views.taskCreate, name="task-create"),

	path('vendor-update/<str:pk>/', views.taskUpdate, name="vendor-update"),
	path('vendor-delete/<str:pk>/', views.taskDelete, name="vendor-delete"),
]