from django.http import HttpResponse
from reportlab.pdfgen import canvas
import datetime

def my_image(request):
	image_data = open("/media/NITYANANDA/bhagwan/Gurumaharaj.jpg", "rb").read()
	return HttpResponse(image_data, mimetype="image/jpg")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>this is now %s</body></html>" %now
	return HttpResponse(html)
	
def home(request):
	return HttpResponse("Hare krsna")
def hello(request):
	return HttpResponse("Hare krsna")
	
def hello_pdf(request):
	response = HttpResponse(mimetype='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=hello.pdf'
	p = canvas.Canvas(response)
	p.drawString(100, 100, "Hare-Krishna")
	p.showPage()
	p.save()
	return response
	
from cStringIO import StringIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
def hello_pdf(request):
	response = HttpResponse(mimetype="application/pdf")
	response['Content-Disposition']= 'attachment; filename=hello.pdf'
	temp = StringIO()
	p= canvas.Canvas(temp)
	p.drawString(100, 100, "Hare-Krishna")
	p.showPage()
	p.save()
	return response
