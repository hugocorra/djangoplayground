from django.forms import ModelForm, inlineformset_factory
from myapp_01 import models


class A(ModelForm):
    class Meta:
        model = models.A
        fields = '__all__'


class B(ModelForm):
    class Meta:
        model = models.B
        fields = '__all__'


class C(ModelForm):
    class Meta:
        model = models.C
        fields = '__all__'


# BFormSet = inlineformset_factory(A, B, fields=('field_mb',))
# CFormSet = inlineformset_factory(A, C, fields=('field_mc',))
