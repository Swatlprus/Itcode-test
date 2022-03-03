from django.shortcuts import render
import core.models


def main_page(request):
    rating = core.models.Company.objects.all()
    return render(request, 'core/index.html', {'company': rating})

# Create your views here.
