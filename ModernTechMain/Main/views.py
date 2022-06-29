from django.shortcuts import render
from .forms import MessagesForm
import telebot
# Create your views here.
def Main(request):
    return render(request, 'main/main.html')
def Background(request):
    return render(request, 'main/background.html')
def Contact(request):
    error = ''
    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid():
            form.save()
            text = form.cleaned_data.get("message")
            cont = form.cleaned_data.get("contact")
            token = '5597625973:AAFYCYSlqyxC-OSz_UBe1d4nuzjouYj9Nts'
            bot = telebot.TeleBot(token)
            bot.send_message(5066558166, f"Новое сообщение на сайте ModernTechnologies:\n{text}\nКонтактная информация: {cont}")
        else:
            error = 'Неверно заполненные поля'
    form = MessagesForm()
    data = {
        'form': form
    }


    #bot.infinity_poling()
    return render(request, 'main/contact.html', data)
