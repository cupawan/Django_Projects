from django.shortcuts import render
from django.http import JsonResponse
from .forms import TranslateForm
from Scripts.Translate import Translator

def translate_text(request):
    if request.method == "POST":
        form = TranslateForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            target = form.cleaned_data['target_language'].title()
            obj = Translator()
            target = obj.language_to_code(target)
            detected_language = obj.detect_language(text)
            
            if detected_language:
                print(f"Source: {detected_language}") 
                
            translation,source = obj.translate(text,target)
            
            data = {
                'detectedLanguage': detected_language,
                'translatedText': translation,
                'source': source,
                'target' : obj.code_to_language(target)
            }


            return render(request, 'result.html',data)
    else:
        form = TranslateForm()

    return render(request, 'index.html', {'form': form})
