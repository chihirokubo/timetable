from django.db import models
import uuid

class MyClass(models.Model):
    day = models.CharField(max_length=10, null=True, blank=True)
    period = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=50, null=False)
    place = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name



def user_portfolio_directory_path(instance, filename):
    return 'image-{0}/{1}'.format(instance.id, filename)

class Information(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    picture1 = models.ImageField(upload_to=user_portfolio_directory_path, null=True, blank=True)
    picture2 = models.ImageField(upload_to=user_portfolio_directory_path, null=True, blank=True)
    picture3 = models.ImageField(upload_to=user_portfolio_directory_path, null=True, blank=True)
    picture4 = models.ImageField(upload_to=user_portfolio_directory_path, null=True, blank=True)
    picture5 = models.ImageField(upload_to=user_portfolio_directory_path, null=True, blank=True)
    comment = models.CharField(max_length=255, null=True, blank=True)
    my_class = models.ForeignKey(MyClass, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255)
    last_login = models.DateTimeField(null=True, blank=True)
    monday_1 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="mon1") 
    monday_2 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="mon2")
    monday_3 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="mon3")
    monday_4 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="mon4")
    monday_5 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="mon5")
    tuesday_1 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="tue1") 
    tuesday_2 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="tue2")
    tuesday_3 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="tue3")
    tuesday_4 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="tue4")
    tuesday_5 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="tue5")
    wednesday_1 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="wed1") 
    wednesday_2 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="wed2")
    wednesday_3 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="wed3")
    wednesday_4 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="wed4")
    wednesday_5 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="wed5")
    thursday_1 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="thu1") 
    thursday_2 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="thu2")
    thursday_3 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="thu3")
    thursday_4 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="thu4")
    thursday_5 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="thu5")
    friday_1 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="fri1") 
    friday_2 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="fri2")
    friday_3 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="fri3")
    friday_4 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="fri4")
    friday_5 = models.ForeignKey(MyClass, on_delete=models.SET_NULL, null=True, related_name="fri5")

    def __str__(self):
        return self.name
