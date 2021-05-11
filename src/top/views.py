import environ
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

env = environ.Env()
env.read_env('.env')

# Create your views here.
def index(request):
    return render(request, 'top/index.html')

def join(request):
    if request.POST["email"] == "":
        return render(request, 'top/fail.html')
    else:
        subject = "エンジニア集会場の参加リンクの送付"
        message = "エンジニア集会場にご参加して頂きありがとうございます。以下のURLからご参加ください。\n" + env('SEND_MESSAGE_LINK') + "\n参加後は「自己紹介」チャンネルにて簡単に自己紹介をお願いします！ \\n\n今後とも宜しくお願いいたします。"
        from_email = env('EMAIL_HOST_USER')  # 送信者
        recipient_list = [request.POST["email"]]  # 宛先リスト
        send_mail(subject, message, from_email, recipient_list)
        return render(request, 'top/success.html')
