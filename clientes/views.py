from django.shortcuts import render, redirect, get_object_or_404
from .models import Cars
from .forms import Car_form
from django.contrib.auth.decorators import login_required


@login_required
def car_list(request):
    context = {
        'cars': Cars.objects.all()
    }
    return render(request, 'list.html', context)


@login_required
def car_create(request):
    form = Car_form(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('car_list')
    return render(request, 'car_save.html', {'form': form})


@login_required
def car_update(request, id):
    car = get_object_or_404(Cars, pk=id)
    form = Car_form(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('car_list')
    return render(request, 'car_save.html', {'form': form})


@login_required
def car_delete(request, id):
    car = get_object_or_404(Cars, pk=id)
    form = Car_form(request.POST or None, instance=car)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'car_delete.html', {'form': form})
