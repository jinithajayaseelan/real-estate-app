from django.shortcuts import render
from .models import Agent

# Create your views here.
def agents_list(request):
	agent_list= Agent.objects.all()


	return render(request , 'agents.html', {'agent_list': agent_list})