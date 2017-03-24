from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'survey/index.html')

def process(request):
    if request.method == "POST":
        request.session['data'] = {
        "Name": request.POST['name'],
        "Location": request.POST['location'],
        "Language": request.POST['language'],
        "Comments": request.POST['comments']
        }
        try:
            request.session['count'] += 1
        except Exception as e:
            request.session['count'] = 1
        return redirect('survey:result')

def result(request):
    return render(request, 'survey/result.html')
