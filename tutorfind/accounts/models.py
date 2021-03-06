from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    is_tutor=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    phn_num=models.CharField(max_length=12,default="")
    locality=models.CharField(max_length=255,default="")
class Tutor(models.Model):
    tutor=models.ForeignKey(MyUser, on_delete=models.CASCADE, unique=True)
    Highest_Qual=models.CharField(max_length=255,default="")
    teach=models.CharField(max_length=255,default="")
    subjects=models.CharField(max_length=255,default="")
    travel=models.CharField(max_length=255,default="")
    mode=models.CharField(max_length=255,default="")
    state=models.CharField(max_length=255,default="")
    fees=models.IntegerField(default=0)
    gender=models.CharField(default="",max_length=12)
    slots=models.CharField(default="",max_length=255)
    experience=models.IntegerField(default=0)
    mapurl=models.URLField(max_length=200,default="")
    favourite=models.ManyToManyField(MyUser,related_name='favourite',blank=True)
    is_favourite=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    meeting=models.URLField(max_length=200,default="")
    video=models.FileField(upload_to='videos/',default="")
    def _str_(self):
        return self.name
    def get_rating(self):
        total=sum(int(review['stars']) for review in self.reviews.values())
        print(self.reviews.count())
        if(self.reviews.count()!=0):
            return total / self.reviews.count()
        else:
            return 0
    def get_count(self):
        return self.reviews.count()
class Monday(models.Model):
    monday=models.OneToOneField(Tutor, on_delete=models.CASCADE, primary_key=True)
    slot_9_10 =models.CharField(default="0",max_length=255)
    slot_10_11 =models.CharField(default="0",max_length=255)
    slot_11_12 =models.CharField(default="0",max_length=255)
    slot_12_13 =models.CharField(default="0",max_length=255)
    slot_13_14 =models.CharField(default="0",max_length=255)
    slot_14_15 =models.CharField(default="0",max_length=255)
    slot_15_16 =models.CharField(default="0",max_length=255)
    slot_16_17 =models.CharField(default="0",max_length=255)
    slot_17_18 =models.CharField(default="0",max_length=255)
    slot_18_19 =models.CharField(default="0",max_length=255)
    slot_19_20 =models.CharField(default="0",max_length=255)
class Tuesday(models.Model):
    tuesday=models.OneToOneField(Tutor, on_delete=models.CASCADE, primary_key=True)
    slot_9_10 =models.CharField(default="0",max_length=255)
    slot_10_11 =models.CharField(default="0",max_length=255)
    slot_11_12 =models.CharField(default="0",max_length=255)
    slot_12_13 =models.CharField(default="0",max_length=255)
    slot_13_14 =models.CharField(default="0",max_length=255)
    slot_14_15 =models.CharField(default="0",max_length=255)
    slot_15_16 =models.CharField(default="0",max_length=255)
    slot_16_17 =models.CharField(default="0",max_length=255)
    slot_17_18 =models.CharField(default="0",max_length=255)
    slot_18_19 =models.CharField(default="0",max_length=255)
    slot_19_20 =models.CharField(default="0",max_length=255)
class Wednesday(models.Model):
    wednesday=models.OneToOneField(Tutor, on_delete=models.CASCADE, primary_key=True)
    slot_9_10 =models.CharField(default="0",max_length=255)
    slot_10_11 =models.CharField(default="0",max_length=255)
    slot_11_12 =models.CharField(default="0",max_length=255)
    slot_12_13 =models.CharField(default="0",max_length=255)
    slot_13_14 =models.CharField(default="0",max_length=255)
    slot_14_15 =models.CharField(default="0",max_length=255)
    slot_15_16 =models.CharField(default="0",max_length=255)
    slot_16_17 =models.CharField(default="0",max_length=255)
    slot_17_18 =models.CharField(default="0",max_length=255)
    slot_18_19 =models.CharField(default="0",max_length=255)
    slot_19_20 =models.CharField(default="0",max_length=255)
class Thursday(models.Model):
    thursday=models.OneToOneField(Tutor, on_delete=models.CASCADE, primary_key=True)
    slot_9_10 =models.CharField(default="0",max_length=255)
    slot_10_11 =models.CharField(default="0",max_length=255)
    slot_11_12 =models.CharField(default="0",max_length=255)
    slot_12_13 =models.CharField(default="0",max_length=255)
    slot_13_14 =models.CharField(default="0",max_length=255)
    slot_14_15 =models.CharField(default="0",max_length=255)
    slot_15_16 =models.CharField(default="0",max_length=255)
    slot_16_17 =models.CharField(default="0",max_length=255)
    slot_17_18 =models.CharField(default="0",max_length=255)
    slot_18_19 =models.CharField(default="0",max_length=255)
    slot_19_20 =models.CharField(default="0",max_length=255)
class Friday(models.Model):
    friday=models.OneToOneField(Tutor, on_delete=models.CASCADE, primary_key=True)
    slot_9_10 =models.CharField(default="0",max_length=255)
    slot_10_11 =models.CharField(default="0",max_length=255)
    slot_11_12 =models.CharField(default="0",max_length=255)
    slot_12_13 =models.CharField(default="0",max_length=255)
    slot_13_14 =models.CharField(default="0",max_length=255)
    slot_14_15 =models.CharField(default="0",max_length=255)
    slot_15_16 =models.CharField(default="0",max_length=255)
    slot_16_17 =models.CharField(default="0",max_length=255)
    slot_17_18 =models.CharField(default="0",max_length=255)
    slot_18_19 =models.CharField(default="0",max_length=255)
    slot_19_20 =models.CharField(default="0",max_length=255)
class Saturday(models.Model):
    saturday=models.OneToOneField(Tutor, on_delete=models.CASCADE, primary_key=True)
    slot_9_10 =models.CharField(default="0",max_length=255)
    slot_10_11 =models.CharField(default="0",max_length=255)
    slot_11_12 =models.CharField(default="0",max_length=255)
    slot_12_13 =models.CharField(default="0",max_length=255)
    slot_13_14 =models.CharField(default="0",max_length=255)
    slot_14_15 =models.CharField(default="0",max_length=255)
    slot_15_16 =models.CharField(default="0",max_length=255)
    slot_16_17 =models.CharField(default="0",max_length=255)
    slot_17_18 =models.CharField(default="0",max_length=255)
    slot_18_19 =models.CharField(default="0",max_length=255)
    slot_19_20 =models.CharField(default="0",max_length=255)
class Sunday(models.Model):
    sunday=models.OneToOneField(Tutor, on_delete=models.CASCADE, primary_key=True)
    slot_9_10 =models.CharField(default="0",max_length=255)
    slot_10_11 =models.CharField(default="0",max_length=255)
    slot_11_12 =models.CharField(default="0",max_length=255)
    slot_12_13 =models.CharField(default="0",max_length=255)
    slot_13_14 =models.CharField(default="0",max_length=255)
    slot_14_15 =models.CharField(default="0",max_length=255)
    slot_15_16 =models.CharField(default="0",max_length=255)
    slot_16_17 =models.CharField(default="0",max_length=255)
    slot_17_18 =models.CharField(default="0",max_length=255)
    slot_18_19 =models.CharField(default="0",max_length=255)
    slot_19_20 =models.CharField(default="0",max_length=255)
class Orders(models.Model):
    stud_name=models.CharField(max_length=255,default="")
    tutor_name=models.CharField(max_length=255,default="")
    stud_email=models.CharField(max_length=255,default="")
    tutor_email=models.CharField(max_length=255,default="")
    stud_phn=models.CharField(max_length=255,default="")
    tutor_phn=models.CharField(max_length=255,default="")
    fee=models.IntegerField(default=0)
    day=models.CharField(max_length=255,default="")
    date=models.CharField(max_length=255,default="")
    time=models.CharField(max_length=255,default="")
    time1=models.CharField(max_length=255,default="")
    status=models.CharField(max_length=255,default="Pending")
class Review(models.Model):
    tut=models.ForeignKey(Tutor,related_name='reviews',on_delete=models.CASCADE)
    user=models.ForeignKey(MyUser,related_name='reviews',on_delete=models.CASCADE)
    title=models.CharField(max_length=200,default="")
    content=models.TextField()
    stars=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)





