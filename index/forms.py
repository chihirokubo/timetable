from django import forms
from .models import Information, User, MyClass

DAYS = (
    (None, ''),
    ('monday', '月曜日'),
    ('tuesday', '火曜日'),
    ('wednesday', '水曜日'),
    ('thursday', '木曜日'),
    ('friday', '金曜日'),
)

PERIODS = (
    (None, ''),
    ('1', '1時間目'),
    ('2', '2時間目'),
    ('3', '3時間目'),
    ('4', '4時間目'),
    ('5', '5時間目'),
)



class InformationForm(forms.Form):
    title = forms.CharField(
        label = 'タイトル',
        max_length = 50,
        required = True,
        widget = forms.TextInput,
    )
    pictures = forms.ImageField(
        label = '画像',
        required = False,
        widget = forms.ClearableFileInput(attrs={'multiple': True}),
    )
    comment = forms.CharField(
        label = 'コメント',
        required = False,
        widget = forms.Textarea(attrs={'cols': 20, 'rows': 7}),
    )
    def get_pictures(self):
        pictures_list = []
        for i in range(5):
            try:
                picture_object = self.files.getlist('pictures')
                pictures_list.append(picture_object[i])
            except:
                pictures_list.append(None)
        return pictures_list



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

        
class RegisterClassForm(forms.Form):
    name = forms.CharField(
        label = '授業名',
        max_length = 50,
        required = True,
        widget = forms.TextInput(attrs={'class':'form-control'}),
    )
    day = forms.ChoiceField(
        label = '曜日',
        choices = DAYS,
        required = False,
        widget=forms.widgets.Select(attrs={'class':'form-control'}),
    )
    period = forms.ChoiceField(
        label = '時間',
        choices = PERIODS,
        required = False,
        widget=forms.widgets.Select(attrs={'class':'form-control'}),
    )
    place = forms.CharField(
        label = '教室',
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'class':'form-control'}),
    )