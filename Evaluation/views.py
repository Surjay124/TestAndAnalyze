import base64
import io
import urllib.parse

import matplotlib.pyplot as plt
import razorpay
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def startQuiz(request):
    razorpay_Client = razorpay.Client(
        auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
    currency = 'INR'
    amount = 60000

    razorpay_order = razorpay_Client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))

    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'quiz'

    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url

    # return render(request, 'payment.html', context=context)
    return render(request, 'index.html', context=context)


@csrf_exempt
def actualQuiz(request):
    return render(request, 'quiz.html')


def actualQuiz2(request):
    return render(request, 'quiz2.html')


def actualQuiz3(request):
    return render(request, 'quiz3.html')


def actualQuiz4(request):
    return render(request, 'quiz4.html')


pcnt = []


def fetch_value(request):
    p1 = request.POST['Percentage']
    pcnt.append(float(p1))
    print(pcnt)

    return HttpResponse("Data is stored fv\n Click the back button to go back to your test")


def fetch_value2(request):
    p1 = request.POST['Percentage2']
    pcnt.append(float(p1))
    print(pcnt)

    return HttpResponse("Data is stored fv2\n Click the back button to go back to your test")


def fetch_value3(request):
    p1 = request.POST['Percentage3']
    pcnt.append(float(p1))
    print(pcnt)

    return HttpResponse("Data is stored fv3\n Click the back button to go back to your test")


def fetch_value4(request):
    p1 = request.POST['Percentage4']
    pcnt.append(float(p1))
    print(pcnt)

    return HttpResponse("Data is stored fv4\n Click the back button to go back to your test")


def analyzeResult(request):
    data = pcnt
    print(data)
    myLabels = ["OOPs", "Wrapper Class", "Collections", "Exception and File Handling"]
    # plt.bar(myLabels,[16.666666664,25,100,40])
    plt.bar(myLabels, data)
    # plt.yticks(np.arange(0,100,10))
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'analyzeResult.html', context={'data': uri})
