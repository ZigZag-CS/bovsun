# -*- coding: utf-8 -*-
from django.http import HttpResponseBadRequest


def ajax_required(f):
    def wrap(request, *args, **kwargs):
        """
        https://docs.djangoproject.com/en/2.0/ref/request-response/
        Возвращает True, если запрос был выполнен через XMLHttpRequest,
        путем проверки заголовка HTTP_X_REQUESTED_WITH для строки
        «XMLHttpRequest». Большинство современных библиотек
        JavaScript отправляют этот заголовок.
        Если вы напишете свой собственный вызов XMLHttpRequest
        (со стороны браузера), вам нужно будет установить этот
        заголовок вручную, если вы хотите, чтобы is_ajax () работал.
        """
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__  # вернуть строки
    wrap.__name__ = f.__name__
    return wrap
