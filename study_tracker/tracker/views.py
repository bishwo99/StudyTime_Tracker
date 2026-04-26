from . forms import SessionForm
from . models import StudySession
from django.shortcuts import render,redirect


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