from django.shortcuts import render, redirect
from .models import Note
from .forms import AddNote
from time import gmtime, strftime
from calendar import monthrange
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def notes(request):
    notes_list = Note.objects.all().order_by('-publish_date')
    page = request.GET.get('page',1)
    paginator = Paginator(notes_list, 4)
    number = Note.objects.all().count()
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)
    return render(request, 'notes.html', {'notes' : notes, 'number': number})

def calendar(request):
    if request.method == "POST":
        query = dict(date="")
        if 'date' in request.POST:
            notes = Note.objects.filter(publish_date=request.POST['date'])
            query['date'] = request.POST['date']
            return render(request, 'calendar.html',  {'notes': notes, 'query': query})
    else:
        return render(request, 'calendar.html')

def add(request):
    if request.method == "POST":
        form = AddNote(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            publish_date = form.cleaned_data['date']
            note = form.cleaned_data['text']
            f = Note(title=title, publish_date=publish_date, note=note)
            f.save()
            message = "Added ✓"
            return render(request, 'add.html', {'form': form, 'message': message})
    else:
        form = AddNote()
    return render(request, 'add.html', {'form': form})

def about(request):
    all_notes = Note.objects.all().count()
    year = strftime("%Y", gmtime())
    month = strftime("%m", gmtime())
    date = '{0}-{1}-01'.format(year, month)
    if (month != '10') or (month != '11') or (month != '12'):
        month2 = month.lstrip('0')
        month_r = int(month2)
    else:
        month_r = int(month)
    year_r = int(year)
    days = monthrange(year_r, month_r)[1]
    date_2 = '{0}-{1}-{2}'.format(year, month, days)
    notes_in_month = Note.objects.filter(publish_date__range=(date, date_2)).count()
    newest = Note.objects.all().order_by('-publish_date')[0]
    return render(request, 'about.html', {'all_notes' : all_notes, 'notes_in_month': notes_in_month, 'newest':newest})
