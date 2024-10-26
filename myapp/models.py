from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)





class Guide(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    # type = models.CharField(max_length=100)

class User(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    post = models.CharField(max_length=100)


class Place(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Package(models.Model):
    name = models.CharField(max_length=100)
    PLACE = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    number_days = models.CharField(max_length=100)

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    PLACE = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    facility = models.CharField(max_length=100)



class Hotel_Booking(models.Model):
    HOTEL = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    price = models.FloatField()
    number_rooms = models.CharField(max_length=100)

class Package_Booking(models.Model):
    PACKAGE = models.ForeignKey(Package, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    price = models.FloatField()


class Guide_Booking(models.Model):
    PACKAGE = models.ForeignKey(Package, on_delete=models.CASCADE)
    GUIDE = models.ForeignKey(Guide, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    total = models.CharField(max_length=100)


class Feedback(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

class Complaints(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    date = models.CharField(max_length=100)



class Chat(models.Model):
    FROMID= models.ForeignKey(Login,on_delete=models.CASCADE,related_name="Fromid")
    TOID= models.ForeignKey(Login,on_delete=models.CASCADE,related_name="Toid")
    message=models.CharField(max_length=100)
    date=models.DateField()


class HotelPayment(models.Model):
    HOTER_BOOKING= models.ForeignKey(Hotel_Booking,on_delete=models.CASCADE)
    time=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    status=models.CharField(max_length=100)


class PackagePayment(models.Model):
    PACKAGE_BOOKING= models.ForeignKey(Package_Booking,on_delete=models.CASCADE)
    time=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    status=models.CharField(max_length=100)



class GuidePayment(models.Model):
    Guidebooking= models.ForeignKey(Guide_Booking,on_delete=models.CASCADE)
    time=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    status=models.CharField(max_length=100)