from django import forms
from .models import Information, User, MyClass

DAYS = (
    ('monday', '月曜日'),
    ('tuesday', '火曜日'),
    ('wednesday', '水曜日'),
    ('thursday', '木曜日'),
    ('friday', '金曜日'),
)

PERIODS = (
    ('1', '1時間目'),
    ('2', '2時間目'),
    ('3', '3時間目'),
    ('4', '4時間目'),
    ('5', '5時間目'),
)


class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['title','picture', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

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