from django.views.generic import ListView
from app.models import Stock
from .filters import StockFilter


class BankerListView(ListView):
    model = Stock
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = StockFilter(self.request.GET, queryset=self.get_queryset())
        return context
