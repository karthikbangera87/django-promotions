
import uuid
#from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect

from .forms import EmailForm,myappmodelforms
from .models import myapp
# Create your views here.

def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip

def get_ref_id():
	reference_id = str(uuid.uuid4())[:11].upper()
	try:
		exists = myapp.objects.get(ref_id = reference_id)
		get_ref_id()
	except:
		return reference_id

def share(request,reference_id):

	context = {'ref_id':reference_id}
	template = "share.html"
	return render(request,template,context)


def home(request):

	# form = EmailForm(request.POST or None)
	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	new_join,created = myapp.objects.get_or_create(email = email)

	# 	print new_join,created
	# 	print new_join.timestamp

	# 	if created:
	# 		print "A new object has been created"

	form = myappmodelforms(request.POST or None)
	if form.is_valid():
		#new_join = form.save(commit=False)
		#we might do something here
		email = form.cleaned_data['email']
		new_join_old, created = myapp.objects.get_or_create(email=email)
		if created:
			new_join_old.ref_id = get_ref_id()
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
		return HttpResponseRedirect("/%s" %(new_join_old.ref_id))

	context = {"form":form}
	template = "test.html"
	return render(request,template,context)


