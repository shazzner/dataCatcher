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
    # TODO: TONS of error checking & formatting
    start_date = styear + '-' + stmonth + '-' + stday + ' 00:00'
    start_slice = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M')
    end_date = edyear + '-' + edmonth + '-' + edday + ' 23:59'
    end_slice = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M')
    range_slices = DataSlice.objects.filter(capture_time__range=(start_date, end_date))

    dateformatted = []
    currRoomTemp = []
    currRoomHumidity = []
    outsideTemp = []
    outsideHumidity = []

    for slice in range_slices:
        dateformatted.append("'" + slice.capture_time.strftime('%Y-%m-%d %H:%M') + "'")
        currRoomTemp.append(str(slice.curr_room_temp))
        currRoomHumidity.append(str(slice.curr_room_humid))
        outsideTemp.append(str(slice.local_outside_temp))
        outsideHumidity.append(str(slice.local_outside_humid))
        
    context = {
        'range_slices': range_slices,
        'dateformatted': dateformatted,
        'currRoomTemp': currRoomTemp,
        'currRoomHumidity': currRoomHumidity,
        'outsideTemp': outsideTemp,
        'outsideHumidity': outsideHumidity,
    }
        
    return render(request, 'weather/timeslice.html', context)
