from django.shortcuts import render
from tasks.models import Task
from datetime import date, datetime


def home(request):
    doneCount = Task.objects.filter(done=True).count
    notdoneCount = Task.objects.filter(done=False).count
    todayCount = Task.objects.filter(due_to=date.today()).count
    expiredCount = Task.objects.filter(due_to=datetime.now()).count

    context = {
        "done_count": doneCount,
        "notdone_count": notdoneCount,
        "today_count": todayCount,
        "expired_count": expiredCount,
    }
    return render(request, "homepage/home.html", context)
