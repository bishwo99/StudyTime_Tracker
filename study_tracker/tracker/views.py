from . forms import SessionForm,UserForm
from . models import StudySession
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


@login_required
def add_session(request):

    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            return redirect('session_list')
    else:
        form = SessionForm()

    return render(request,'form.html', {'form' : form})

@login_required
def session_list(request):
    sessions = StudySession.objects.filter(user = request.user)

    start = request.GET.get('start')
    end = request.GET.get('end')

    if start and end:
        sessions = sessions.filter(created_at__date__range = [start,end])
    elif start:
        sessions = sessions.filter(created_at__date__gte =start)
    elif end:
        sessions = sessions.filter(created_at__date__lte=end )


    return render(request,'session_list.html', {"sessions": sessions})

@login_required
def delete_session(request , id):
    session = get_object_or_404(StudySession, id = id, user = request.user)
    session.delete()
    return redirect('session_list')

@login_required
def update_session(request,id):
    session = get_object_or_404(StudySession, id = id, user = request.user)
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


def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)

            return redirect('session_list')
    else:
        form = UserForm()
    return render(request,'signup.html',{"form":form})


