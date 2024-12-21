from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from storesapp import models
from storesapp import forms

from client.models import confirmorder , servicerequest



# Create your views here.
def storeindex(request):
    if request.user.is_authenticated:
        return render(request, 'stores/index.html')
    else:
        return redirect(storelogin)


def storeregister(request):
    if request.method == "POST":
        if request.POST.get('password') == request.POST.get('password1'):
            try:
                User.objects.get(username=request.POST.get('username'))
                return HttpResponse("user is already exist")
            except:
                user = User.objects.create_user(username=request.POST.get('username'),
                                                email=request.POST.get('email'),
                                                password=request.POST.get('password'),
                                                is_superuser=True,
                                                )
                return redirect(storelogin)
        else:
            return HttpResponse("Enter Valid Password")
    return render(request, 'stores/store-register.html')


def storelogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_superuser == True:
            login(request, user)
            return redirect(storeindex)
        elif user is not None and user.is_staff == True:
            login(request, user)
            return redirect(clientindex)
        else:
            return HttpResponse("User is not found ")
    return render(request, 'stores/store-login.html')

def storelogout(request):
    logout(request)
    return redirect(storelogin)

# product data
def addproduct(request):
    if request.user.is_authenticated:
        addcate = models.categorymodel.objects.all()
        addusecate = models.usecategorymodel.objects.all()
        context = {'addcate': addcate, 'addusecate': addusecate}

        if request.method == "POST":
            form = forms.productform(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save()
                obj.isavailable = True
                obj.save()
                return redirect(manageproduct)
            else:
                print(form.errors)
        return render(request, 'stores/add-product.html', context=context)
    else:
        return redirect(storelogin)


def manageproduct(request):
    if request.user.is_authenticated:
        product = models.productmodel.objects.all()
        context = {'product': product}
        return render(request, 'stores/manage-product.html', context=context)
    else:
        return redirect(storelogin)

def deleteproduct(request, id):
    if request.user.is_authenticated:
        product = models.productmodel.objects.get(id=id)
        product.delete()
        return redirect(manageproduct)
    else:
        return redirect(storelogin)

def editproduct(request, id):
    if request.user.is_authenticated:
        addcate = models.categorymodel.objects.all()
        addusecate = models.usecategorymodel.objects.all()


        product = models.productmodel.objects.get(id=id)
        context = {'addcate': addcate, 'addusecate': addusecate, 'product': product}
        return render(request, 'stores/product_edit.html', context=context)
    else:
        return redirect(storelogin)

def updateproduct(request, id):
    if request.user.is_authenticated:
        product = models.productmodel.objects.get(id=id)
        if request.method == "POST":
            form = forms.productform(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                return redirect(manageproduct)
            else:
                print(form.errors)
                return redirect(manageproduct)

        return render(request, 'stores/product_edit.html')
    else:
        return redirect(storelogin)
# category data
def addcategory(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = forms.categoryform(request.POST)
            if form.is_valid():
                obj = form.save()
                obj.save()
                return redirect(managecategory)
            else:
                print(form.errors)

        return render(request, 'stores/category.html')
    else:
        return redirect(storelogin)

def managecategory(request):
    if request.user.is_authenticated:
        data = models.categorymodel.objects.all()
        context = {'data': data}
        return render(request, 'stores/managecategory.html', context=context)
    else:
        return redirect(storelogin)

def deletecategory(request,id):
    if request.user.is_authenticated:
        category = models.categorymodel.objects.get(id=id)
        category.delete()
        return redirect(managecategory)
    else:
        return redirect(storelogin)

def editcategory(request, id):
    if request.user.is_authenticated:
        category = models.categorymodel.objects.get(id=id)
        context = {'category': category}
        return render(request, 'stores/category_edit.html', context=context)
    else:
        return redirect(storelogin)

def updatecategory(request, id):
    if request.user.is_authenticated:
        category = models.categorymodel.objects.get(id=id)
        if request.method == "POST":
            form = forms.categoryform(request.POST, request.FILES, instance=category)
            if form.is_valid():
                form.save()
                return redirect(managecategory)
            else:
                print(form.errors)
                return redirect(managecategory)
        return render(request, 'stores/category_edit.html')
    else:
        return redirect(storelogin)
# usecategory data

def addusecategory(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = forms.usecategoryform(request.POST)
            if form.is_valid():
                obj = form.save()
                obj.save()
                return redirect(manageusecate)
            else:
                print(form.errors)
        return render(request, 'stores/usecategory.html')
    else:
        return redirect(storelogin)

def manageusecate(request):
    if request.user.is_authenticated:
        data = models.usecategorymodel.objects.all()
        context = {'data': data}
        return render(request, 'stores/manage-usecategory.html', context=context)
    else:
        return redirect(storelogin)

def deleteusecate(request,id):
    if request.user.is_authenticated:
        usecategory = models.usecategorymodel.objects.get(id=id)
        usecategory.delete()
        return redirect(managecategory)
    else:
        return redirect(storelogin)

def editusecate(request, id):
    if request.user.is_authenticated:

        usecate = models.usecategorymodel.objects.get(id=id)
        context = {'usecate': usecate}
        return render(request, 'stores/usecate_edit.html', context=context)
    else:
        return redirect(storelogin)

def updateusecate(request, id):
    if request.user.is_authenticated:
        usecate = models.usecategorymodel.objects.get(id=id)
        if request.method == "POST":
            form = forms.usecategoryform(request.POST, request.FILES, instance=usecate)
            if form.is_valid():
                form.save()
                return redirect(manageusecate)
            else:
                print(form.errors)
                return redirect(manageusecate)

        return render(request, 'stores/usecate_edit.html')
    else:
        return redirect(storelogin)

def createinvoice(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = forms.invoiceform(request.POST)
            if form.is_valid():
                obj = form.save()
                obj.save()
                return redirect(manageinvoice)
            else:
                print(form.errors)
        return render(request, 'stores/create_invoice.html')
    else:
        return redirect(storelogin)


def manageinvoice(request):
    if request.user.is_authenticated:
        invoice = models.invoicemodel.object.all()
        context = {'invoice': invoice}
        return render(request, 'stores/manage-invoice.html', context=context)
    else:
        return redirect(storelogin)

def service(request):
    if request.user.is_authenticated:
        return render(request, 'stores/service.html')
    else:
        return redirect(storelogin)


def contact(request):
    if request.user.is_authenticated:
        return render(request, 'stores/contact.html')
    else:
        return redirect(storelogin)

def about(request):
    if request.user.is_authenticated:
        return render(request, 'stores/about.html')
    else:
        return redirect(storelogin)


# --------------For Services--------------------

def addstore(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.storeform(request.POST,request.FILES)
            if form.is_valid():
                obj = form.save()
                obj.save()
                return redirect (managestore)
            else:
                print(form.errors)
        return render(request,'stores/add-service.html')
    else:
        return redirect(storelogin)
def managestore(request):
    if request.user.is_authenticated:
        service = models.storemodel.objects.all()
        context = {'service' : service }
        return render(request,'stores/manage-service.html',context=context)
    else:
        return redirect(storelogin)
def deletestore(request,id):
    if request.user.is_authenticated:
        service = models.storemodel.objects.get(id=id)
        service.delete()
        return redirect(managestore)
    else:
        return redirect(storelogin)
def editstore(request,id):
    if request.user.is_authenticated:
        service = models.storemodel.objects.get(id=id)
        context = {'service' : service}
        return render(request,'stores/service_edit.html',context=context)
    else:
        return redirect(storelogin)
def updatestore(request,id):
    if request.user.is_authenticated:
        service = models.storemodel.objects.get(id=id)
        if request.method == "POST":
            form = forms.storeform(request.POST, instance=service)
            if form.is_valid():
                form.save()
                return redirect(managestore)
            else:
                print(form.errors)
                return redirect(managestore)
        return render(request,'stores/service_edit.html')
    else:
        return redirect(storelogin)
def manageservicerequest(request):
    if request.user.is_authenticated:
        servicereq = servicerequest.objects.all()
        context = {'servicereq' : servicereq}
        return render(request,'stores/manage_servicerequest.html',context=context)
    else:
        return redirect(storelogin)

def allorderlist(request):
    if request.user.is_authenticated:
        data = confirmorder.objects.all()
        context = {'data': data}
        return render(request, 'stores/orderlist.html', context=context)
    else:
        return redirect(storelogin)


def acceptservice(request,id):
    service = servicerequest.objects.get(id=id)
    service.status = "accepted"
    service.save()
    return redirect(manageservicerequest)


def rejectservice(request,id):
    service = servicerequest.objects.get(id=id)
    service.status = "Take a New Date"
    service.save()
    return redirect(manageservicerequest)





