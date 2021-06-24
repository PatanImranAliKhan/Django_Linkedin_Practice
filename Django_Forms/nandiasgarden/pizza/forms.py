from django import forms
from .models import Pizza

# class PizzaForm(forms.Form):
#     topping1=forms.CharField(label='Topping 1', max_length=100,widget=forms.PasswordInput)
#     topping2=forms.CharField(label='Tooping 2',max_length=100)
#     # toppings=forms.MultipleChoiceField(choices=[('pep','Pepporoni'),('cheese','Cheese'),('olives','Olives')],widget=forms.CheckboxSelectMultiple)
#     size=forms.ChoiceField(label='Size', choices=[('Small','small'),('Medium','medium'),('Large','large')])

class PizzaForm(forms.ModelForm):
    
    class Meta:
        model=Pizza
        fields=['topping1','topping2','size']
        labels={'topping1':'Topping 1','topping2':'Topping 2'}

class MultiplePizzaForm(forms.Form):
    number=forms.IntegerField(min_value=1,max_value=6)