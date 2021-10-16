from django.http import HttpResponse
from datetime import datetime
import json


def hello_world(request):

    now = datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs')
    return HttpResponse('Hello word! {now}'.format(now=str(now)))


def sorted(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted sucessfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request,name,age):
    if age < 12:
        message='Sorry {}, you are not allowed here'.format(name)
    else: 
        message='hello, {}!welcome to Platzigram'.format(name)
    return HttpResponse(message)
