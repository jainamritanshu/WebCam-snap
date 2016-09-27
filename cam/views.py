from django.shortcuts import render
from .models import *
from selenium import webdriver
import urllib
import time
from django.views.decorators.csrf import csrf_exempt

def list_cam(request):
	camera = Camera.objects.all()

	context = {'camera': camera}
	return render(request, 'cam/index.html', context)

@csrf_exempt
def cam_click(request):

	c_id = request.POST.get('id')
	print c_id
	cam = Camera.objects.get(pk = c_id)
	driver = webdriver.Firefox()
	x=0
	while x<10:
		driver.get(cam.link)
		driver.save_screenshot(str(cam.university_name) + str(time.time()))
		time.sleep(10)
		x+=1

	driver.quit()

	context = {'cam': cam}
	return render(request, 'cam/downloading.html', context)

	# urllib.urlretrieve("http://portalweb.bucknell.edu/stuaptcam/readImage.asp", img_file_name1)
