from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    chars = ''

    if request.GET.get('uppercase_letters'):
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if request.GET.get('lowercase_letters'):
        chars += 'abcdefghijklmnopqrstuvwxyz'

    if request.GET.get('punctuation'):
        chars += '!#$%&*+-=?@^_'

    if request.GET.get('numbers'):
        chars += '0123456789'

    if request.GET.get('simbols'):
        for i in 'il1Lo0O':
            chars = chars.replace(i, '')

    length = int(request.GET.get('length', 12))
    thepassword = ''

    if len(chars) == 0:
        thepassword += 'Выберите хотя бы один пункт...'
    else:
        for i in range(length):
            thepassword += random.choice(chars)

    return render(request, 'generator/password.html', {'password': thepassword})
