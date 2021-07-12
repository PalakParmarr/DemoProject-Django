from django.core.checks import messages
from FormDemoApp.models import FormModel
from django.contrib import messages
from django.shortcuts import redirect, render
from FormDemoApp.forms import MyForm
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def mainform(request):
    if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            name = myForm.cleaned_data['name']
            email = myForm.cleaned_data['email']
            feedback = myForm.cleaned_data['feedback']
            if FormModel.objects.filter(name=name).exists():
                messages.info(request,'already exists')
                return redirect('/')
            else:
                m=FormModel(name=name, email=email, feedback=feedback)
                m.save()
            context = {
            'name': name,
            'email': email,
            'feedback': feedback
            }

            template = loader.get_template('rform.html')
           
            return HttpResponse(template.render(context, request))
    else:
        form = MyForm()


    return render(request,'mainform.html',{'form':form})