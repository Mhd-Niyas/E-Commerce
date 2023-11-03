from django.shortcuts import render,redirect
from SampleApp.models import categorydb,Productdb3
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from FrontEnd.models import contactusdb
from django.contrib import messages

# Create your views here.
def indexpage(req):
    return render(req,"index.html")

def categorypage(req):
    return render(req,"AddCategory.html")

def catdata(req):
    if req.method == "POST":
        cn = req.POST.get('catname')
        cd = req.POST.get('description')
        ci = req.FILES['image']
        obj = categorydb(CatName=cn,CatDes=cd,CatImg=ci)
        obj.save()
        messages.success(req,"Category Saved Successfully")
        return redirect(categorypage)

def catdisplay(req):
    data = categorydb.objects.all()
    return render(req,"DisplayCategory.html",{'data':data})

def editcat(req,editid):
    edit = categorydb.objects.get(id=editid)
    return render(req,"EditCategory.html",{'edit':edit})

def updatecat(req,updateid):
    if req.method == "POST":
        catn = req.POST.get('catname')
        catd = req.POST.get('description')
    try:
        im = req.FILES['image']
        fs = FileSystemStorage()
        file = fs.save(im.name, im)
    except MultiValueDictKeyError:
        file = categorydb.objects.get(id=updateid).CatImg
        categorydb.objects.filter(id=updateid).update(CatName=catn,CatDes=catd,CatImg=file)
        messages.success(req,"Category Updated Succesfully")
        return redirect(catdisplay)

def deletecat(req,deleid):
    dele = categorydb.objects.filter(id=deleid)
    dele.delete()
    messages.error(req,"Category Deleted Succesfully")
    return redirect(catdisplay)

def addproduct(req):
    cat = categorydb.objects.all()
    return render(req,"AddProduct.html",{'cat':cat})

def productdata(req):
    if req.method == "POST":
        sp = req.POST.get('select')
        pn = req.POST.get('pname')
        des = req.POST.get('description')
        pri = req.POST.get('price')
        img = req.FILES['image']
        obj = Productdb3(Select_Product=sp,Product_Name=pn,Description=des,Price=pri,Image=img)
        obj.save()
        return redirect(addproduct)

def display_product(req):
    data = Productdb3.objects.all()
    return render(req,"DsiplayProduct.html",{'data':data})

def edit_product(req,editid):
    edit = Productdb3.objects.get(id=editid)
    cat = categorydb.objects.all()
    return render(req,"EditProduct.html",{'edit':edit,'cat':cat})

def update_product(req,updateid):
    if req.method == "POST":
        spr = req.POST.get('select')
        pna = req.POST.get('pname')
        desc = req.POST.get('description')
        pric = req.POST.get('price')
    try:
        im = req.FILES['image']
        fs = FileSystemStorage()
        file = fs.save(im.name, im)
    except MultiValueDictKeyError:
        file = Productdb3.objects.get(id=updateid).Image
    Productdb3.objects.filter(id=updateid).update(Select_Product=spr,Product_Name=pna,Description=desc,Price=pric,Image=file)
    return redirect(display_product)

def delete_product(req,deleid):
    dele = Productdb3.objects.filter(id=deleid)
    dele.delete()
    return redirect(display_product)

def admin_login(request):
    return render(request,"AdminLogin.html")

def adminlogin(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        ps = request.POST.get('pass_word')

        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=ps)
            if user is not None:
                login(request,user)
                request.session['username']=un
                request.session['password']=ps
                return redirect(indexpage)
            else:
                return redirect(admin_login)
        else:
            return redirect(admin_login)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)

def contact_display(request):
    data = contactusdb.objects.all()
    return render(request,"Display_Contact.html",{'data':data})