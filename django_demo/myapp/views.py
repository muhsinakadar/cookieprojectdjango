from django.http import HttpResponse

# Create your views here.
def index(request):
    if 'count' in request.COOKIES:
        count=int(request.COOKIES['count'])
        output="<h2 style='color:blue;'>Hi, you are visiting this page "+str(count)+" times before...</h2>"
        count=count+1
    else:
        output="<h2 style='color:red;'>Welcome... You are visiting this page for the first time...</h2>"
        count=1
    response=HttpResponse(output)
    response.set_cookie('count',str(count))
    return response
