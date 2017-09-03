from django.shortcuts import render

def test(request):
    return render(request, "index.html", locals())

# Create your views here.
