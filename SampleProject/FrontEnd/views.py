from django.shortcuts import render,redirect
from SampleApp.models import categorydb,Productdb3
from FrontEnd.models import contactusdb,registerdb,cartdb

# Create your views here.

def homepage(req):
    cat = categorydb.objects.all()
    return render(req,"Homepage.html",{'cat':cat})

def product_page(req):
    pro = Productdb3.objects.all()
    return render(req,"Products.html",{'pro':pro})

def single_product(request,proid):
    data = Productdb3.objects.get(id=proid)
    return render(request,"Single_Product.html",{'data':data})

def filtered_product(request,cat_name):
    data = Productdb3.objects.filter(Select_Product=cat_name)
    return render(request,"Filtered_Product_Page.html",{'data':data})

def aboutus(request):
    return render(request,"About_Us.html")

def services(request):
    return render(request,"Services.html")

def contactus(request):
    return render(request,"Contact_Us.html")

def contactdata(request):
    if request.method == "POST":
        cn = request.POST.get('name')
        ce = request.POST.get('email')
        cc = request.POST.get('city')
        ca = request.POST.get('address')
        obj = contactusdb(C_Name=cn,C_Email=ce,C_City=cc,C_Address=ca)
        obj.save()
        return redirect(contactus)

def registerpage(request):
    return render(request,"Register.html")


def registerdata(request):
    if request.method == "POST":
        rn = request.POST.get('name')
        rm = request.POST.get('number')
        re = request.POST.get('email')
        ra = request.POST.get('address')
        ru = request.POST.get('username')
        rp = request.POST.get('password')
        obj = registerdb(R_Name=rn,R_Mobile=rm,R_Email=re,R_Address=ra,R_Username=ru,R_Password=rp)
        obj.save()
        return redirect(registerpage)

def userlogin(request):
    if request.method=="POST":
        un=request.POST.get("username")
        pwd=request.POST.get("password")
        if registerdb.objects.filter(R_Username=un,R_Password=pwd).exists():
            request.session["R_Username"]=un
            request.session["R_Password"]=pwd
            return redirect(homepage)
        else:
            return redirect(registerpage)

    return redirect(registerpage)

def userlogout(request):
    del request.session["R_Username"]
    del request.session["R_Password"]
    return redirect(registerpage)

def cartpage(request):
    data = cartdb.objects.filter(User_name=request.session['R_Username'])
    total_price = 0
    for i in data:
        total_price = total_price+i.Total_Price
    return render(request,"Add_To_Cart.html",{'data':data,'total_price':total_price})

def cartdata(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        pn = request.POST.get('product_name')
        des = request.POST.get('description')
        qty = request.POST.get('quantity')
        tpri = request.POST.get('total')
        obj = cartdb(User_name=un,Product_name=pn,Description=des,Quantity=qty,Total_Price=tpri)
        obj.save()
        return redirect(cartpage)


def cart_delete(request,pro_id):
    pro = cartdb.objects.filter(id=pro_id)
    pro.delete()
    return redirect(cartpage)

def checkoutpage(request):
    return render(request,"Checkout.html")

def summarypage(request):
    return render(request,"Summary.html")