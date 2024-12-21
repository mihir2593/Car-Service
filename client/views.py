from io import BytesIO

from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render, redirect
from storesapp.models import productmodel
from client import models
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from storesapp.models import storemodel
from client import forms
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from reportlab.pdfgen import canvas

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from storesapp.views import storeindex


# Create your views here.
def clientindex(request):
    if request.user.is_authenticated:
        return render(request, 'client/index.html')
    else:
        return redirect(clientlogin)


def clientservice(request):
    if request.user.is_authenticated:
        return render(request, 'client/service.html')
    else:
        return redirect(clientlogin)


def clientcontact(request):
    if request.user.is_authenticated:
        return render(request, 'client/contact.html')
    else:
        return redirect(clientlogin)


def clientabout(request):
    if request.user.is_authenticated:
        return render(request, 'client/about.html')
    else:
        return redirect(clientlogin)


def clientregister(request):
    if request.method == "POST":
        if request.POST.get('password') == request.POST.get('password1'):
            try:
                User.objects.get(username=request.POST.get('username'))
                return HttpResponse("user is already exists")
            except:
                user = User.objects.create_user(username=request.POST.get('username'),
                                                email=request.POST.get('email'),
                                                password=request.POST.get('password'),
                                                is_staff=True,
                                                )
                detail = models.userdetail.objects.create(user=user,
                                                          address=request.POST.get('address'),
                                                          phone=request.POST.get('phone'),
                                                          )
                return redirect(clientlogin)
        else:
            return HttpResponse("enter valid password")

    return render(request, 'client/register.html')


def clientlogin(request):
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
    return render(request, 'client/login.html')


def clientlogout(request):
    logout(request)
    return redirect(clientlogin)


def storeproduct(request):
    if request.user.is_authenticated:
        data = productmodel.objects.filter(isavailable=True)
        paginator = Paginator(data, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        abc = {
            'data': page_obj,
        }
        return render(request, 'client/product.html', abc)
    else:
        return redirect(clientlogin)


#
#
# cart detail

def cart_add(request, id):
    if request.user.is_authenticated:
        cart = Cart(request)
        product = productmodel.objects.get(id=id)
        cart.add(product=product)
        return redirect("cl-product")
    else:
        return redirect(clientlogin)


def item_clear(request, id):
    if request.user.is_authenticated:
        cart = Cart(request)
        product = productmodel.objects.get(id=id)
        cart.remove(product)
        return redirect("cart_detail")
    else:
        return redirect(clientlogin)


def item_increment(request, id):
    if request.user.is_authenticated:
        cart = Cart(request)
        product = productmodel.objects.get(id=id)
        cart.add(product=product)
        return redirect("cart_detail")
    else:
        return redirect(clientlogin)


def item_decrement(request, id):
    if request.user.is_authenticated:
        cart = Cart(request)
        product = productmodel.objects.get(id=id)
        cart.decrement(product=product)
        return redirect("cart_detail")
    else:
        return redirect(clientlogin)


def cart_clear(request):
    if request.user.is_authenticated:

        cart = Cart(request)
        cart.clear()
        return redirect("cart_detail")
    else:
        return redirect(clientlogin)


def cart_detail(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        x = cart.cart.values()
        y = list(x)
        print(y)
        total = 0
        prod_ids = [item['product_id'] for item in y]
        print(prod_ids)
        for ab in cart.cart.values():
            subtotal = float(ab['price']) * float(ab['quantity'])
            total += subtotal
            print(subtotal)

            productname = ab['name']
            Quantity = ab['quantity']

        print(total)
        gst = total * 0.09
        final_total = gst + total
        xyz = productmodel.objects.filter(isavailable=False).aggregate(total=Sum('price'))['total']

        context = {
            'final_total': final_total,
            'gst': gst,
            'total': total,

        }

        return render(request, 'client/cart.html', context=context)
    else:
        return redirect(clientlogin)


def storelist(request):
    if request.user.is_authenticated:
        data = storemodel.objects.filter(isavailable=True)
        context = {'data': data}
        return render(request, 'client/storelist.html', context=context)
    else:
        return redirect(clientlogin)


def requestservice(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = forms.servicerequest(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                store = storemodel.objects.get(id=id)
                obj.service = store
                obj.user = request.user
                obj.save()
                return redirect(clientindex)
            else:
                print(form.errors)
        return render(request, 'client/service_request.html')
    else:
        return redirect(clientlogin)


def myservices(request):
    if request.user.is_authenticated:
        myservice = models.servicerequest.objects.all()
        context = {'myservice': myservice}
        return render(request, 'client/myservices.html', context=context)
    else:
        return redirect(clientlogin)


def myprofile(request):
    if request.user.is_authenticated:
        myprofile = models.userdetail.objects.filter(user=request.user)
        context = {'myprofile': myprofile}
        return render(request, 'client/client_details.html', context=context)
    else:
        return redirect(clientlogin)


def confirmorder(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        x = cart.cart.values()
        y = list(x)
        print(y)
        total = 0
        prod_ids = [item['product_id'] for item in y]
        print(prod_ids)

        fnl = models.FinalOrder.objects.create(user=request.user, gst=0, total=0, finaltotal=0)

        for xy in cart.cart.values():
            Productid = xy['product_id']
            print(Productid)

            subtotal = float(xy['price']) * float(xy['quantity'])
            total += subtotal
            print(subtotal)
            print(total)

            Quantity = xy['quantity']
            print(Quantity)

            order = models.confirmorder.objects.create(user=request.user, final=fnl, price=subtotal, quantity=Quantity,
                                                       product_id=Productid)
            print("order", order)
        fnl.total = total
        pro_gst = total * 0.09
        fnl.gst = pro_gst
        fnl.finaltotal = total + pro_gst
        fnl.save()

        cart.clear()
        return render(request, 'client/confirmorder.html')
    else:
        return redirect(clientlogin)


def myorder(request):
    if request.user.is_authenticated:
        data = models.FinalOrder.objects.filter(user=request.user)
        context = {'data': data}
        return render(request, 'client/myorder.html', context=context)
    else:
        return redirect(clientlogin)


def add_to_wishlist(request, id):
    wished = productmodel.objects.filter(is_wished=True)
    return redirect(wishlist)


def wishlist(request):
    if request.user.is_authenticated:
        wisheditem = productmodel.objects.all()
        wisheditem.is_wished = 'True'
        context = {'wisheditem': wisheditem}
        return render(request, 'client/wishlist.html', context=context)
    else:
        return redirect(clientlogin)


def remmovewishlist(request):
    if request.user.is_authenticated:
        remove = productmodel.objects.filter()
        remove.is_wished = 'False'
        context = {'wisheditem': remove}
        return render(request, 'client/wishlist.html', context=context)
    else:
        return redirect(clientlogin)


def productinvoice(request, id):
    userdetail = models.userdetail.objects.get(user=request.user)
    abc = models.FinalOrder.objects.get(id=id)
    print(abc)
    data = models.confirmorder.objects.filter(final_id=id)
    print(data)
    xyz = productmodel.objects.all()
    context = {'data': data,
               'userdetail': userdetail,
               'abc': abc,
               'xyz' : xyz,

               }

    return render(request, 'client/product_invoice.html', context=context)


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def download_invoice_pdf(request, order_id):
    # Fetch your order and user details based on order_id
    # For example:
    order = get_object_or_404(confirmorder, pk=order_id)
    user = order.user
    userdetail = user.profile
    print(order_id)

    context = {
        'abc': order,
        'user': user,
        'userdetail': userdetail,
        'data': order.items.all(),
    }

    pdf = render_to_pdf('invoice_template.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = f"Invoice_{order_id}.pdf"
        content = f"attachment; filename={filename}"
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Error generating PDF", status=400)