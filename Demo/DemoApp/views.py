
from django.shortcuts import render
from DemoApp.models import Contact
from django.contrib import messages
# Create your views here.'
def index(request):
    context={
        'variable':'PALAK'
    }
    return render(request,'index.html',context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')