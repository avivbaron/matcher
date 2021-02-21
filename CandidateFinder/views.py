from django.shortcuts import render, redirect, get_object_or_404
from CandidateFinder.models import Skill, Job, Candidate
from . forms import CandidateForm


def dashboard(request):
    candidates = Candidate.objects.all().order_by('-skills')
    jobs = Job.objects.all()
    total_candidates = candidates.count()
    total_software = candidates.filter(skills__name__in=['C++', 'SQL', 'Java', 'C']).count()
    total_backend = candidates.filter(skills__name__in=['NodeJS', 'django']).count()
    total_frontend = candidates.filter(skills__name__in=['VueJS', 'React']).count()

    context = {'candidates':candidates, 'jobs':jobs, 'total_candidates':total_candidates,
    'total_software':total_software,'total_backend':total_backend,
    'total_frontend':total_frontend}

    return render(request, 'dashboard.html', context)

def candidate(request, pk):
    candidate = Candidate.objects.get(id=pk)
    skill = candidate.skills
    job = candidate.job

    context = { 'candidate': candidate }
    return render(request, 'candidate.html', context)

#-------------------(CREATE VIEWS) -------------------

def createOrder(request):
	action = 'create'
	form = CandidateForm()
	if request.method == 'POST':
		form = CandidateForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {'action':action, 'form':form}
	return render(request, 'candidate_form.html', context)

#-------------------(UPDATE VIEWS) -------------------

def updateOrder(request, pk):
	action = 'update'
	candidate = get_object_or_404(Candidate, pk=pk)
	form = CandidateForm(instance=candidate)

	if request.method == 'POST':
		form = CandidateForm(request.POST, instance=candidate)
		if form.is_valid():
			form.save()
			return redirect('/candidate/' + str(pk))

	context =  {'action':action, 'form':form}
	return render(request, 'candidate_form.html', context)

#-------------------(DELETE VIEWS) -------------------

def deleteOrder(request, pk):
	candidate = Candidate.objects.get(id=pk)
	if request.method == 'POST':
		candidate_id = candidate.id
		candidate.delete()
		return redirect('dashboard')

	return render(request, 'delete_candidate.html', {'item':candidate})


def index(request):
    candidate_list = Candidate.objects.all()
    jobs_list = Job.objects.filter(job_title__exact='Back-end')
    context = {
    "candidate_list" : candidate_list ,
    "jobs_list" : jobs_list
    }

    return render(request, 'index.html', context)
