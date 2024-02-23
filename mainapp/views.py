from django.shortcuts import render, redirect
from django.http import JsonResponse
from .services.queries_services import *


def query(request):
    result, status_code = query_handler(request)
    return JsonResponse(result, status=status_code)


def return_result(request):
    result, status_code = get_result(request)
    return JsonResponse(result, status=status_code)


def ping(request):
    status, status_code = ping_server()
    return JsonResponse(status, status=status_code)


def history(request):
    history, status_code = get_history(request)
    return JsonResponse(history, status=status_code)