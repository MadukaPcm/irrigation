from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import json
from moisture.models import *
from django.template import loader 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
 

def uploadsensors(request):
	id = request.GET['id']
	sensor_1 =request.GET['sensor_1']
	sensor_2 = request.GET['sensor_2']
	temperature = request.GET['temperature']
	humidity = request.GET['humidity']
	pump_1 = request.GET['pump_1']
	pump_2 = request.GET['pump_2']
	print("id>>>>>>>>>>>>>",id)
	print("sensor_1>>>>>>>",sensor_1)
	print("sensor_2>>>>>>>",sensor_2)
	print("temperature>>>>",temperature)
	print("humidity>>>>>>>",humidity)
	print("pump_1>>>>>>>>>",pump_1)
	print("pump_2>>>>>>>>>",pump_2)
	data = DataTable(id=id,sensor_1=sensor_1,sensor_2=sensor_2,temperature=temperature,humidity=humidity,pump_1=pump_1,pump_2=pump_2)
	data.save()
	dataraw = SettingTable.objects.all().values()
	json_data = json.dumps(list(dataraw))
	return HttpResponse(json_data,content_type='application/json')

def uploadsetting(request):
	id = request.GET['id']
	minsensor_1 = request.GET['minsensor_1']
	maxsensor_1 = request.GET['maxsensor_1']
	minsensor_2 = request.GET['minsensor_2']
	maxsensor_2 = request.GET['maxsensor_2']
	data = SettingTable(id=id,minsensor_1=minsensor_1,maxsensor_1=maxsensor_1,minsensor_2=minsensor_2,maxsensor_2=maxsensor_2)
	data.save()
	dataraw = SettingTable.objects.all().values()
	json_data = json.dumps(list(dataraw))
	return HttpResponse(json_data,content_type='application/json')

def members(request):
  template = loader.get_template('reading.html')
  mymembers = DataTable.objects.all().values()
  setting = SettingTable.objects.all().values()
  context = {
  'mymembers': mymembers,
  'setting' : setting,
  }
  return HttpResponse(template.render(context, request))


def getReading(request):
  
    model_a = DataTable.objects.first() 
    model_b = SettingTable.objects.first() 

    # Prepare data dictionaries
    model_a_data = {
			"sensor_1": model_a.sensor_1,
			"sensor_2": model_a.sensor_2,
			"temperature": model_a.temperature,
			"humidity": model_a.humidity,
			"pump_1": model_a.pump_1,
			"pump_2": model_a.pump_2,
			"time_min": model_a.get_time_dft_in_min(),
    }

    model_b_data = {
			"minsensor_1": model_b.minsensor_1,
			"maxsensor_1": model_b.maxsensor_1,
			"minsensor_2": model_b.minsensor_2,
			"maxsensor_2": model_b.maxsensor_2,
			"plant_1": model_b.plant_1,
			"plant_2": model_b.plant_2,
    }

    # Combine data into a list
    combined_data = [model_a_data, model_b_data]

    return JsonResponse(combined_data, safe=False)


def set(request):
	template = loader.get_template('set.html')
	mymembers = SettingTable.objects.all().values()
	context = {
	'mymembers': mymembers,
	}
	return HttpResponse(template.render(context, request))

 

def uploadsettingWeb(request):
	id = request.GET['id']
	minsensor_1 = request.GET['minsensor_1']
	maxsensor_1 = request.GET['maxsensor_1']
	minsensor_2 = request.GET['minsensor_2']
	maxsensor_2 = request.GET['maxsensor_2']
	plant_1=request.GET['plant_1']
	plant_2=request.GET['plant_2']
	data = SettingTable(id=id,minsensor_1=minsensor_1,maxsensor_1=maxsensor_1,minsensor_2=minsensor_2,maxsensor_2=maxsensor_2,plant_1=plant_1,plant_2=plant_2)
	data.save()
	template = loader.get_template('reading.html')
	mymembers = DataTable.objects.all().values()
	setting = SettingTable.objects.all().values()
	context = {
	'mymembers': mymembers,
	'setting' : setting,
	}
	return HttpResponse(template.render(context, request))


@csrf_exempt  
def upload_data(request):
	if request.method == 'POST':
   
		success = "success"
  
		data_dict = json.loads(request.body.decode('utf-8'))
		
		id = 1
		minsensor_1 = data_dict.get('minsensor_1')
		maxsensor_1 = data_dict.get('maxsensor_1')
		minsensor_2 =data_dict.get('minsensor_2')
		maxsensor_2=data_dict.get('maxsensor_2') 
		plant_1=data_dict.get('plant_1')
		plant_2=data_dict.get('plant_2' )

		data = SettingTable(id=id,minsensor_1=minsensor_1,maxsensor_1=maxsensor_1,minsensor_2=minsensor_2,maxsensor_2=maxsensor_2,plant_1=plant_1,plant_2=plant_2)
		data.save()
  
          
	return HttpResponse({"status":success})
