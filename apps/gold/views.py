from django.shortcuts import render, redirect, HttpResponse
import random
import datetime

def index(request):
    # if 'gold' not in request.session:
    #     request.session['gold'] = 0
    # if 'earnings' not in request.session:
    #     request.session['earnings'] = 0
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities'] = []

    return render(request, "gold/index.html")

def process_money(request):

    if request.method == 'POST':
        if 'log' not in request.session:
            request.session['log'] = []

        if request.POST['building'] == 'farm':
            request.session['earnings'] = random.randrange(10,21)
            request.session['gold'] += request.session['earnings']
            request.session['time'] = str(datetime.datetime.utcnow())
            request.session['log'] += "You earned " + str(request.session['earnings']) + " gold pieces from the " + str(request.POST['building']) + "! " + str(request.session['time']) + "\n"

        if request.POST['building'] == 'cave':
            request.session['earnings'] = random.randrange(5,10)
            request.session['gold'] += request.session['earnings']
            request.session['time'] = str(datetime.datetime.utcnow())
            request.session['log'] += "You earned " + str(request.session['earnings']) + " gold pieces from the " + str(request.POST['building']) + "! " + str(request.session['time']) + "\n"

        if request.POST['building'] == 'house':
            request.session['earnings'] = random.randrange(2,5)
            request.session['gold'] += request.session['earnings']
            request.session['time'] = str(datetime.datetime.utcnow())
            request.session['log'] += "You earned " + str(request.session['earnings']) + " gold pieces from the " + str(request.POST['building']) + "! " + str(request.session['time']) + "\n"

        if request.POST['building'] == 'casino':
            request.session['earnings'] = random.randrange(-50,50)
            request.session['gold'] += request.session['earnings']
            request.session['time'] = str(datetime.datetime.utcnow())
            if request.session['earnings'] > 0:
                request.session['log'] += "You earned " + str(request.session['earnings']) + " gold pieces from the " + str(request.POST['building']) + "! " + str(request.session['time']) + "\n"
            else:
                request.session['log'] += "You lost " + str(request.session['earnings']) + " gold pieces from the " + str(request.POST['building']) + "! " + str(request.session['time']) + "\n"


        # now = datetime.datetime.now()
        # building = request.POST['building']
        # buildings = {
        #     'farm': random.randint(10,21),
        #     'house': random.randint(2,5),
        #     'cave': random.randint(5,10),
        #     'casino': random.randint(-50,50)
        # }
        # if building in buildings:
        #     gold = buildings[building]
        #     request.session['gold'] += gold
        #
        # formatted_datetime = format.date_format(now, "SHORT_DATETIME_FORMAT")
        #
        # if gold < 0:
        #     color = 'lost'
        #     activity = "Sorry, you lost {} from the {}!! {}".format(abs(gold), building.upper(), formatted_datetime)
        # else:
        #     color = 'win'
        #     activity = "Yay, went to the {} and won {} gold! {}".format(abs(gold), building.upper(), formatted_datetime)
        #
        # activity = {'class': color, 'activity': activity}
        #
        # request.session['activities'].append(activity)
        # request.session.modified = True

    return redirect("gold:index")

def reset(request):
    request.session['gold'] = 0
    # request.session['building'] = "building"
    request.session['log'] = ""
    request.session['log2'] = ""
    request.session['time'] = ""
    return redirect('gold:index')
