from django import forms
from .models import Pizza, Size


# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100)

#*********************** Working with widget in  : note :: forms only ***************************************
#     topping1 = forms.CharField(label='Topping 1', max_length=100,widget=forms.PasswordInput)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size',choices=[('small','Small'),('medium','Medium'),('Large','large')])

# ********************Creating a form using model***********************************

# class PizzaForm(forms.ModelForm):
#     # We have to provide some information here and these are meta information
#     class Meta:
#          model = Pizza
#          fields = ['topping1','topping2','size']
#          labels ={'topping1':'First Topping','topping2':'Second Topping'}
#
# ********************************** Using widget in modelform ************************

class PizzaForm(forms.ModelForm):

    size = forms.ModelChoiceField(queryset=Size.objects,empty_label=None,widget=forms.RadioSelect)
    # We have to provide some information here and these are meta information
    class Meta:
         model = Pizza
         fields = ['topping1','topping2','size']
         labels ={'topping1':'First Topping','topping2':'Second Topping'}

         # To overcome this problem
         # Goto line 24
         # widgets = {'size':forms.CheckboxSelectMultiple}



# Greatest features of form is here
#  ***************** Files uploading *************************************

class PizzaForm(forms.ModelForm):

    # image = forms.ImageField()
    # We have to provide some information here and these are meta information
    class Meta:
         model = Pizza
         fields = ['topping1','topping2','size']
         labels ={'topping1':'First Topping','topping2':'Second Topping'}

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2,max_value=6)