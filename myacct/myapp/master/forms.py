from django.forms import ModelForm
from master.models import Classification, Purpose

############################################################################

# TODO 本当は登録と更新で共通化したい
class ClassificationForm_c(ModelForm):
    
    class Meta:
        model = Classification
        fields = (
            'id',
            'name',
        )

############################################################################

class ClassificationForm_u(ModelForm):
    
    read_only = (
        'id',
    )

    class Meta:
        model = Classification
        fields = (
            'id',
            'name',
        )

    # TODO いまいち更新時のみ変更不可がうまくいかない
    def __init__(self, *args, **kwargs):
        super(ClassificationForm_u, self).__init__(*args, **kwargs)
        for val in self.read_only:
            self.fields[val].widget.attrs['readonly'] = 'readonly'

    def clean(self):
        data = super(ClassificationForm_u, self).clean()
        for val in self.read_only:
            data[val] = getattr(self.instance, val)
        return data

############################################################################

class PurposeForm_c(ModelForm):

    class Meta:
        model = Purpose
        fields = (
            'classification',
            'sub_id',
            'name',
        )

############################################################################

class PurposeForm_u(ModelForm):

    read_only = (
        'classification',
        'sub_id',
    )

    class Meta:
        model = Purpose
        fields = (
            'classification',
            'sub_id',
            'name',
        )

    def __init__(self, *args, **kwargs):
        super(PurposeForm_u, self).__init__(*args, **kwargs)
        for val in self.read_only:
            self.fields[val].widget.attrs['readonly'] = 'readonly'

    def clean(self):
        data = super(PurposeForm_u, self).clean()
        for val in self.read_only:
            data[val] = getattr(self.instance, val)
        return data

############################################################################

'''
class TestForm(forms.ModelForm):

    class Meta:
        model = Classification
        fields = {
            'myfield': forms.CharField(widget=forms.Textarea())
        }

        meta_attrs = {
            'model': model,
        }

        form_class_attrs = {
            'Meta': type('Meta', (object, ), meta_attrs), 
        }

        form_class_attrs.update(fields)

        MyModelForm = forms.ModelFormMetaclass('MyModelForm', (forms.ModelForm, ), form_class_attrs)
'''

