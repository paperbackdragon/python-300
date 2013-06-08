from django.shortcuts import render_to_response
from django.template import RequestContext
import md5
import random

def index(request):
    r = random.random()
    m = md5.md5(str(r))
    # this might be tough to access in pdb, may have to use exec "d = 'foo'" 
    d = {'data': m.hexdigest()}

    1/0
    return render_to_response("index.html", d, context_instance=RequestContext(request))
