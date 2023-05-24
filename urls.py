from django.urls import path
from .views import *

urlpatterns = [
	path('', ToolListView.as_view()),
	path('tool/new', ToolCreateView.as_view()),
	path('tool/<int:pk>/delete', ToolDeleteView.as_view()),
	path('tool/<int:pk>', ToolUpdateView.as_view()),
]
