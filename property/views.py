from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .models import Property, Category
from .forms import ReserveForm 
from django.db.models import Q
def property_list(request):
    property_list = Property.objects.all()
    template = 'list.html'

    address_query = request.GET.get('q')
    property_type = request.GET.getlist('property_type' , None)
    if address_query and property_type : 
        print(address_query)
        print(property_type)
        property_list = property_list.filter(
            Q(name__icontains = address_query) &
            Q(property_type__icontains=property_type[0])
        ).distinct()
        
    print(property_list)

    context = {
        'property_list' : property_list
    }
    return render(request , template , context)



def property_detail(request, id):
	property_detail= Property.objects.get(id=id)

	if request.method == 'POST':
		reserve_form= ReserveForm(request.POST)
		if reserve_form.is_valid():
			reserve_form.save()

	else:
		reserve_form= ReserveForm()

	return render(request, 'detail.html',{'reserve_form': reserve_form,'property_detail': property_detail})







def signup(request):
	if request.method== "POST":
		username= request.POST["username"]
		password= request.POST["password"]
		email= request.POST["email"]

		user = User.objects.create_user(
			username=username,
			password=password,
			email= email
			)
		login(request, user)
		return redirect('')
	return render(request,"signup.html")

def signin(request):
	if request.method== "POST":
		username= request.POST["username"]
		password= request.POST["password"]

		user= authenticate(request, username=username,
		 password= password)
		if user != None:
			login(request, user)
			return redirect('')

	return render(request,"signin.html")

def signout(request):
	
	logout(request)

	return redirect("/signin/")
