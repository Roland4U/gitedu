from gitedu.models import facultet, service
def facultets(request):
    return {
        'facultets': facultet.objects.all()[:8],
        'services': service.objects.all(),
        'service' : service.objects.all()[:5],
    }