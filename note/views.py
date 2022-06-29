from django.shortcuts import render, redirect  
from note.forms import NoteForm  
from note.models import Note 

# Create your views here.
def no(request):  
    if request.method == "POST":  
        form = NoteForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = NoteForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    notes = Note.objects.all()  
    return render(request,'show.html',{'notes':notes})  
def edit(request, id):  
    note = Note.objects.get(id=id)  
    return render(request,'edit.html', {'note':note})  
def update(request, id):  
    note = Note.objects.get(id=id)  
    form = NoteForm(request.POST, instance = note)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'note': note})  
def destroy(request, id):  
    note = Note.objects.get(id=id)  
    note.delete()  
    return redirect("/show")