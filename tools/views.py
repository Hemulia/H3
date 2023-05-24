from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import *

class ToolListView(ListView):
	model = Tool

class ToolUpdateView(UpdateView):
	model = Tool
	fields = ["name", "brand"]
	success_url = "/"

class ToolCreateView(CreateView):
	model = Tool
	fields = ["name", "brand"]
	success_url = "/"

class ToolDeleteView(DeleteView):
	model = Tool
	success_url = "/"
