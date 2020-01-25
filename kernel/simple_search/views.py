from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q 

from .models import Link


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Link
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Link.objects.filter(
            Q(title__icontains=query) | Q(rate__icontains=query)
        )
        return object_list