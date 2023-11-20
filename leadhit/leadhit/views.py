from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from tinydb import TinyDB, Query

from .constants import DB_PATH, NAME_FIELD
from .validators import type_validator

@csrf_exempt
def get_form(request):
    db = TinyDB(DB_PATH)
    params = type_validator(request.GET.dict())
    for i in [{k: v} for k, v in params.items()]:
        forms = db.search(Query().fragment(i))
        for form in forms:
            a = set((k, v) for k,v in form.items() if k != NAME_FIELD)
            b = set((k, v) for k,v in params.items())
            if a.issubset(b):
                return JsonResponse({NAME_FIELD: form.get(NAME_FIELD)})
    return JsonResponse(params)
