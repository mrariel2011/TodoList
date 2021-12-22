from django.shortcuts import render
from tasks.models import Task
from datetime import date, datetime
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    doneCount = Task.objects.filter(done=True, user=request.user).count
    notdoneCount = Task.objects.filter(done=False, user=request.user).count
    todayCount = Task.objects.filter(due_to=date.today(), user=request.user).count
    expiredCount = Task.objects.filter(due_to=datetime.now(), user=request.user).count

    context = {
        "done_count": doneCount,
        "notdone_count": notdoneCount,
        "today_count": todayCount,
        "expired_count": expiredCount,
    }
    return render(request, "homepage/home.html", context)
