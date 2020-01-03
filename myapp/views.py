from django.shortcuts import render, HttpResponse, Http404, redirect
from django.contrib import messages
from myapp.models import Teams, Team_players, Stadium, Schedule_Match,Seats,Payment,Bank
from accounts.models import Accounts
from datetime import datetime as dt , timezone
import json as js
import random
# Create your views here.
def home(request):
    return render(request,"home.html",{})
def teams(request):
    team = Teams.objects.all()
    return render(request,"teams.html",{'teams': team})    
def teamhome(request,team):
    players = Team_players.objects.filter(team_name=team)
    return render(request, "team_home.html",{"players":players})
def match_list(request):
    try:
        match_schedule = Schedule_Match.objects.all()        
    except Exception as e:
        raise Http404("Page does not exist")
    return render(request, 'match_list.html', {'match_schedule': match_schedule})
def ticketbook(request,id):
    match_book = Schedule_Match.objects.get(id=id)
    return render(request, "ticketbook.html", {'match_book':match_book})

def seat_query(request):
    if request.method == "GET":
        match_id = request.GET.get('match')
        bay = request.GET.get('bay')
        match_book = Schedule_Match.objects.get(pk=match_id)
        try:
            with open('static/arrange.json','r') as file:
                seat_arrange = js.load(file)
        except:
            raise Http404("Json Error")
        Seats.delete_temp_allocated()
        occ_seats = Seats.objects.filter(match=match_book)
        occ_seats = [x.seats[1:] for x in occ_seats if x.seats[0]==bay]
        #for x in occ_seats:
        #    print(x)
        return render(request,'Seat_arrange.html',{"data":seat_arrange, 'match_book':match_book,'bay': bay, "unavilable_seats": occ_seats})
    else:
        selected_seats = request.POST['selected_seats']
        selected_seats = selected_seats.split(',')
        request.session['selected_seats'] = selected_seats
        match_id = request.POST['match_id']
        match_book = Schedule_Match.objects.get(pk=match_id)
        email_id = request.session['email_id']
        account = Accounts.objects.get(email_id=email_id)
        bay = request.POST['bay']
        level_count = [x[0] for x in selected_seats] 
        scount = set(level_count)
        a = {}
        for x in scount:
            a[x]=level_count.count(x)
        price = a.get('1',0)*250+a.get('2',0)*450+a.get('3',0)*550
        gst = 0.09*price
        total = price + gst + gst
        pay = [price,gst,total]
        return render(request,'payment.html',{'selected_seats':selected_seats,'match_book':match_book,'account':account,'bay':bay,'pay':pay})

def check_seat(request):
    if request.method == "GET":
        match_id = request.GET.get('match_id')
        seat_id = request.GET.get('seat_id')
        seat = Seats.objects.filter(match=match_id, seats =seat_id)
        if len(seat) == 0:
            s = Seats()
            s.user = Accounts.objects.get(email_id=request.session['email_id'])
            s.match = Schedule_Match.objects.get(pk=match_id)
            s.seats = seat_id
            s.temp_allocated = "True"
            s.save()
            return HttpResponse("true")
        else:
            s = seat[0]
            if s.temp_allocated == "True":
                time = dt.now(timezone.utc) - s.booked_date
                if time.seconds > (10*60):
                    s.user = Accounts.objects.get(email_id=request.session['email_id'])
                    s.temp_allocated = "True"
                    s.save()
                    return HttpResponse("true")
                else:
                    return HttpResponse("false")
            else:
                return HttpResponse("false")
def payment(request):
    if request.method == "POST":
        from_t = request.POST['card_no']
        name = request.POST['name']
        exp_month = request.POST['exp_month']
        exp_year = request.POST['exp_year']
        cvv = request.POST['cvv']
        amount = request.POST['amount']
        selected_seats = request.session['selected_seats']
        result = Bank.transfer('3300330033003333',from_t,cvv,name,exp_month,exp_year,amount)
        user = Accounts.objects.get(email_id=request.session['email_id'])
        match_id = request.POST['match_id']
        match = Schedule_Match.objects.get(pk=match_id)
        bay = request.POST['bay']
        booked_seats = ""
        for s in selected_seats:
            seat = Seats.objects.filter(user=user,match=match,seats=(bay+s))
            booked_seats += bay+s + ', '
            if len(seat)==1:
                seat[0].temp_allocated=False
                seat[0].save()
        pay = Payment()
        pay.user = user
        pay.seats = booked_seats[:-2]
        print(pay.seats)
        pay.price = amount
        pay.match = match
        pay.save()
        del request.session['selected_seats']
        messages.info(request, f'Your tickets are booked successfully!')
    return redirect(home)
def booked_tickets(request):
    if request.method=="GET":
        email_id = request.session['email_id']
        user = Accounts.objects.get(email_id=email_id)
        pay = Payment.objects.filter(user=user)
        booked_chairs = {}
        for p in pay:
            b = p.seats
            booked_chairs[p.pk]=b.split(', ')
        return render(request,'booked_tickets.html',{'pay':pay,'booked_chairs':booked_chairs})

