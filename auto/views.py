#-*- coding: utf-8 -*-


from django.shortcuts import render
from django.conf import settings
from .forms import *
from django.core.mail import EmailMessage
import json
from .models import *


def sender_mail(theme, text):
    msg=EmailMessage(theme, text, settings.SERVER_EMAIL, [settings.MASTER_EMAIL])
    msg.content_subtype = 'html'
    msg.send()


def main_view(request):
    interests = Interest.objects.all()
    comments = Comments.objects.order_by('?')
    adr = Adress.objects.all()
    sListTO = ServiceListTO.objects.all()
    sList = ServiceList.objects.all()
    images = ImageOfWorks.objects.all().order_by('-date')[:6]
    path = adr[0].path
    coords = adr[0].coords
    street = adr[0].street
    servitems = json.dumps([dict(item) for item in
                            ServiceItems.objects.all().values('title__type', 'description', 'price')])
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            author = request.POST['author']
            text = request.POST['text']
            fmail = 'от: %s.  Отзыв: %s. Напоминание: необходимо разрешить показывать' \
                    ' этот отзыв на сайте или удалить...' \
                    % (author.title(), text.capitalize())
            theme = 'Оставлен новый отзыв по работам от пользователя %s.' % author.title()
            sender_mail(theme, fmail)
            comment.save()
        return render(request, 'success.html', {'author': author })
    else:
        form = CommentsForm()


    return render(request, 'base.html',
                  {'interests': interests, 'comments' : comments ,'servitems': servitems,
                   'form': form, 'path' : path, 'coords': coords , 'street': street,
                   'sList': sList, 'sListTO': sListTO, 'images': images})

