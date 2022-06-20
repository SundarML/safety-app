from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from inspection.models import equipments

# Create your views here.

class equipmentCreate(CreateView):
	model = equipments
	template_name = "equipments_form.html"
	fields = "__all__"
	success_url = "/list"
class equipmentListView(ListView):
	model = equipments
	template_name = "equipments_list.html"
	def get_query_set(self):
		qs = equipments.objects.all()
		return qs
class equipmentsDetailView(DetailView):
	model = equipments
	template_name = "equipments_detail.html"
