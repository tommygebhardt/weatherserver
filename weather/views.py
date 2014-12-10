from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from weather.models import node, weather
# Create your views here.

def index(request):
    all_nodes = node.objects.order_by('id')
    context = {'all_nodes': all_nodes}
    return render(request,'weather/index.html', context)

def detail(request, node_id):
    Node = get_object_or_404(node,pk=node_id)
    # TODO: Add in database information
    return render(request, 'weather/detail.html', {'Node' : Node})


def submit(request):
    try:
        n = get_object_or_404(node, pk=request.POST['NodeID'])
    except (KeyError, NodeID.DoesNotExist):
        return(request, 'weather/detail.html', {'error_mesage':"The node is not in the table"})
    else:
        r = n.nodeID_set.create(Time=request.POST['Time'], TimeReceived=timezone.now(),\
                                Temp=request.POST['Temp'], Humd=request.POST['Humdity'])

        return HttpResponse('Submitted. Thanks!')
