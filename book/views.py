from django.shortcuts import render
from . import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from web.models import Bus
from .models import Seat, Booking, Ticket
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
@csrf_protect
def book_bus(request):
    request.session["active"] = 1
    request.session.set_expiry(600)

    form1 = forms.FormBookBus(prefix="form1")
    form2 = forms.FormBookBus(prefix="form2")
    form3 = forms.FormBookBus(prefix="form3")
    form4 = forms.FormBookBus(prefix="form4")
    form5 = forms.FormBookBus(prefix="form5")
    form6 = forms.FormBookBus(prefix="form6")
    template = 'error.html'
    context = {}

    if 'seat_selected' in request.POST and request.user.is_authenticated() and "active" in request.session:
        seat_selected = request.POST['seat_selected']

        if seat_selected:

            seat_total = request.POST['seat_total']
            seat_selected = seat_selected.split(",")
            number = len(seat_selected)


            if number < 7 and "bus_number" in request.session:
                bs = request.session["bus_number"]
                seat_id = []
                for label in seat_selected:
                    total_seats = Seat.objects.get(bus__bus_number=bs, seat_label=label)
                    seat_id.append(total_seats.id)

                    total_seats.status = 'unavailable'
                    total_seats.save()

                request.session["seat_id"] = seat_id
                sseat = 0
                tseat = 0
                fseat = 0
                fiseat = 0

                if number == 3:
                    sseat = seat_selected[1]
                elif number == 4:
                    sseat = seat_selected[1]
                    tseat = seat_selected[2]
                elif number == 5:
                    sseat = seat_selected[1]
                    tseat = seat_selected[2]
                    fseat = seat_selected[3]
                elif number == 6:
                    sseat = seat_selected[1]
                    tseat = seat_selected[2]
                    fseat = seat_selected[3]
                    fiseat = seat_selected[4]

                template = 'book.html'
                context = {'seat_selected': seat_selected, 'number': number, 'seats': seat_selected[0], 'seatsrest': seat_selected[1:], 'sseat': sseat, 'lseat': seat_selected[-1], 'tseat': tseat, 'fseat': fseat, 'fiseat': fiseat, 'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,}

    return render(request, template, context)

@require_http_methods(["POST"])
@csrf_protect
def payment(request):
    template = "error.html"
    context = {}

    if "seat_id" in request.session and request.user.is_authenticated() and "active" in request.session:

        seat_id = request.session["seat_id"]
        book_id = []

        if len(seat_id) == 1:
            name1 = request.POST.get("form1-name")
            gender1 = request.POST.get("form1-gender")
            age1 = request.POST.get("form1-age")
            phone1 = request.POST.get("form1-phone")
            user = request.user
            seat1 = seat_id[0]

            book1 = Booking(user=user, name=name1, gender=gender1, age=age1, phone=phone1, seat_id=seat1)
            book1.save()
            book_id.append(book1.id)

        elif len(seat_id) == 2:
            name1 = request.POST.get("form1-name")
            name2 = request.POST.get("form2-name")
            gender1 = request.POST.get("form1-gender")
            gender2 = request.POST.get("form2-gender")
            age1 = request.POST.get("form1-age")
            age2 = request.POST.get("form2-age")
            phone1 = request.POST.get("form1-phone")
            phone2 = request.POST.get("form2-phone")
            user = request.user
            seat1 = seat_id[0]
            seat2 = seat_id[1]

            book1 = Booking(user=user, name=name1, gender=gender1, age=age1, phone=phone1, seat_id=seat1)
            book1.save()
            book_id.append(book1.id)

            book2 = Booking(user=user, name=name2, gender=gender2, age=age2, phone=phone2, seat_id=seat2)
            book2.save()
            book_id.append(book2.id)


        elif len(seat_id) == 3:
            name1 = request.POST.get("form1-name")
            name2 = request.POST.get("form2-name")
            name3 = request.POST.get("form3-name")
            gender1 = request.POST.get("form1-gender")
            gender2 = request.POST.get("form2-gender")
            gender3 = request.POST.get("form3-gender")
            age1 = request.POST.get("form1-age")
            age2 = request.POST.get("form2-age")
            age3 = request.POST.get("form3-age")
            phone1 = request.POST.get("form1-phone")
            phone2 = request.POST.get("form2-phone")
            phone3 = request.POST.get("form3-phone")
            user = request.user
            seat1 = seat_id[0]
            seat2 = seat_id[1]
            seat3 = seat_id[2]

            book1 = Booking(user=user, name=name1, gender=gender1, age=age1, phone=phone1, seat_id=seat1)
            book1.save()
            book_id.append(book1.id)

            book2 = Booking(user=user, name=name2, gender=gender2, age=age2, phone=phone2, seat_id=seat2)
            book2.save()
            book_id.append(book2.id)

            book3 = Booking(user=user, name=name3, gender=gender3, age=age3, phone=phone3, seat_id=seat3)
            book3.save()
            book_id.append(book3.id)

        elif len(seat_id) == 4:
            name1 = request.POST.get("form1-name")
            name2 = request.POST.get("form2-name")
            name3 = request.POST.get("form3-name")
            name4 = request.POST.get("form4-name")
            gender1 = request.POST.get("form1-gender")
            gender2 = request.POST.get("form2-gender")
            gender3 = request.POST.get("form3-gender")
            gender4 = request.POST.get("form4-gender")
            age1 = request.POST.get("form1-age")
            age2 = request.POST.get("form2-age")
            age3 = request.POST.get("form3-age")
            age4 = request.POST.get("form4-age")
            phone1 = request.POST.get("form1-phone")
            phone2 = request.POST.get("form2-phone")
            phone3 = request.POST.get("form3-phone")
            phone4 = request.POST.get("form4-phone")
            user = request.user
            seat1 = seat_id[0]
            seat2 = seat_id[1]
            seat3 = seat_id[2]
            seat4 = seat_id[3]

            book1 = Booking(user=user, name=name1, gender=gender1, age=age1, phone=phone1, seat_id=seat1)
            book1.save()
            book_id.append(book1.id)

            book2 = Booking(user=user, name=name2, gender=gender2, age=age2, phone=phone2, seat_id=seat2)
            book2.save()
            book_id.append(book2.id)

            book3 = Booking(user=user, name=name3, gender=gender3, age=age3, phone=phone3, seat_id=seat3)
            book3.save()
            book_id.append(book3.id)

            book4 = Booking(user=user, name=name4, gender=gender4, age=age4, phone=phone4, seat_id=seat4)
            book4.save()
            book_id.append(book4.id)

        elif len(seat_id) == 5:
            name1 = request.POST.get("form1-name")
            name2 = request.POST.get("form2-name")
            name3 = request.POST.get("form3-name")
            name4 = request.POST.get("form4-name")
            name5 = request.POST.get("form5-name")
            gender1 = request.POST.get("form1-gender")
            gender2 = request.POST.get("form2-gender")
            gender3 = request.POST.get("form3-gender")
            gender4 = request.POST.get("form4-gender")
            gender5 = request.POST.get("form5-gender")
            age1 = request.POST.get("form1-age")
            age2 = request.POST.get("form2-age")
            age3 = request.POST.get("form3-age")
            age4 = request.POST.get("form4-age")
            age5 = request.POST.get("form5-age")
            phone1 = request.POST.get("form1-phone")
            phone2 = request.POST.get("form2-phone")
            phone3 = request.POST.get("form3-phone")
            phone4 = request.POST.get("form4-phone")
            phone5 = request.POST.get("form5-phone")
            user = request.user
            seat1 = seat_id[0]
            seat2 = seat_id[1]
            seat3 = seat_id[2]
            seat4 = seat_id[3]
            seat5 = seat_id[4]

            book1 = Booking(user=user, name=name1, gender=gender1, age=age1, phone=phone1, seat_id=seat1)
            book1.save()
            book_id.append(book1.id)

            book2 = Booking(user=user, name=name2, gender=gender2, age=age2, phone=phone2, seat_id=seat2)
            book2.save()
            book_id.append(book2.id)

            book3 = Booking(user=user, name=name3, gender=gender3, age=age3, phone=phone3, seat_id=seat3)
            book3.save()
            book_id.append(book3.id)

            book4 = Booking(user=user, name=name4, gender=gender4, age=age4, phone=phone4, seat_id=seat4)
            book4.save()
            book_id.append(book4.id)

            book5 = Booking(user=user, name=name5, gender=gender5, age=age5, phone=phone5, seat_id=seat5)
            book5.save()
            book_id.append(book5.id)

        elif len(seat_id) == 6:
            name1 = request.POST.get("form1-name")
            name2 = request.POST.get("form2-name")
            name3 = request.POST.get("form3-name")
            name4 = request.POST.get("form4-name")
            name5 = request.POST.get("form5-name")
            name6 = request.POST.get("form6-name")
            gender1 = request.POST.get("form1-gender")
            gender2 = request.POST.get("form2-gender")
            gender3 = request.POST.get("form3-gender")
            gender4 = request.POST.get("form4-gender")
            gender5 = request.POST.get("form5-gender")
            gender6 = request.POST.get("form6-gender")
            age1 = request.POST.get("form1-age")
            age2 = request.POST.get("form2-age")
            age3 = request.POST.get("form3-age")
            age4 = request.POST.get("form4-age")
            age5 = request.POST.get("form5-age")
            age6 = request.POST.get("form6-age")
            phone1 = request.POST.get("form1-phone")
            phone2 = request.POST.get("form2-phone")
            phone3 = request.POST.get("form3-phone")
            phone4 = request.POST.get("form4-phone")
            phone5 = request.POST.get("form5-phone")
            phone6 = request.POST.get("form6-phone")
            user = request.user
            seat1 = seat_id[0]
            seat2 = seat_id[1]
            seat3 = seat_id[2]
            seat4 = seat_id[3]
            seat5 = seat_id[4]
            seat6 = seat_id[5]

            book1 = Booking(user=user, name=name1, gender=gender1, age=age1, phone=phone1, seat_id=seat1)
            book1.save()
            book_id.append(book1.id)

            book2 = Booking(user=user, name=name2, gender=gender2, age=age2, phone=phone2, seat_id=seat2)
            book2.save()
            book_id.append(book2.id)

            book3 = Booking(user=user, name=name3, gender=gender3, age=age3, phone=phone3, seat_id=seat3)
            book3.save()
            book_id.append(book3.id)

            book4 = Booking(user=user, name=name4, gender=gender4, age=age4, phone=phone4, seat_id=seat4)
            book4.save()
            book_id.append(book4.id)

            book5 = Booking(user=user, name=name5, gender=gender5, age=age5, phone=phone5, seat_id=seat5)
            book5.save()
            book_id.append(book5.id)

            book6 = Booking(user=user, name=name6, gender=gender6, age=age6, phone=phone6, seat_id=seat6)
            book6.save()
            book_id.append(book6.id)


        request.session["id"] = book_id

        template = 'payment.html'
        context = {}
    return render(request, template, context)

@login_required
def book_seats(request, bus_number,):
    template = 'error.html'
    context = {}
    valid = Bus.objects.filter(bus_number=bus_number,)

    if valid.exists():
        for info in valid:
            bcapacity = info.capacity
            bprice = info.price
            request.session["bus_number"] = info.bus_number


        seat_info = Seat.objects.filter(bus__bus_number=bus_number)
        for info in seat_info:
            if info.status == 'unavailable':
                seat_id = info.id
                ticket_info = Ticket.objects.filter(book__seat=seat_id)
                if ticket_info.count()==0 and "active" not in request.session:

                    change = Seat.objects.get(pk=seat_id)
                    change.status = 'available'
                    change.save()

                    booking_form = Booking.objects.filter(seat=seat_id)
                    if booking_form.exists():
                        Booking.objects.get(seat=seat_id).delete()



        seat_info = Seat.objects.filter(bus__bus_number=bus_number)



        template = 'seats.html'
        context = {'capacity': bcapacity, 'price': bprice, 'seats':seat_info}
        
    return render(request, template, context)


@login_required
def final(request):
    template = "error.html"
    context = {}

    if "active" in request.session and "id" in request.session and "bus_number" in request.session and "seat_id" in request.session:
        book_id = request.session["id"]

        for id in book_id:
            ticket = Ticket(book_id=id)
            ticket.save()

        template = "success.html"

        del request.session["id"]
        del request.session["bus_number"]
        del request.session["seat_id"]
        del request.session["active"]

    return render(request,template,context)
