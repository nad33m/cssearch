from glob import escape
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q, OuterRef, Subquery
# from .forms import *
from django.contrib import messages

# Create your views here.
def index(request): 
    return render(request, 'cssearch/home.html')


def testing_db(request):
    # schools = csinfo.objects.all().order_by('scode')
    q = request.GET.get('q')
     # get the scode from the input box
    if q:
        q = q[:100]
        q = escape(q)
    else:
        q=' '
    
    if q:
        # artists = Artist.objects.filter(name__icontains=url_parameter)
        # schools = csinfo.objects.filter(Q(scode__icontains=q) | Q(sname__icontains=q))
        schools = csinfo.objects.filter(Q(scode__icontains=q) | Q(sname__icontains=q))
        total_records = schools.count
        teachers = cst042024.objects.filter(scode__in=schools.values_list('scode', flat=True))
        # teachers = cst042024.objects.filter(scode=q)
        # teachers = cst042024.objects.all()
        # dataentry = dataentry.filter(Q(bemiscode__icontains=q) | Q(schoolname__icontains=q))
    # form = csinfoForm()
    
    # if request.method == 'POST':
    #     form = csinfoForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect ('/')

    context = {'schools': schools,
            #    'form':form,   
               'teachers': teachers,
               'total_records' : total_records,
               
               }
    # return HttpRessponse('Hello world!')
    return render(request, 'cssearch/testing.html', context)


def teacher_show(request, pk):
    teachers = cst042024.objects.filter(scode=pk)
    context = {
               # 'form':form,   
               'teachers': teachers,
               }
    
    return render(request, 'cssearch/teachers.html', context)

# # def index(request): 
#     tasks = Task.objects.all()

#     form = TaskForm()    
    
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect ('/')

#     context = {'tasks': tasks, 'form':form }
#     # return HttpRessponse('Hello world!')
#     return render(request, 'tasks/list.html', context)

def updateCs(request, pk):
    school = get_object_or_404(csinfo, id=pk)
    form = csinfoForm(instance=school)

    if request.method == 'POST':
        form = csinfoForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            messages.success(request, 'School updated successfully!')
            return redirect('test-page')

    context = {'form': form}
    return render(request, 'cssearch/update_school.html', context)