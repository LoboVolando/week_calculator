import datetime

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from rest_framework.decorators import api_view

from get_week.forms import DateForm
from get_week.utils import get_week_number


class DateView(View):
    """Index page date request view"""
    form = DateForm()

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {'form': self.form})

    def post(self, request, *args, **kwargs):
        self.form = DateForm(request.POST)

        if self.form.is_valid():
            date = self.form.cleaned_data.get('date')
            week = get_week_number(date)
            return render(request, 'index.html', {'form': self.form,
                                                  'week': week})

        return render(request, 'index.html', {'form': self.form})


@api_view(('GET',))
def api_date_view(request):
    """API date request view"""
    try:
        date = request.GET.get('date')
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        week = get_week_number(date)

        return JsonResponse({'reply': week})

    except ValueError:
        return JsonResponse({'reply': 'wrong date format'})
