# core/views.py
from django.shortcuts import render, redirect
from . import utils

def dashboard(request):
    context = {
        'interfaces': utils.get_interfaces(),
        'route_table': utils.get_routing_table(),
        # Если в сессии есть результаты сниффинга, достаем их
        'packets': request.session.pop('packets', None),
        'ping_result': request.session.pop('ping_result', None)
    }
    return render(request, 'core/dashboard.html', context)

def configure_ip(request):
    if request.method == 'POST':
        utils.set_ip_address(
            request.POST.get('interface'),
            request.POST.get('ip'),
            request.POST.get('mask'),
            request.POST.get('gateway')
        )
    return redirect('dashboard')

def diagnostic_ping(request):
    if request.method == 'POST':
        host = request.POST.get('host')
        output = utils.ping_host(host)
        request.session['ping_result'] = output
    return redirect('dashboard')

def sniff_traffic(request):
    """Анализ трафика"""
    if request.method == 'POST':
        # Захватываем 10 пакетов
        packets = utils.capture_packets(count=15)
        request.session['packets'] = packets
    return redirect('dashboard')