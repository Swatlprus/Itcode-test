from django_filters import filters

import core.models


class CompanyFilter(filters.Filter):
    name = filters.Filter()

    class Meta:
        model = core.models.Company
        fields = ('name', )