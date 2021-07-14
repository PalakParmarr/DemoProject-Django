from django.shortcuts import render, redirect
from uploadfileapp.models import Document
from uploadfileapp.forms import DocumentForm


def index(request):
    return render(request, 'index.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/list/')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })


def list(request):
    documents = Document.objects.all()
    return render(request, 'list.html', {'documents': documents})
