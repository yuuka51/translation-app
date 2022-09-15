from operator import imod
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import deepl
from .forms import TranslationForm
from django.conf import settings

# Create your views here.


def index(request):
    """
    翻訳画面
    """
    # 翻訳結果
    translation_results = ""

    if request.method == "POST":
        # 翻訳ボタン押下時

        form = TranslationForm(request.POST)

        # バリデーションチェック
        if form.is_valid():
            # 翻訳
            translator = deepl.Translator(settings.DEEPL_API_KEY)

            # 翻訳文を取得
            sentence = form.cleaned_data['sentence']
            # 日本語に翻訳
            translation_results = translator.translate_text(
                sentence, target_lang="EN-US")

    else:
        form = TranslationForm()

    template = loader.get_template('translation/index.html')
    context = {
        'form': form,
        'translation_results': translation_results
    }
    return HttpResponse(template.render(context, request))