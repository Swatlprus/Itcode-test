import django_filters
import core.models


class CompanyFilter(django_filters.FilterSet):
    name = django_filters.Filter(lookup_expr='icontains', label='Название')
    rate = django_filters.Filter(lookup_expr='gte', label='Рейтинг (не менее)')

    class Meta:
        model = core.models.Company
        fields = ('name', 'rate', )