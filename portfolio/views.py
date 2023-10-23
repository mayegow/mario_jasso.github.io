from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "landing/home.html"
    


class PortfolioView(TemplateView):
    template_name = "landing/portfolio.html"



# Create your views here.