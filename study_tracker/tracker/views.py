from . forms import SessionForm
from . models import StudySession
from django.shortcuts import render,redirect,get_object_or_404


def add_session(request):

    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            return redirect('home')
    else:
        form = SessionForm()

    return render(request,'form.html', {'form' : form})


def session_list(request):
    sessions = StudySession.objects.filter(user = request.user)
    return render(request,'session_list.html', {"sessions" : sessions})


def delete_session(request , id):
    session = get_object_or_404(StudySession, id = id, user=request.user)
    session.delete()
    return redirect('session_list')

def update_session(request,id):
    session = get_object_or_404(StudySession, id = id , user = request.user)
    if request.method == 'POST':
        form = SessionForm(request.POST, instance = session)
        if form.is_valid():
            updated = form.save(commit = False)
            updated.user = request.user
            updated.save()
            return redirect("session_list")
    else: 
        form = SessionForm(instance = session)
    return render(request,'form.html', {'form' : form})