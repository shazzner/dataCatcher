from django.shortcuts import get_object_or_404, render
import datetime
from .models import DataSlice

# Create your views here.
def index(request):
    latest_data_slices = DataSlice.objects.order_by('-capture_time')[:5]
    context = {'latest_data_slices' : latest_data_slices}
    return render(request, 'weather/index.html', context)

def detail(request, data_id):
    data_id = get_object_or_404(DataSlice, pk=data_id)
    return render(request, 'weather/detail.html', {'data_id': data_id})

def timeslice(request, styear, stmonth, stday, edyear, edmonth, edday):
    start_date = styear + '-' + stmonth + '-' + stday + ' 00:00'
    start_slice = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M')
    end_date = edyear + '-' + edmonth + '-' + edday + ' 23:59'
    end_slice = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M')
    range_slices = DataSlice.objects.filter(capture_time__range=(start_date, end_date))
    return render(request, 'weather/timeslice.html', {'range_slices': range_slices})
