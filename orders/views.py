from django.shortcuts import render, redirect
from .models import Order, Line
from .forms import OrderForm
from .formsLine import OrderLine
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    orders = Order.objects.all()
    return render(request, 'index.html', {'orders': orders})

@login_required
def indexline(request):
    lines = Line.objects.all()
    return render(request, 'indexline.html', {'lines': lines})

@login_required
def show(request, order_id):
    order = Order.objects.filter(id=order_id)
    return render(request, 'show.html', {'order': order})

def showLine(request, line_id):
    line = Line.objects.filter(id=order_id)
    return render(request, 'showline.html', {'line': line})

@login_required
def new(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Order was successfully created.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm()
        return render(request, 'new.html', {'form':form})

@login_required
def newLine(request):
    if request.POST:
        line = OrderLine(request.POST)
        if line.is_valid():
            if line.save():
                return redirect('/order/indexline', messages.success(request, 'New Line was successfully created.', 'alert-success'))
            else:
                return redirect('/order/indexline', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/order/indexline', messages.error(request, 'Line is not valid', 'alert-danger'))
    else:
        line = OrderLine()
        return render(request, 'newline.html', {'line':line})

@login_required
def edit(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.POST:
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Order was successfully updated.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm(instance=order)
        return render(request, 'edit.html', {'form':form})

@login_required
def editLine(request, line_id):
    line = Line.objects.get(id=line_id)
    if request.POST:
        line = OrderLine(request.POST, instance=line)
        if line.is_valid():
            if line.save():
                return redirect('/order/indexline', messages.success(request, 'New Line was successfully updated.', 'alert-success'))
            else:
                return redirect('/order/indexline', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/order/indexline', messages.error(request, 'Line is not valid', 'alert-danger'))
    else:
        line = OrderLine(instance=line)
        return render(request, 'editline.html', {'line':line})

@login_required
def destroy(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('/', messages.success(request, 'Order was successfully deleted.', 'alert-success'))

@login_required
def destroyLine(request, line_id):
    line = Line.objects.get(id=line_id)
    line.delete()
    return redirect('/order/indexline', messages.success(request, 'Line was successfully deleted.', 'alert-success'))
