from django.shortcuts import render, HttpResponse
from home.models import Contact
import datetime

def index(request):
    temp = {
        "a":"This is A",
        "b": "This is B"
    }
    return render(request, 'index.html', temp)

def about(request):
    return HttpResponse('THIS IS ABOUT PAGE')

    

def contact(request):
    # if request.method == 'POST':
    #     # post_data = request.POST.get()
    #     # print(post_data)
    #     exit()
    if request.method == 'POST':
        post = request.POST
        contact = Contact(
            name = request.POST.get('email'),
            email = request.POST.get('phone'),
            amount = post.get('amount'),
            posted_on = datetime.datetime.now()
        )
        contact.save()
    

    return render(request, 'contacts.html')
    # return HttpResponse('THIS IS CONTACTS PAGE')


