from django.shortcuts import render
from django.http import *
from .models import *

# Create your views here.
def home(req):
	return render(req,'myapp/home.html')
def register(req):
	if req.method == 'POST':
		username = req.POST['name']
		usermail = req.POST['mail']
		userpwd = req.POST['pass']
		useraddr = req.POST['addr']
		userdob = req.POST['dob']
		usergen = req.POST['gender']
		obj = Register(Name = username,Email=usermail,Password=userpwd,Address=useraddr,DOB=userdob,Gender=usergen)
		obj.save()
		return render(req,'myapp/home.html')

	return render(req,'myapp/register.html')

def login(req):
	if req.method =='POST':
		umail = req.POST['mail']
		upwd = req.POST['pass']
		data = Register.objects.all()
		

		l=[]
		k=[]
		for i in data:
			l.append(i.Email)
			k.append(i.Password)

		if umail in l and upwd in k:
			obj1 = Register.objects.get(Email=umail)
			return render(req,'myapp/details.html',{'data':obj1})
			return HttpResponse("Valid User")

		elif umail in l and upwd not in k:
			return HttpResponse("Wrong Password Please Try Again !")

		else:
			return HttpResponse("Invalid User, You need to Register First !")

	return render(req,'myapp/login.html')

def edit(req,num):
	obj = Register.objects.get(Email=num)

	if req.method=='POST':
		obj.Name = req.POST['name']
		obj.Email = req.POST['mail']
		obj.Password = req.POST['pass']
		obj.Address = req.POST['addr']
		obj.DOB = req.POST['dob']
		obj.Gender = req.POST['gender']
		obj.save()
		return render(req,'myapp/details.html',{'data':obj})
	return render(req,'myapp/update.html',{'data':obj})

def show(request):
	data = Register.objects.all()
	return render(request,'myapp/data.html',{'data':data})

def seek(req):
	if req.method=='POST':
		uphone = req.POST['phone']
		uitem = req.POST['item']
		uquan = req.POST['quan']
		obj = Seeking(Phone=uphone,Item=uitem,Quantity=uquan)
		obj.save()
		return HttpResponse("Your Requirements are recorded !")
	return render(req,'myapp/seek.html')

def help(req):
	if req.method == 'POST':
		up = req.POST['phone']
		ut = req.POST['item']
		uq = req.POST['quan']
		obj = Helping(Hphone=up,Hitem=ut,Hquantity=uq)
		obj.save()
		k = Seeking.objects.get(Phone=up)
		k.Quantity = str(abs(int(uq)-int(k.Quantity)))
		k.save()

		obj = Seeking.objects.all()
		return render(req,'myapp/help.html',{'data':obj})
		

		#for i in range(len(obj2)):

		return HttpResponse("Donated Something")
	obj = Seeking.objects.all()
	return render(req,'myapp/help.html',{'data':obj})