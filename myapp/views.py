import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from myapp.models import *
import razorpay



def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')


def login(request):
    return render(request,'login.html')

def login_post(request):
    username = request.POST['username']
    password = request.POST['password']

    a = Login.objects.filter(username=username, password=password)
    if a.exists():
        b = Login.objects.get(username=username, password=password)
        request.session['lid'] = b.id
        if b.type == 'admin':
            return HttpResponse('''<script>alert("Login successfully ");window.location='/admin_home'</script>''')
        elif b.type == 'guide':
            return HttpResponse('''<script>alert("Login successfully ");window.location='/guide_home'</script>''')
        elif b.type == 'user':
            return HttpResponse('''<script>alert("Login successfully ");window.location='/user_home'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid ");window.location='/'</script>''')
    else:
        return HttpResponse('''<script>alert("Invalid ");window.location='/'</script>''')

def admin_home(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    return render(request,'admin/admin_home.html')

def admin_view_place(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    a=Place.objects.all()
    return render(request,'admin/view_place.html',{'data':a})

def admin_add_place(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    if 'submit' in request.POST:
        name=request.POST['name']
        place=request.POST['place']
        image=request.FILES['image']
        latitude=request.POST['latitude']
        speciality=request.POST['speciality']
        longitude=request.POST['longitude']
        description=request.POST['description']

        fs=FileSystemStorage()
        date=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.jpg'
        fs.save(date,image)
        path=fs.url(date)


        aaa=Place.objects.filter(name=name)
        if aaa.exists():
            return HttpResponse('''<script>alert("Name Already Taken ");window.location='/admin_add_place'</script>''')

        a=Place()
        a.name=name
        a.place=place
        a.image=path
        a.speciality=speciality
        a.latitude=latitude
        a.longitude=longitude
        a.description=description
        a.save()
        return HttpResponse('''<script>alert("Added ");window.location='/admin_add_place'</script>''')

    return render(request,'admin/add_place.html')


def delete_place(request,id):
    a=Place.objects.get(id=id)
    a.delete()
    return HttpResponse('''<script>alert("Deleted ");window.location='/admin_view_place'</script>''')


def admin_add_package(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    a=Place.objects.all()
    if 'submit' in request.POST:

        name=request.POST['name']
        PLACE=request.POST['PLACE']
        image=request.FILES['image']
        description=request.POST['description']
        number_days=request.POST['number_days']
        price=float(request.POST['price'])


        fs=FileSystemStorage()
        date=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.jpg'
        fs.save(date,image)
        path=fs.url(date)

        a=Package()
        a.name=name
        a.price=price
        a.PLACE=Place.objects.get(id=PLACE)
        a.image=path
        a.number_days=number_days

        a.description=description
        a.save()
        return HttpResponse('''<script>alert("Added ");window.location='/admin_add_package'</script>''')

    return render(request,'admin/add package.html',{'data':a})

def view_packages(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    items = Package.objects.all()  # Fetch all items from the model
    return render(request, 'admin/view_packages.html', {'items': items})


def delete_packages(request,id):
    a=Package.objects.get(id=id)
    a.delete()
    return HttpResponse('''<script>alert("Deleted ");window.location='/view_packages'</script>''')

def admin_add_hotel(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    a=Place.objects.all()
    if 'submit' in request.POST:

        name=request.POST['name']
        PLACE=request.POST['PLACE']
        image=request.FILES['image']
        description=request.POST['description']
        facility=request.POST['facility']
        price=float(request.POST['price'])


        fs=FileSystemStorage()
        date=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.jpg'
        fs.save(date,image)
        path=fs.url(date)

        a=Hotel()
        a.name=name
        a.price=price
        a.PLACE=Place.objects.get(id=PLACE)
        a.image=path
        a.facility=facility

        a.description=description
        a.save()
        return HttpResponse('''<script>alert("Added ");window.location='/admin_add_package'</script>''')

    return render(request,'admin/add hotel.html',{'data':a})


def view_hotel(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    items = Hotel.objects.all()  # Fetch all items from the model
    return render(request, 'admin/view_hotels.html', {'items': items})

def delete_hotel(request,id):
    a=Hotel.objects.get(id=id)
    a.delete()
    return HttpResponse('''<script>alert("Deleted ");window.location='/view_hotel'</script>''')

def view_users(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    users = User.objects.all()  # Fetch all user records
    return render(request, 'admin/view user.html', {'users': users})

def delete_user(request,id):
    aa=User.objects.get(id=id)
    aa.delete()
    aa.LOGIN.delete()
    return HttpResponse('''<script>alert("Deleted ");window.location='/view_users'</script>''')


def view_hotel_booking(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    users = Hotel_Booking.objects.all().order_by('-id')  # Fetch all user records
    return render(request, 'admin/view Bookings.html', {'users': users})


def view_package_booking(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    users = Package_Booking.objects.all().order_by('-id')  # Fetch all user records
    return render(request, 'admin/view package Bookings.html', {'users': users})



def view_complaints(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    users = Complaints.objects.all().order_by('-id')  # Fetch all user records
    return render(request, 'admin/view_complaints.html', {'users': users})


def send_reply(request,id):
    a=Complaints.objects.get(id=id)
    return render(request, 'admin/sendreply.html', {'data': a})


def sendreply_post(request):
    id=request.POST['id']
    reply=request.POST['reply']

    a=Complaints.objects.get(id=id)
    a.reply=reply
    a.save()
    return HttpResponse('''<script>alert("Replied ");window.location='/view_complaints'</script>''')




def view_feedback(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    users = Feedback.objects.all().order_by('-id')  # Fetch all user records
    return render(request, 'admin/view_feedback.html', {'users': users})



# user

def user_reg(request):
    if 'submit' in request.POST:
        name=request.POST['name']
        place=request.POST['place']
        email=request.POST['email']
        # image=request.FILES['image']
        phone=request.POST['phone']
        post=request.POST['post']
        password=request.POST['password']


        aa=Login.objects.filter(username=email)
        if aa.exists():
            return HttpResponse('''<script>alert("Already Exists ");window.location='/user_reg'</script>''')

        # fs = FileSystemStorage()
        # date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
        # fs.save(date, image)
        # path = fs.url(date)

        a=Login()
        a.username=email
        a.password=password
        a.type='user'
        a.save()


        b=User()
        b.LOGIN=a
        b.name=name
        b.phone=phone
        b.place=place
        b.post=post
        b.email=email
        b.save()
        return HttpResponse('''<script>alert("Success ");window.location='/'</script>''')
    return render(request,'user/userregister.html')


def user_home(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    return render(request,'user/userindex.html')

def user_view_profile(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    A=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'user/profile.html',{'profile':A})


def user_view_place(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    a=Place.objects.all()
    return render(request,'user/view_place.html',{'data':a})

def user_view_place_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    name=request.POST['name']
    a=Place.objects.filter(name__icontains=name)
    return render(request,'user/view_place.html',{'data':a})



def user_view_packages(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    a=Place.objects.all()
    items = Package.objects.all()  # Fetch all items from the model
    return render(request, 'user/view_packages.html', {'items': items,'data':a})
#
# def user_view_packages_post(request):
#     place=request.POST['place']
#
#     a=Place.objects.all()
#     items = Package.objects.filter(PLACE_id=place)  # Fetch all items from the model
#     return render(request, 'user/view_packages.html', {'items': items,'data':a})
#

from django.shortcuts import render
from django.db.models import Q
from .models import Package, Place

def user_view_packages_post(request):
    a = Place.objects.all()  # Fetch all places
    items = Package.objects.all()  # Start with all items

    # Get filter parameters from the request
    place_id = request.POST.get('place')
    min_price = request.POST.get('min_price')
    max_price = request.POST.get('max_price')

    # Apply filters based on the provided parameters
    if place_id:
        items = items.filter(PLACE_id=place_id)  # Filter by selected place

    # Apply price filtering only if values are provided
    if min_price:
        items = items.filter(price__gte=min_price)  # Greater than or equal to min_price
    if max_price:
        items = items.filter(price__lte=max_price)  # Less than or equal to max_price

    return render(request, 'user/view_packages.html', {'items': items, 'data': a})

def userview_hotel(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    a=Place.objects.all()

    items = Hotel.objects.all()  # Fetch all items from the model
    return render(request, 'user/view_hotels.html', {'items': items,'data':a})

# def userview_hotel_post(request):
#     place=request.POST['place']
#     place_id = request.POST.get('place')
#     min_price = request.POST.get('min_price')
#     max_price = request.POST.get('max_price')
#     # Apply filters based on the provided parameters
#     items = Hotel.objects.filter(PLACE_id=place)  # Fetch all items from the model
#
#     if place_id:
#         items = items.filter(PLACE_id=place_id)  # Filter by selected place
#
#     # Apply price filtering only if values are provided
#     if min_price:
#         items = items.filter(price__gte=min_price)  # Greater than or equal to min_price
#     if max_price:
#         items = items.filter(price__lte=max_price)  # Less than or equal to max_price
#
#     a=Place.objects.all()
#
#     return render(request, 'user/view_hotels.html', {'items': items,'data':a})





def userview_hotel_post(request):
    # Get the selected place and price range from the POST request
    place_id = request.POST.get('place')
    min_price = request.POST.get('min_price')
    max_price = request.POST.get('max_price')

    # Start with all hotels
    items = Hotel.objects.all()  # Fetch all items from the model

    # Apply place filtering if a place is selected
    if place_id:
        items = items.filter(PLACE_id=place_id)  # Filter by selected place

    # Apply price filtering only if values are provided
    if min_price:
        try:
            items = items.filter(price__gte=float(min_price))  # Greater than or equal to min_price
        except ValueError:
            pass  # Handle the case where min_price is not a valid number

    if max_price:
        try:
            items = items.filter(price__lte=float(max_price))  # Less than or equal to max_price
        except ValueError:
            pass  # Handle the case where max_price is not a valid number

    # Fetch all places for the dropdown
    a = Place.objects.all()

    # Render the response with filtered items and place data
    return render(request, 'user/view_hotels.html', {'items': items, 'data': a})






def user_book_hotel(request,id):
    a=Hotel.objects.get(id=id)
    return render(request,'user/book_hotel.html',{'data':a})


# def user_book_hotel_post(request):
#     id=request.POST['id']
#     number=float(request.POST['number'])
#
#     cc=Hotel.objects.get(id=id)
#     am=cc.price
#     total=am*number
#
#     a=Hotel_Booking()
#     a.HOTEL=cc
#     a.date=datetime.datetime.now().today().date()
#     a.USER=User.objects.get(LOGIN_id=request.session['lid'])
#     a.number_rooms=number
#     a.price=total
#     a.save()
#     return HttpResponse('''<script>alert("Booked ");window.location='/userview_hotel'</script>''')


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import datetime


def user_book_hotel_post(request):
    id = request.POST['id']
    number = float(request.POST['number'])

    # Get the hotel object
    cc = get_object_or_404(Hotel, id=id)
    am = cc.price
    total = am * number
    user = User.objects.get(LOGIN_id=request.session['lid'])

    # Check for existing booking on the same date
    existing_booking = Hotel_Booking.objects.filter(
        HOTEL=cc,
        USER=user,
        date=datetime.datetime.now().today().date()
    ).first()

    if existing_booking:
        return HttpResponse(
            '''<script>alert("You have already booked this hotel on this date.");window.location='/userview_hotel'</script>''')

    # Create a new booking since there is no existing booking
    a = Hotel_Booking()
    a.HOTEL = cc
    a.date = datetime.datetime.now().today().date()  # Store the date
    a.USER = user
    a.number_rooms = str(number)  # Convert to string if needed
    a.price = total
    a.save()

    return HttpResponse('''<script>alert("Booked successfully!");window.location='/userview_hotel'</script>''')

# def user_book_packages(request,id):
#     a=Package.objects.get(id=id)
#     return render(request,'user/book_packages.html',{'data':a})

# def user_book_packages_post(request,id):
#     a=Package.objects.get(id=id)
#     d=float(a.number_days)
#     p=float(a.price)
#     total=d*p
#
#
#     bbb=Package_Booking.objects.filter(USER__LOGIN_id=request.session['lid'],
#                                        PACKAGE_id=a,
#                                        date=datetime.datetime.now().today().date)
#
#     if bbb.exists():
#         return HttpResponse('''<script>alert("Already Book in this Date!");window.location='/user_view_packages'</script>''')
#
#     bb=Package_Booking()
#     bb.PACKAGE=Package.objects.get(id=a.id)
#     bb.USER=User.objects.get(LOGIN_id=request.session['lid'])
#     bb.date=datetime.datetime.now().today().date()
#     bb.price=total
#     bb.save()
#     return HttpResponse('''<script>alert("Booked successfully!");window.location='/user_view_packages'</script>''')

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import datetime

def user_book_packages_post(request, id):
    package = get_object_or_404(Package, id=id)
    d = float(package.number_days)
    p = float(package.price)
    # total = d * p

    user = User.objects.get(LOGIN_id=request.session['lid'])

    today_date = datetime.datetime.now().today().date()
    existing_booking = Package_Booking.objects.filter(
        USER=user,
        PACKAGE=package,
        date=today_date
    )

    if existing_booking.exists():
        return HttpResponse('''<script>alert("Already booked on this date!");window.location='/user_view_packages'</script>''')

    bb = Package_Booking()
    bb.PACKAGE = package
    bb.USER = user
    bb.date = today_date  # Store today's date
    bb.price = p
    bb.save()

    return HttpResponse('''<script>alert("Booked successfully!");window.location='/user_view_packages'</script>''')


def user_view_hotel_booking(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    users = Hotel_Booking.objects.filter(USER__LOGIN_id=request.session['lid']).order_by('-id')  # Fetch all user records
    return render(request, 'user/view hotel Bookings.html', {'users': users})

def user_view_package_booking(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    users = Package_Booking.objects.filter(USER__LOGIN_id=request.session['lid']).order_by('-id')  # Fetch all user records
    return render(request, 'user/view user package Bookings.html', {'users': users})


def send_complaint(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    if 'submit' in request.POST:
        compl=request.POST['com']
        a=Complaints()
        a.USER=User.objects.get(LOGIN_id=request.session['lid'])
        a.date = datetime.datetime.now().today().date()
        a.reply='pending'
        a.complaint=compl
        a.save()
        return HttpResponse('''<script>alert(" Sent ");window.location='/user_home'</script>''')

    return render(request,'user/send complaints.html')

def user_view_complaint(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    a=Complaints.objects.filter(USER__LOGIN_id=request.session['lid']).order_by('-id')
    return render(request,'user/view compla.html',{'data':a})


def user_send_feedback(request):
    if 'submit' in request.POST:
        rating = request.POST['rating']
        review = request.POST['review']  # Ensure this matches the form field name

        a = Feedback()
        a.USER = User.objects.get(LOGIN_id=request.session['lid'])
        a.date = datetime.datetime.now().today().date()
        a.rating = rating
        a.feedback = review
        a.save()
        return HttpResponse('''<script>alert("Feedback Sent ");window.location='/user_home'</script>''')

    return render(request, 'user/send feedback.html')



def admin_add_guide(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')


    if 'submit' in request.POST:
       name = request.POST['name']
       place = request.POST['place']
       post = request.POST['post']
       email = request.POST['email']
       phone = request.POST['phone']
       price = request.POST['price']

       e=Login.objects.filter(username=email)
       if e.exists():
           return HttpResponse('''<script>alert("Email Already Taken ");window.location='/admin_add_guide'</script>''')

       a=Login()
       a.username=email
       a.password=phone
       a.type='guide'
       a.save()

       b=Guide()
       b.LOGIN=a
       b.name=name
       b.phone=phone
       b.post=post
       b.place=place
       b.price=price
       b.email=email
       b.save()
       return HttpResponse('''<script>alert("added ");window.location='/admin_add_guide'</script>''')

    return render(request,'admin/add guide.html')

def admin_view_guide(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    a=Guide.objects.all()
    return render(request,'admin/view guide.html',{'guides':a})


def delete_guide(request,id):
    a=Guide.objects.get(id=id)
    a.delete()
    a.LOGIN.delete()
    return HttpResponse('''<script>alert("Deleted ");window.location='/admin_view_guide'</script>''')


def user_view_guide(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    a=Guide.objects.all()
    return render(request,'user/view guide.html',{'guides':a})

def user_view_guide_post(request):
    name=request.POST['name']
    a=Guide.objects.filter(name__icontains=name)
    return render(request,'user/view guide.html',{'guides':a})


def user_book_guide(request,id):
    a=Package.objects.all()
    b=Guide.objects.get(id=id)
    return render(request,'user/book_guide.html',{'data':b,'data1':a})


def user_book_guide_post(request):
    id=request.POST['id']
    package=request.POST['package']
    aa=Guide.objects.get(id=id)
    am=aa.price

    a=Guide_Booking()
    a.date= datetime.datetime.now().today().date()
    a.PACKAGE=Package.objects.get(id=package)
    a.GUIDE=aa
    a.USER=User.objects.get(LOGIN_id=request.session['lid'])
    a.status='booked'
    a.total=am
    a.save()
    return HttpResponse('''<script>alert("Booked ");window.location='/user_view_guide'</script>''')



def guide_home(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    return render(request,'guide/guideindex.html')

def giude_view_booking(request):
    a=Guide_Booking.objects.filter(GUIDE__LOGIN_id=request.session['lid']).order_by('-id')
    return render(request,'guide/view Bookings.html',{'data':a})

def guide_view_user(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logout successfully ");window.location='/'</script>''')

    a=User.objects.all()
    return render(request,'guide/view user.html',{'data':a})


def guide_chat_to_user(request, id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = User.objects.get(LOGIN=cid)
    print(qry.LOGIN_id,'login----------')

    return render(request, "guide/Chat.html", { 'name': qry.name, 'toid': cid})

def chat_view(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    try:
        qry = User.objects.get(LOGIN_id=request.session["userid"])
    except:
        qry=Guide.objects.get(LOGIN_id=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid)).order_by('id')
    l = []
    print(qry.name,'userssssssssss')

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TOID_id, "date": i.date, "from": i.FROMID_id})

    return JsonResponse({ "data": l, 'name': qry.name, 'toid': request.session["userid"]})


def chat_send(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TOID_id = toid
    chatobt.FROMID_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})


def user_chat_to_guide(request, id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = Guide.objects.get(LOGIN_id=cid)
    print(qry.LOGIN_id,'login----------')

    return render(request, "user/Chat.html", { 'name': qry.name, 'toid': cid})


def chat_view1(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = Guide.objects.get(LOGIN_id=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid)).order_by('id')
    l = []
    print(qry.name,'userssssssssss')

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TOID_id, "date": i.date, "from": i.FROMID_id})

    return JsonResponse({ "data": l, 'name': qry.name, 'toid': request.session["userid"]})

def chat_send1(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TOID_id = toid
    chatobt.FROMID_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})


def user_view_guide_booking(request):
    a=Guide_Booking.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,'user/view guide Bookings.html',{'data':a})


def user_pay_proceed(request,id,amt):
    request.session['rid'] = id


    request.session['pay_amount'] = str(amt).split(".")[0]
    client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M", "XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': request.session['pay_amount']+"00", 'currency': "INR", 'payment_capture': '1'})
    res=User.objects.get(LOGIN__id=request.session['lid'])


    ob=Hotel_Booking.objects.get(id=request.session['rid'])
    ob.status='paid'
    ob.save()
    return render(request,'user/UserPayProceed.html',{'p':payment,'val':res,"lid":request.session['lid'],"id":request.session['rid']})

def on_payment_success(request):
    request.session['rid'] = request.GET['id']
    request.session['lid'] = request.GET['lid']
    # var = auth.authenticate(username='admin', password='admin')
    # if var is not None:
    #     auth.login(request, var)
    # amt = request.session['pay_amount']
    ob=HotelPayment()
    ob.date=datetime.datetime.now().today().date()
    ob.time=datetime.datetime.now().today().time()
    ob.HOTER_BOOKING=Hotel_Booking.objects.get(id=request.session['rid'])
    ob.status='paid'
    ob.save()
    return HttpResponse('''
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@10">
                <script src="https://cdn.jsdelivr.net/npm/sweetalert2@10"></script>
                <script>
                    document.addEventListener("DOMContentLoaded", function() {
                        Swal.fire({
                            icon: 'success',
                            title: 'Order Confirmed... !',
                            confirmButtonText: 'OK',
                            reverseButtons: true
                        }).then((result) => {
                            if (result.isConfirmed) {
                                window.location = '/user_home';
                            }
                        });
                    });
                </script>
            ''')




    # return HttpResponse('''<script>alert("Success! Thank you for your Contribution");window.location="/userhome"</script>''')



def package_user_pay_proceed(request,id,amt):
    request.session['rid'] = id


    request.session['pay_amount'] = str(amt).split(".")[0]
    client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M", "XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': request.session['pay_amount']+"00", 'currency': "INR", 'payment_capture': '1'})
    res=User.objects.get(LOGIN__id=request.session['lid'])


    ob=Package_Booking.objects.get(id=request.session['rid'])
    ob.status='paid'
    ob.save()
    return render(request,'user/pakage_UserPayProceed.html',{'p':payment,'val':res,"lid":request.session['lid'],"id":request.session['rid']})


def package_on_payment_success(request):
    request.session['rid'] = request.GET['id']
    request.session['lid'] = request.GET['lid']
    # var = auth.authenticate(username='admin', password='admin')
    # if var is not None:
    #     auth.login(request, var)
    # amt = request.session['pay_amount']
    ob=PackagePayment()
    ob.date=datetime.datetime.now().today().date()
    ob.time=datetime.datetime.now().today().time()
    ob.PACKAGE_BOOKING=Package_Booking.objects.get(id=request.session['rid'])
    ob.status='paid'
    ob.save()
    return HttpResponse('''
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@10">
                <script src="https://cdn.jsdelivr.net/npm/sweetalert2@10"></script>
                <script>
                    document.addEventListener("DOMContentLoaded", function() {
                        Swal.fire({
                            icon: 'success',
                            title: 'Order Paid... !',
                            confirmButtonText: 'OK',
                            reverseButtons: true
                        }).then((result) => {
                            if (result.isConfirmed) {
                                window.location = '/user_home';
                            }
                        });
                    });
                </script>
            ''')




    # return HttpResponse('''<script>alert("Success! Thank you for your Contribution");window.location="/userhome"</script>''')



def guide_booking_user_pay_proceed(request,id,amt):
    request.session['rid'] = id


    request.session['pay_amount'] = str(amt).split(".")[0]
    client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M", "XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': request.session['pay_amount']+"00", 'currency': "INR", 'payment_capture': '1'})
    res=User.objects.get(LOGIN__id=request.session['lid'])


    ob=Guide_Booking.objects.get(id=request.session['rid'])
    ob.status='paid'
    ob.save()
    return render(request,'user/guide_payement.html',{'p':payment,'val':res,"lid":request.session['lid'],"id":request.session['rid']})

def guide_on_payment_success(request):
    request.session['rid'] = request.GET['id']
    request.session['lid'] = request.GET['lid']
    # var = auth.authenticate(username='admin', password='admin')
    # if var is not None:
    #     auth.login(request, var)
    # amt = request.session['pay_amount']
    ob=GuidePayment()
    ob.date=datetime.datetime.now().today().date()
    ob.time=datetime.datetime.now().today().time()
    ob.Guidebooking=Guide_Booking.objects.get(id=request.session['rid'])
    ob.status='paid'
    ob.save()
    return HttpResponse('''
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@10">
                <script src="https://cdn.jsdelivr.net/npm/sweetalert2@10"></script>
                <script>
                    document.addEventListener("DOMContentLoaded", function() {
                        Swal.fire({
                            icon: 'success',
                            title: 'Paid Success... !',
                            confirmButtonText: 'OK',
                            reverseButtons: true
                        }).then((result) => {
                            if (result.isConfirmed) {
                                window.location = '/user_home';
                            }
                        });
                    });
                </script>
            ''')




    # return HttpResponse('''<script>alert("Success! Thank you for your Contribution");window.location="/userhome"</script>''')
