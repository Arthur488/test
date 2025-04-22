from django.http import JsonResponse
from django.shortcuts import render


def healthcheck(request):
    return JsonResponse({"status": "ok"}, status=200)
