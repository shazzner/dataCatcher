from django.shortcuts import get_object_or_404, render

from .models import DataSlice

# Create your views here.
def index(request):
    latest_data_slices = DataSlice.objects.order_by('-capture_time')[:5]
    context = {'latest_data_slices' : latest_data_slices}
    return render(request, 'weather/index.html', context)

def detail(request, data_id):
    data_id = get_object_or_404(DataSlice, pk=data_id)
    return render(request, 'weather/detail.html', {'data_id': data_id})
