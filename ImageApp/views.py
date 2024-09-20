from django.shortcuts import render,redirect, get_object_or_404
from .forms import ImageForm
from.models import Image
# Create your views here.
#Home View
def Home(request):
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        
    form=ImageForm()
    img=Image.objects.all()
    return render(request,'myapp/home.html',{'img':img,'form':form})


# Delete Image
def DeleteView(request,pk):
    img=get_object_or_404(Image, id=pk)
    img.delete()
    return redirect('home')


#Update Image

def UpdateView(request,pk):
    img=get_object_or_404(Image, id=pk)
    form=ImageForm(instance=img)
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES,instance=img)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'myapp/update.html',{'form':form})