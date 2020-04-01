from ..models import User, Information, MyClass
from django.urls import reverse
from urllib.parse import urlencode

Period = ['1', '2', '3', '4', '5']
Day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']


def user_object(request):
    user_id = request.session['user_id']
    user = User.objects.filter(id=user_id).first()
    
    class_list = []
        
    for period in Period:
        day_list = []
        for day in Day:
            day_and_period = day + '_' + period
            value = getattr(user, day_and_period)
            day_list.append(value)
        class_list.append(day_list)
    return class_list
    """
    return user
    """


def CreateMyClass(request, Data):
    if MyClass.objects.filter(name = Data['name']):
        url = ''
    else :
        MyClassData = MyClass(
            name = Data['name'],
            day = Data['day'],
            period = Data['period'],
            place = Data['place'],
        )
        MyClassData.save()
        if Data['day'] and Data['period']:
            user_id = request.session['user_id']
            user = User.objects.get(id=user_id)
            day_and_period = Data['day'] + '_' + Data['period']
            setattr(user, day_and_period, MyClassData)
            user.save()

        url = '/'

    return url

def SaveChange(request):
    for i in range(5):
        for j in range(5):
            i_j = str(j+1) + "_" + str(i+1)
            if request.POST.get(i_j):
                d_p = Day[j] + "_" + Period[i]
                name_of_class = request.POST.get(i_j)
                data = MyClass.objects.get(name=name_of_class) if name_of_class != "null" else None
                user_id = request.session['user_id']
                user = User.objects.get(id=user_id)
                setattr(user, d_p, data)
                user.save()
                return '/change_class'
    print(request.POST.get(i_j))
    return '/'

def show_information(request, class_name):
    myclass = MyClass.objects.get(name=class_name)
    informations = Information.objects.filter(my_class=myclass)
    return informations

def upload_func(formdata, myclass):
    pictures_list = formdata.get_pictures()
    formdata = formdata.cleaned_data
    InformationData = Information(
        title = formdata['title'],
        comment = formdata['comment'],
        my_class = myclass,
        picture1 = pictures_list[0],
        picture2 = pictures_list[1],
        picture3 = pictures_list[2],
        picture4 = pictures_list[3],
        picture5 = pictures_list[4],
    )
    InformationData.save()
    redirect_url = reverse('app:information')
    parameters = urlencode({'class_name': myclass.name})
    url = f'{redirect_url}?{parameters}'

    return url

def trace_user(request, user_traced_name):
    user_id = request.session["user_id"]
    user = User.objects.get(id=user_id)
    user_traced = User.objects.get(name=user_traced_name)
    for period in Period:
        day_list = []
        for day in Day:
            day_and_period = day + '_' + period
            value = getattr(user_traced, day_and_period)
            setattr(user, day_and_period, value)
    user.save()
    return "/"