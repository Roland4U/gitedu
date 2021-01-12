from django.shortcuts import render
from django.contrib.auth.models import User as usr
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.conf import settings
from .models import facultet, subscribe, training, service, orderto, ordertoserv

# Create your views here.
def home(request):
	fac = facultet.objects.all()
	return render(request, 'gitedu/index.html', {'fac':fac})

def login1(request):	
	if request.method == 'POST':
		username = request.POST.get('username')
		if (usr.objects.filter(username=username).exists()):
			uss = usr.objects.get(username=username)
			if check_password(request.POST.get("password"), uss.password):
				password =  request.POST.get('password')
				log_user = authenticate(username = username, password = password)
				login(request, log_user)
				return HttpResponseRedirect('/')
			else:
				return render(request,'gitedu/index.html',{'err':'Մուտքագրված ծածկագիրը սխալ է', 'show_err':True})
		else:
			return render(request,'gitedu/index.html',{'err':'Այդ մուտքանունը ակտիվ չէ կամ գայություն չունի', 'show_err':True})


def save_reg(request):
	if request.method == 'POST':
		first_name = request.POST.get('name')
		last_name = request.POST.get('lname')
		username = request.POST.get('username')
		email =  request.POST.get('email')
		if request.POST.get('password')==request.POST.get('password_rep'):
		    if len(request.POST.get('password'))>=8:
		        password =  request.POST.get('password')
		        if not (usr.objects.filter(username=username).exists() or usr.objects.filter(email=email).exists()):
		            usr.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
		            user = authenticate(username = username, password = password)
		            login(request, user)
		            return HttpResponseRedirect('/')    
		        else:
		            if usr.objects.filter(username=username).exists():
		                return render(request,'gitedu/index.html',{'err':'Նշված մուտքանունը կրկնվում է', 'show_err':True})
		            else:
		                return render(request,'gitedu/index.html',{'err':'Նշված Էլ.Փոստը կրկնվում է', 'show_err':True})
		    else:
		        return render(request,'gitedu/index.html',{'err':'Ծածկագիր կարճ է', 'show_err':True})                    
		else:
		    return render(request,'gitedu/index.html',{'err':'Ծածկագրի կրկնությունը սխալ է', 'show_err':True})

def about(request):
	return render(request, 'gitedu/about.html')

def subscribe_mail(request):
	if request.method == 'POST':
		mail = subscribe(email = request.POST.get('email'))
		mail.save()
		return HttpResponseRedirect('/')

def facultet_det(request, fac_slug):
	fac = facultet.objects.get(slug=fac_slug)
	facs = facultet.objects.all()
	return render(request, 'gitedu/facultet.html', {'fac':fac, 'facs':facs})

def training_det(request, fac_slug, tr_slug):
	fac=facultet.objects.get(slug=fac_slug)
	tr=training.objects.get(slug=tr_slug)
	return render(request, 'gitedu/training.html', {'fac':fac, 'tr':tr})

def service_det(request, serv_slug):
	servs=service.objects.all()
	serv=service.objects.get(slug=serv_slug)
	return render(request, 'gitedu/service.html', {'servs':servs, 'serv':serv})

def facultets(request):
	fac=facultet.objects.all()
	return render(request, 'gitedu/facultets.html', {'fac':fac})

# Registration to training
def reg_to_tr(request):
	if request.method == 'POST':
		owner = request.POST
		name = owner.get('name')
		lname = owner.get('lname')
		phone = owner.get('phone')
		email = owner.get('email')
		fa = owner.get('fa')
		tra = owner.get('tra')
		if orderto.objects.filter(phone__iexact=phone) or orderto.objects.filter(email__iexact=email):
			subject = 'Դուք չեք կարող գրանցվել'
			message = ' Դուք չեք կարող գրանցվել արդեն '
			return render(request,'gitedu/index.html',{'err':'Դուք արդեն գրանցված եք', 'show_err':True, 'subj': subject, 'mess': message})
		else: 
			ordr = orderto(name=name, last_name=lname, phone=phone, email=email, fac=fa, tra=tra)
			ordr.save()
			subject = 'Շնորհակալություն մեր ծառայություններից օգտվելու համար'
			message = ' Մեր մասնագետները դիտարկում են ձեր հայտը: '
			# email_from = settings.EMAIL_HOST_USER
			recipient_list = [email,]
			# send_mail( subject, message, email_from, recipient_list )
			subject = '{0} {1}-ը ուղարկել է ({2}/{3})-ի մասնակցության հայտ'.format(name, lname, fa, tra)
			message = ''' Անուն - {0} {1}
			Էլ.փոստ - {2}
			Հեռախոսահամար - {3}
			Ֆակուլտետ - {4}
			Դասընթաց - {5}'''.format(name, lname, email, phone, fa, tra)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = ['gitedu@bk.ru',]
			send_mail( subject, message, email_from, recipient_list, fail_silently=False, )
			return render(request, 'gitedu/index.html', {'err': 'Ձեր հայտը ուղարկված է, մեր մասնագետները կկապնվեն ձեր թողած կոնտակտներով: Շնորհակալություն մեր ծառայություններից օգտվելու համար', 'show_err': True, 'subj': subject, 'mess': message})


# Registration to service
def reg_to_serv(request):
	if request.method == 'POST':
		owner = request.POST
		name = owner.get('name')
		lname = owner.get('lname')
		phone = owner.get('phone')
		email = owner.get('email')
		serv = owner.get('serv')
		text = owner.get('text')
		if orderto.objects.filter(phone__iexact=phone) or orderto.objects.filter(email__iexact=email):

			subject = 'Դուք չեք կարող գրանցվել'
			message = ' Դուք չեք կարող գրանցվել արդեն ' #simple
			return render(request, 'gitedu/index.html', {'err': 'Դուք արդեն գրանցված եք', 'show_err': True, 'subj': subject, 'mess': message})
		else:
			ordr = ordertoserv(name=name, last_name=lname, phone=phone, email=email, serv=serv, text=text)
			ordr.save()
			subject = 'Շնորհակալություն մեր ծառայություններից օգտվելու համար'
			message = ' Մեր մասնագետները դիտարկում են ձեր հայտը: '
			# email_from = settings.EMAIL_HOST_USER
			recipient_list = [email,]
			# send_mail( subject, message, email_from, recipient_list )
			subject = '{0} {1}-ը ուղարկել է ({2})-ի հայտ'.format(name, lname, serv)
			message = ''' Անուն - {0} {1}
			Էլ.փոստ - {2}
			Հեռախոսահամար - {3}
			Ծառայություն - {4}
			Մանրամասնությունները՝
			{5} '''.format(name, lname, email, phone, serv, text)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = ['gitedu@bk.ru',]
			send_mail( subject, message, email_from, recipient_list, fail_silently=False, )
		
			return render(request, 'gitedu/index.html', {'err': 'Ձեր հայտը ուղարկված է, մեր մասնագետները կկապնվեն ձեր թողած կոնտակտներով: Շնորհակալություն մեր ծառայություններից օգտվելու համար', 'show_err': True, 'subj': subject, 'mess': message})
