from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.forms import formset_factory

from .models import Pizza
from .forms import PizzaForm, MultiplePizzaForm
from .decorators import allowed_users,unauthenticated_user



def index(request):
    return render(request, 'pizza_template/index.html')



class ListPizza(ListView):
    queryset = Pizza.objects.all()
    template_name = 'pizza_template/view_pizza.html'

@login_required
def order(request):
    mpizza = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = 'Thanks for ordering'
            new_form = PizzaForm()
            return render(request, 'pizza_template/order.html',
                          {'pizzaform': new_form, 'note': note, 'multiple_form': mpizza})
    else:

        form = PizzaForm()
        return render(request, 'pizza_template/order.html', {'pizzaform': form, 'multiple_form': mpizza})


def pizzas(request):
    number_of_pizza = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizza = filled_multiple_pizza_form.cleaned_data['number']
    # class
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizza)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_form_set = PizzaFormSet(request.POST)
        if filled_multiple_pizza_form.is_valid():
            for form in filled_form_set:
                print(form.cleaned_data['topping1'])
            note = 'pizzas have been ordered'
        else:
            note = 'Ordered was not created'
        return render(request, 'pizza_template/pizzas.html', {'note': note, 'formset': formset})

    else:
        return render(request, 'pizza_template/pizzas.html', {'formset': formset})


def edit_order(request, id):
    pizza = Pizza.objects.get(id=id)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
    return render(request, 'pizza_template/edit.html', {'pizza': pizza})

@allowed_users(allowed=['Staff'])
def rules(request):
    return render(request, 'account/company.html')
