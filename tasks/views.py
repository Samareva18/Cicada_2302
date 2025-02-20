from django.shortcuts import render, redirect


def index(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'cicada_2302' and password == 'love_ctf':
            return redirect('/cipher')
        else:
            error_message = "Попробуй еще раз"

    return render(request, 'index.html', {'error_message': error_message})


def image(request):
    return render(request, 'image.html')


#Well done, now enter it in the field: goooodjob
def cipher(request):
    error_message = None
    if request.method == 'POST':
        flag = request.POST.get('flag')

        if flag == 'goooodjob':
            return redirect('/сhange_the_boundaries')
        else:
            error_message = "Попробуй еще раз"

    return render(request, 'cipher.html', {'error_message': error_message})


# ci172ca8da02
def audio(request):
    error_message = None
    if request.method == 'POST':
        flag = request.POST.get('flag')

        if flag == 'ci172ca8da02':
            return redirect('/final')
        else:
            error_message = "Попробуй еще раз"
    return render(request, 'pilots.html', {'error_message': error_message})


def final(request):
    return render(request, 'final.html')
