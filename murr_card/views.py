from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def murr_card_list(request):
    return render(request, 'murr_card/murr_card_list.html')
