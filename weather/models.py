from django.db import models

# Create your models here.
class DataSlice(models.Model):
    capture_time = models.DateTimeField(auto_now_add=True, blank=False, unique=True)
    curr_room_temp = models.DecimalField(max_digits=3, decimal_places=1)
    curr_room_humid = models.DecimalField(max_digits=3, decimal_places=1)
    local_outside_icon = models.CharField(max_length=30)
    local_outside_temp = models.DecimalField(max_digits=3, decimal_places=1)
    local_outside_humid = models.DecimalField(max_digits=3, decimal_places=1)
    local_outside_apparent_temp = models.DecimalField(max_digits=3, decimal_places=1)

    def __unicode__(self):
        return str(self.capture_time)

# class DataModel(models.Model):
#     chart = models.ForeignKey(DataChart)
#     data_start_time = models.DateTimeField(blank=false)
#     data_end_time = models.DateTimeField(blank=false)

# class DataChart(models.Model):
#     chart_type = models.Charfield(max_length=30, blank=false, unique=True)
