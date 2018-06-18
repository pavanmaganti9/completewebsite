from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import website,FormData,Document
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filters import UserFilter
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm

# Create your views here.
def index(request):
	#return HttpResponse('Hello Pavan!')
	return render(request, 'index.html', {'title' : 'Home'})
	
def about(request):
	#return HttpResponse('Hello Pavan!')
	return render(request, 'about.html', {'title' : 'About'})
	
def backend(request):
	Website = website.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(Website, 3)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
		# context = {
		# 'title' : 'Dynamic',
		# 'website' : Website,
		# 'users': users
	# }
	return render(request, 'backend.html', { 'users': users,'title' : 'Dynamic Content' })
	
def details(request, id):
	Content = website.objects.get(id=id)
	context = {
		'content' : Content,
		'title' : 'Content Details'
	}
	return render(request, 'details.html', context)
	
def contact(request):
	return render(request, 'contact.html', {'title' : 'Contact'})
	
	
def login(request):
	return render(request, 'login.html', {'title' : 'Login'})
	
def form(request):
	return render(request, 'form.html', {'title' : 'Form data'})
	
def formsubmit(request):
	print("Form Submitted!")
	form_name = request.POST["name"]
	form_email = request.POST["email"]
	form_address = request.POST["address"]
	
	form_data = FormData(name=form_name,email=form_email,address=form_address)
	form_data.save()
	
	return render(request, 'success.html', {'title' : 'Data Submitted'})
	
def submitted_data(request):
	formdata = FormData.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(formdata, 2)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
	return render(request, 'submitted_data.html', { 'users': users,'title' : 'Submitted form data' })

def formdetails(request, id):
	Content = FormData.objects.get(id=id)
	context = {
		'formdata' : Content,
		'title' : 'Submitted form data'
	}
	return render(request, 'formdetails.html', context)
	
def search(request):
	user_list = FormData.objects.all()
	user_filter = UserFilter(request.GET, queryset=user_list)
	return render(request, 'search.html', {'filter': user_filter,'title' : 'Search form data'})
	
def fileupload(request):
	if request.method == 'POST' and request.FILES['myfile']:
			#form_file = request.POST["myfile"]
			myfile = request.FILES['myfile']
			form_file_desc = request.POST["description"]
			form_file_path = request.FILES['myfile']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.url(filename)
			
			form_data = Document(document=uploaded_file_url,description=form_file_desc)
			form_data.save()
			#myfile = request.FILES['myfile']
			#fs = FileSystemStorage()
			#filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.url(filename)
			return render(request, 'fileupload.html', {
				 'uploaded_file_url': uploaded_file_url,
				 'title' : 'File Upload'
			})
	return render(request, 'fileupload.html',{'title' : 'File Upload'})
	# if request.method == 'POST':
			# form = DocumentForm(request.POST, request.FILES)
			# if form.is_valid():
				# form.save()
				# return render(request, 'fileupload.html', {'title' : 'Search form data'})
	# else:
			# form = DocumentForm()
			# return render(request, 'fileupload.html', {
			# 'form': form,
			# 'title' : 'File Upload'
	# })
	