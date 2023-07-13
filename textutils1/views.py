from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')
    # return HttpResponse(f'Home \n <a href="https://chat.openai.com/"> Google</a>')


def analyze_text(request):
    djtxt = request.GET.get('text', 'off')
    removepuch = request.GET.get('removepunc', 'off')
    caps = request.GET.get('full_cap', 'off')
    capital = request.GET.get('capital', 'off')
    newlineremover= request.GET.get('line_remover', 'off')
    space = request.GET.get('space_remover', 'off')
    if removepuch == 'on':
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for i in djtxt:
            if i not in punctuation:
                analyzed += i
        param = {'remove': 'remove punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)
    elif caps=='on':
        analyzed=''
        for i in djtxt:
            analyzed+=i.upper()
        param = {'remove': 'Upper Case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)
    elif newlineremover == "on":
        analyzed = ""
        for char in djtxt:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text

        return render(request, 'analyze.html', params)
    elif capital=='on':
        analyzed=djtxt.capitalize()
        param = {'remove': 'Capitalization', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)
    elif space=='on':
        analyzed=''
        for i in djtxt:
            if i!=' ':
                analyzed+=i

        param = {'remove': 'Space Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)
    else:
        return HttpResponse('Error')



