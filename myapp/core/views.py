from django.shortcuts import redirect, render, HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse('<h1>Home Page</h1>')
    return render(request, 'home.html')


def error_404(request, exception):
    print("no se encuentra 404")
    # return render(request, 'blog.html')
    return redirect('/')
