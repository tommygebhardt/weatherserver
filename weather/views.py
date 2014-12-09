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
        report = request.POST[''])
    
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
