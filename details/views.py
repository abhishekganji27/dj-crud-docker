from django.shortcuts import render, redirect
from .models import *
from django.forms import ModelForm
# Create your views here.


class RegisterForm(ModelForm):
    class Meta:
        model = Details
        fields = '__all__'

# def register(request):
    # form = RegisterForm()
    # if request.method == 'POST':
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
            # return redirect('home')
    # return render(request, 'register.html', {'form': form})

def home_page(request):
    form = RegisterForm()
    records = Details.objects.all().order_by('id')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'home.html', {'form': form, 'records': records})

def delete_record(request, pk):
    record_to_delete = Details.objects.get(id=pk)
    record_to_delete.delete()
    return redirect('home')

def update_record(request, pk):
    record_to_update = Details.objects.get(id=pk)
    # form = None 
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=record_to_update)
        if form.is_valid():
            form.save()
            return redirect('home')
    # else:
    #     form = RegisterForm(record_to_update)
    return render(request, 'update.html', {'record': record_to_update})

def search_record(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        search_results = Details.objects.filter(name__contains=search_query)
        return render(request, 'search_result.html',
                       {'search_query': search_query, 
                        'search_results': search_results })
