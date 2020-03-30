from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import HttpResponse
from django.views.generic import TemplateView, RedirectView, ListView
import sys, os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Information, MyClass, User
from .forms import InformationForm, UserForm, RegisterClassForm
from django.views.decorators.http import require_POST, require_GET
from django.conf import settings
from .module import index 
from django.urls import reverse
from urllib.parse import urlencode



def delete(request):
    class_name = request.session['class_name']
    delete_id = request.POST.getlist('delete_id')
    if delete_id:
        deleted_imgs = Information.objects.filter(id__in=delete_id)
        for deleted_img in deleted_imgs:
            if deleted_img.picture.name:
                os.remove(settings.MEDIA_ROOT + "/" + deleted_img.picture.name)
            
        Information.objects.filter(id__in=delete_id).delete()
    return redirect('app:information')

def table(request):
    if not 'user_id' in request.session: return redirect('/auth/login')
    if 'class_name' in request.session: 
        del request.session['class_name']
    context = { 
        'classlists':index.user_object(request)
    }
    return render(request, "index/table.html", context)

def register_class(request):
    if not 'user_id' in request.session: return redirect('/auth/login')
    RegisterClassData = RegisterClassForm()
    context = {
        'form': RegisterClassData,
    }
    return render(request, 'index/register_class.html', context)

def create_class(request):
    if not 'user_id' in request.session: return redirect('/auth/login')
    RegisterClassData = RegisterClassForm(request.POST or None)
    # バリデーションチェック
    if RegisterClassData.is_valid():
        Data = RegisterClassData.cleaned_data
        url = index.CreateMyClass(request, Data)
        if not url:
            RegisterClassData = RegisterClassForm()
            data = {
                'form': RegisterClassData,
                'error': 'この授業はすでに登録されているなり',
            }
            return render(request, 'index/register_class.html', data)
    else :
        url = '/register_class'

    return redirect(url)

def change_class(request):
    if not 'user_id' in request.session: return redirect('/auth/login')
    context = {    
        'classlists':index.user_object(request),
        'allclasses': MyClass.objects.all(),
    }
    return render(request, 'index/change_class.html', context)

@csrf_exempt
def save_change_class(request):
    if not 'user_id' in request.session: return redirect('/auth/login')
    url = index.SaveChange(request)
    return redirect(url)


"""
ModelFormから生成されたクラス、つまり今回では「QuestionPostForm」にはsaveメソッドがあります。
このsaveメソッドは「commit」という引数を指定することができます。
commit引数はTrueまたはFalseをとります。
「save(commit = False)」のようにFalseにすると、データベースに保存する前にモデルインスタンス、つまり今回ではQuestionPostFormクラスのMetaクラスに指定したモデルクラス「Question」を返します。
この機能を使い、保存前に何らかの処理を行い、最終的にsaveメソッドを呼び出せばデータベースに保存されます。
"""

def information_of_class(request):
    if not 'user_id' in request.session: return redirect('/auth/login')
    if request.method == 'POST':
        request.session['class_name'] = request.POST.get('class_name')
    class_name = request.session['class_name']   
    myclass = MyClass.objects.get(name=class_name)
    informations = Information.objects.filter(my_class=myclass)
    context = {
        'informations': informations,
        'class_name': request.session['class_name']   
    }
    
    return render(request, "index/information.html", context)


def upload(request):
    class_name = request.session['class_name']
    if request.method == "POST":
        myclass = MyClass.objects.get(name=class_name)
        form = InformationForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit = False)
            question.my_class = myclass
            question.save()
            redirect_url = reverse('app:information')
            parameters = urlencode({'class_name': class_name})
            url = f'{redirect_url}?{parameters}'
            return redirect(url)
    else:
        form = InformationForm()
    context = {
        'form':form,
        'class_name':class_name    
    }
    return render(request, 'index/upload.html', context)
