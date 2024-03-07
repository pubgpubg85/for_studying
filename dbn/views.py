from django.shortcuts import render
from .models import Dbns
from django.views import generic
from pathlib import Path


class DbnsView(generic.ListView):
    model = Dbns
    template_name = 'dbn/index.html'
    context_object_name = 'pdf_files'


class DetailView(generic.DetailView):
    model = Dbns
    template_name = 'dbn/detail.html'
    context_object_name = 'pdf_file'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     ROOT = Path.cwd()
    #     pdf_dir = ROOT / "media" / "dbns"
    #     pdf_files = list(Path(pdf_dir).glob("*.pdf"))
    #     context['pdf_files'] = pdf_files
    #     return context