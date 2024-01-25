from django.shortcuts import render
from django.http import JsonResponse
from .forms import TranslateForm
from .translate import Translator

def translate_text(request):
    if request.method == "POST":
        form = TranslateForm(request.POST)
        if form.is_valid():
            api = form.cleaned_data['api_key']
            text = form.cleaned_data['text']
            target = form.cleaned_data['target_language']
            obj = Translator(api_key=api)
            target = obj.language_to_code(target)
            detected_language = obj.detect_language(text)
            
            if detected_language:
                print(f"Source: {detected_language}") 
                
            translation,source = obj.translate(text,target)
            
            data = {
                'detectedLanguage': detected_language,
                'translatedText': translation,
                'source': source
            }


            return render(request, 'result.html',data)
    else:
        form = TranslateForm()

    return render(request, 'index.html', {'form': form})
