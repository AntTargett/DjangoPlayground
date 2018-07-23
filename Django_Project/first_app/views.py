from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    my_test_dictionary = {"insert_text": "I am a piece of text plz dun h8 meh"}
    return render(request, 'first_app/index.html', context=my_test_dictionary)