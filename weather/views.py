from django.shortcuts import get_object_or_404, render
from datetime import datetime, timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from more_itertools import unique_everseen
from .models import DataSlice

def _daterange(start_date, end_date):
        end_date_date = end_date.date()
        start_date_date = start_date.date()
        for n in range(int ((end_date_date - start_date_date).days)):
            yield start_date + timedelta(n)

            
# Create your views here.
def index(request):
    # first we want to get the start date and the end date
    start_date = DataSlice.objects.first()
    end_date = DataSlice.objects.last()
    # Add one more day to it
    end_date = end_date.capture_time + timedelta(days=1)

    dates = []
    
    for single_date in _daterange(start_date.capture_time, end_date):
        dates.append(datetime.strftime(single_date, '%Y-%m-%d'))

    # for date in dates:
    #     # styear + '-' + stmonth + '-' + stday + ' 00:00'
    #     # edyear + '-' + edmonth + '-' + edday + ' 23:59'
    #     start_slice = date.replace(minute=0, second=0)
    #     end_slice = date.replace(minute=23, second=59)
    #     range_slices = []
    #     try:
    #         range_slices = DataSlice.objects.filter(capture_time__range=(start_slice, end_slice)).get()
    #     except:
    #         pass
    #     if range_slices: slices_by_date.append(range_slices)

    #latest_data_slices = DataSlice.objects.order_by('-capture_time')
    paginator = Paginator(dates, 5)
    
    page = request.GET.get('page')
    try:
        slices = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        slices = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        slices = paginator.page(paginator.num_pages)
        
    context = {'slices' : slices}
    return render(request, 'weather/index.html', context)

def detail(request, data_id):
    data_id = get_object_or_404(DataSlice, pk=data_id)
    return render(request, 'weather/detail.html', {'data_id': data_id})

def timeslice(request, styear, stmonth, stday, edyear, edmonth, edday):
    # TODO: TONS of error checking & formatting
    # TODO: Look into doing smarter lists see: https://docs.djangoproject.com/en/dev/ref/models/querysets/#values-list
    
    start_date = styear + '-' + stmonth + '-' + stday + ' 00:00'
    end_date = edyear + '-' + edmonth + '-' + edday + ' 23:59'
    range_slices = DataSlice.objects.filter(capture_time__range=(start_date, end_date))

    dateformatted = []
    currRoomTemp = []
    currRoomHumidity = []
    outsideTemp = []
    outsideHumidity = []
    weatherIcon = 'clear-day'

    for slice in range_slices:
        dateformatted.append("'" + slice.capture_time.strftime('%Y-%m-%d %H:%M') + "'")
        currRoomTemp.append(str(slice.curr_room_temp))
        currRoomHumidity.append(str(slice.curr_room_humid))
        outsideTemp.append(str(slice.local_outside_temp))
        outsideHumidity.append(str(slice.local_outside_humid))
        weatherIcon = str(slice.local_outside_icon)
        
    context = {
        'range_slices': range_slices,
        'dateformatted': dateformatted,
        'currRoomTemp': currRoomTemp,
        'currRoomHumidity': currRoomHumidity,
        'outsideTemp': outsideTemp,
        'outsideHumidity': outsideHumidity,
        'weatherIcon': weatherIcon,
    }
        
    return render(request, 'weather/timeslice.html', context)

def export(request, styear, stmonth, stday, edyear, edmonth, edday):
    return render(request, 'weather/today.html', context)

def today(request):
    return render(request, 'weather/today.html', context)

def day(request, year, month, day):
    #date = year + '-' + month + '-' + day
    start_date = year + '-' + month + '-' + day + ' 00:00'
    #start_slice = datetime.strptime(start_date, '%Y-%m-%d %H:%M')
    end_date = year + '-' + month + '-' + day + ' 23:59'
    #end_slice = datetime.strptime(start_date, '%Y-%m-%d %H:%M')
    #range_slices = DataSlice.objects.filter(capture_time__range=(start_slice, end_slice))
    range_slices = DataSlice.objects.filter(capture_time__range=(start_date, end_date))
    #range_slices = DataSlice.objects.filter(capture_time__exact=datetime.date(year, month, day))

    dateformatted = []
    currRoomTemp = []
    currRoomHumidity = []
    outsideTemp = []
    outsideHumidity = []
    weatherIcons = []

    for slice in range_slices:
        dateformatted.append("'" + slice.capture_time.strftime('%Y-%m-%d %H:%M') + "'")
        currRoomTemp.append(str(slice.curr_room_temp))
        currRoomHumidity.append(str(slice.curr_room_humid))
        outsideTemp.append(str(slice.local_outside_temp))
        outsideHumidity.append(str(slice.local_outside_humid))
        weatherIcons.append(str(slice.local_outside_icon))

    # This can probably be replaced by a non-library call
    weatherIcons = list(unique_everseen(weatherIcons))
        
    context = {
        'range_slices': range_slices,
        'dateformatted': dateformatted,
        'currRoomTemp': currRoomTemp,
        'currRoomHumidity': currRoomHumidity,
        'outsideTemp': outsideTemp,
        'outsideHumidity': outsideHumidity,
        'weatherIcons': weatherIcons,
    }
    return render(request, 'weather/day.html', context)
