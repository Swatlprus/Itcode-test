from django import forms

import core.models

class CompanySearch(forms.Form):
#     FOUNDER_CHOICES =(
#     ("1", "One"),
#     ("2", "Two"),
#     ("3", "Three"),
#     ("4", "Four"),
#     ("5", "Five"),
# )

    # founder = forms.ChoiceField(choices=FOUNDER_CHOICES)
    name = forms.CharField(label='Название', required=False)
    min_rating = forms.IntegerField(label='Рейтинг компании', required=False, help_text='Минимальный рейтинг компании')

    def clean_min_rating(self):
        min_rating = self.cleaned_data['min_rating']

        if min_rating and min_rating > 10000:
            raise forms.ValidationError('Рейтинг компании не может быть выше 10 000')

        return min_rating

class CompanyEdit(forms.ModelForm):

    class Meta:
        model = core.models.Company
        fields = '__all__'
