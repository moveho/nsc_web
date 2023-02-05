from time import strptime, mktime

from rest_framework.viewsets import ModelViewSet

from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from django.http.response import JsonResponse
from django.views.generic import CreateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib import messages


from stockapp.models import Kospi
from stockapp.forms import KospiCreationForm
from stockapp.serializers import KospiSerializer


def KospiData(request):
    stocks = Kospi.objects.all().order_by('date')

    close_list = []
    open_list = []

    for stock in stocks:
        times = strptime(str(stock.date), '%Y-%m-%d')
        utc_now = mktime(times) * 1000

        close_list.append([utc_now, stock.close])
        open_list.append([utc_now, stock.open])

    data = {
        'close': close_list,
        'open': open_list,
    }

    return JsonResponse(data)

    
class KospiViewSet(ModelViewSet):
    queryset = Kospi.objects.all()
    serializer_class = KospiSerializer


class ChartView(View):
    def get(self, request, *args, **kwargs):
        kospi_list = Kospi.objects.order_by('date')
        return render(request, 'stockapp/chart.html', {'kospi_list': kospi_list})
    

def KospiCreate(request):
    if request.method == "POST":
        date = request.POST["date"]
        open = request.POST["open"]
        close = request.POST["close"]
        kospi_list = Kospi.objects.order_by('date')
        
        if not date or not open or not close:
            message = "필드에 누락된 값이 있습니다."
            return render(request, 'stockapp/chart.html', {'kospi_list': kospi_list, 'message': message})
        elif Kospi.objects.filter(date=date):
            message = "날짜가 중복됩니다."
            return render(request, 'stockapp/chart.html', {'kospi_list': kospi_list, 'message': message})
        else:
            Kospi(date=date, open=open, close=close).save()
            message = "추가 완료"
            kospi_list = Kospi.objects.order_by('date')
            return render(request, 'stockapp/chart.html', {'kospi_list': kospi_list, 'message': message})
            
    else:
        kospi_list = Kospi.objects.order_by('date')
        return render(request, 'stockapp/chart.html', {'kospi_list': kospi_list})


def KospiDelete(request, pk):
    if request.method == "POST":
        target_kospi = Kospi.objects.get(pk=pk)
        target_kospi.delete()
        
        kospi_list = Kospi.objects.order_by('date')
        message = "삭제 완료"
        return render(request, 'stockapp/chart.html', {'kospi_list': kospi_list, 'message': message})
        
    else:
        kospi_list = Kospi.objects.order_by('date')
        return render(request, 'stockapp/chart.html', {'kospi_list': kospi_list})
        