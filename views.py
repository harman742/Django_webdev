from django.shortcuts import render




def home(request):
    # return HttpResponse("hello world home")
    return render(request,'index.html')

def login_view(request):
    return render(request,'loginwow.html')


# def contact(request):
#     return HttpResponse("hello world contact")