from django.shortcuts import render

# Create your views here.
def index(request):
    # next_page = request.GET['next']
    context = {
        'next':'abc'
    }
    return render(request,'dashboard/base.html',context)