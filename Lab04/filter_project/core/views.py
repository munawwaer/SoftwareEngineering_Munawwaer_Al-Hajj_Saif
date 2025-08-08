from django.shortcuts import render
from django.utils.text import slugify
from django.template.defaultfilters import capfirst, truncatewords, truncatechars
import datetime
import random

# Create your views here.
import datetime
def filter_view(request):
    context={
        'name':"Munawwaer",
        "bio":"Django is a high-level pyhton web framework.",
        "item_count":5,
        "price":29.995,
        "birthday":datetime.date(2025,7,29),
        "items":["Python","Django","JavaScript"],
        "empty_vareble":None,
        "html_code":'<h3>This is <strong> safe </strong> HTML </h3> ',
    }
    return render(request,'core/index.html',context)


def filters_view(request):
    # بيانات معدة مسبقًا لعرض تأثير الفلاتر التي تحتاج أنواعًا خاصة
    context = {
        'original_text': '',
        'result': '',
        'today': datetime.datetime.now(),
        'past_date': datetime.datetime.now() - datetime.timedelta(days=5),
        'future_date': datetime.datetime.now() + datetime.timedelta(days=5),
        'my_list': ['تفاح', 'برتقال', 'موز'],
        'file_size_in_bytes': 123456789,
        'my_number': 3.14159265,
        'is_happy': True,
        'is_sad': False,
        'is_unknown': None,
        'html_string': '<em>هذا النص مهم</em>'
    }

    if request.method == 'POST':
        text = request.POST.get('user_text', '')
        context['original_text'] = text
        
        filter_type = request.POST.get('filter_type')

        result_text = ''
        # --- تطبيق الفلاتر التفاعلية ---
        if filter_type == 'upper':
            result_text = text.upper()
        elif filter_type == 'lower':
            result_text = text.lower()
        elif filter_type == 'capfirst':
            result_text = capfirst(text)
        elif filter_type == 'title':
            result_text = text.title()
        elif filter_type == 'slugify':
            result_text = slugify(text)
        elif filter_type == 'length':
            result_text = f"عدد الأحرف: {len(text)}"
        elif filter_type == 'wordcount':
            result_text = f"عدد الكلمات: {len(text.split())}"
        elif filter_type == 'truncatewords':
            result_text = truncatewords(text, 4)
        elif filter_type == 'truncatechars':
            result_text = truncatechars(text, 15)
        elif filter_type == 'linebreaks':
            # هذا الفلتر يحول السطور الجديدة إلى وسوم <p> و <br>
            # لنعرضه ككود حتى يظهر تأثيره
            from django.template.defaultfilters import linebreaks as lb
            result_text = f"الكود الناتج: {lb(text)}"
        elif filter_type == 'striptags':
            from django.utils.html import strip_tags
            result_text = strip_tags(text)

        context['result'] = result_text

    return render(request, 'core/userfilter.html', context)