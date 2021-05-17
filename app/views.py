from django.shortcuts import render, redirect
from .models import Memo, Tags
from django.shortcuts import get_object_or_404
from .forms import MemoForm


def index(request):
    memos = Memo.objects.all().order_by('-updated_datetime')
    return render(request, 'app/index.html', {'memos': memos})


def detail(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    tags = Tags.objects.filter(memo=memo_id)
    return render(request, 'app/detail.html', {'memo': memo, 'tags': tags})


def new_memo(request):
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:   
        form = MemoForm
    return render(request, 'app/new_memo.html', {'form': form})
