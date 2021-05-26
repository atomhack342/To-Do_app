from django.shortcuts import render, redirect

import datetime
from datetime import datetime

import calendar
from calendar import HTMLCalendar
# Create your views here.

from .models import Document

def Notes(request):
    docid = int(request.GET.get('docid', 0))
    documents = Document.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')

        if docid > 0:
            document = Document.objects.get(pk=docid)
            document.title = title
            document.content = content
            document.save()

            return redirect('/?docid=%i' % docid)
        else:
            document = Document.objects.create(title=title, content=content)

            return redirect('/?docid=%i' % document.id)

    if docid > 0:
        document = Document.objects.get(pk=docid)
    else:
        document = ''

    context = {
        'docid': docid,
        'documents': documents,
        'document': document
    }

    return render(request, 'notes/notes.html', context)

def delete_document(request, docid):
    document = Document.objects.get(pk=docid)
    document.delete()

    return redirect('/?docid=0')



def Calendar(request):
    
    # get corrent year
    now = datetime.now()
    current_year = now.year

    month = now.month
    year = now.year

    # convert month from name to number
    # month_number = list(calendar.month_name).index(month)
    # month_number = int(month_number)

    

    # create a calendar
    cal = HTMLCalendar().formatmonth(
        year,
        month
    )


    # get current time
    time = now.strftime('%I:%M %p')

    return render(request, 
        'notes/calendar.html', {
        "year": year,
        "month": month,
        # "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time": time

     })
