import django_filters

class StockFilter(django_filters.FilterSet):
    CHOICES = (
        ('ascending', 'asc'),
        ('descending', 'desc')
    )
    name = django_filters.ChoiceFilter(label='Sort', choices=CHOICES, method='filter_by_order')


    def filter_by_order(self, queryset, name, value):
        expression = 'name' if value == 'ascending' else '-name'
        return queryset.order.by(expression)