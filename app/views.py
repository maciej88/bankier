from django.views.generic import ListView
from app.models import Stock

class BankerListView(ListView):
    model = Stock
    queryset = Stock.objects.all()
    template_name = 'index.html'
