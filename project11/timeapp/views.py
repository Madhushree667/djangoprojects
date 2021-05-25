from django.shortcuts import render
from datetime import datetime

def display_time(request):
	date=datetime.now()
	hour=int(datetime.now().hour)
	msg='hello students good'
	if hour>0 and hour<12:
		msg=msg+'morning'
	elif hour>12 and hour<16:
		msg=msg+'afternoon'
	elif hour>16 and hour<21:
		msg=msg+'evening'
	else:
		msg=msg+'night'
	msg=msg
	my_dict={'date':date,'msg':msg}
	return render(request=request,template_name='timeapp/time.html',context=my_dict)


# Create your views here.
