from django.shortcuts import render
from django.http import HttpResponse
import json
from moisture.models import *
from django.template import loader
# Create your views here.
 




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




  



# def uploadsensors(request):
#     # id = request.GET['id']
# 	# sensor_1 = request.GET['sensor_1']
# 	# sensor_2 = request.GET['sensor_2']
# 	# temperature = request.GET['temperature']
# 	# humidity = request.GET['humidity']
# 	# pump_1 = request.GET['pump_1']
# 	# pump_2 = request.GET['pump_2']
# 	# print("id>>>>>>>>>>>>>",id)   
#     # print("sensor_1>>>>>>>",sensor_1)
#     # print("sensor_2>>>>>>>",sensor_2)   
#     # print("temperature>>>>",temperature)
#     # print("humidity>>>>>>>",humidity)   
#     # print("pump_1>>>>>>>>>",pump_1)
#     # print("pump_2>>>>>>>>>",pump_2)
#     # data = DataTable(id=id,sensor_1=sensor_1,sensor_2=sensor_2,temperature=temperature,humidity=humidity,pump_1=pump_1,pump_2=pump_2)
# 	# data.save()
#     # dataraw = SettingTable.objects.all().values()
#     # json_data = json.dumps(list(dataraw))
#     # return HttpResponse(json_data,content_type='application/json')

# def uploadsetting(request):
#     # id = request.GET['id']
# 	# minsensor_1 = request.GET['minsensor_1']
# 	# maxsensor_1 = request.GET['maxsensor_1']
# 	# minsensor_2 = request.GET['minsensor_2']
# 	# maxsensor_2 = request.GET['maxsensor_2']
#     # print("id>>>>>>>>>>>>>>>>", id)   
#     # print("minsensor_1>>>>>>>",minsensor_1)
#     # print("maxsensor_1>>>>>>>",maxsensor_1)   
#     # print("minsensor_2>>>>>>>",minsensor_2)
#     # print("maxsensor_2>>>>>>>",maxsensor_2)   
#     # data = SettingTable(id=id,minsensor_1=minsensor_1,maxsensor_1=maxsensor_1,minsensor_2=minsensor_2,maxsensor_2=maxsensor_2)
# 	# data.save()
# 	# dataraw = SettingTable.objects.all().values()
#     # json_data = json.dumps(list(dataraw))
#     # return HttpResponse(json_data,content_type='application/json')