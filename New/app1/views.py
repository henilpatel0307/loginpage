from django.shortcuts import render

# Create your views here.
def NewData(request):
    if request.POST:
        a1 = request.POST['val1']
        a2 = request.POST['val2']
        rec = int(a1) + int(a2)
        
        print(a1,a2)
        
        print(rec)
        return render(request,'hello.html',{'ans':rec})
    return render(request,'hello.html')

def Index(request):
    return render(request,'index.html')

def About_us(request):
    return render(request,'about.html')

def Blog(request):
    return render(request,'blog.html')

def Contact_us(request):
    return render(request,'contact.html')

