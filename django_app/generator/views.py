import os
import mimetypes
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .forms import GeneratorForm
from .models import Template

from .scripts.main import main

from django.conf import settings
from django.templatetags.static import static
import zipfile
# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def home(request):
    template = Template.objects.all()[0]
    path = settings.MEDIA_ROOT
    img_list = os.listdir(f"{path}/articles")
    context = {'template': template,'images' : img_list}
    return render(request, 'generator/index.html', context)

def upload(request):
    if request.method == 'POST':
        template_intro = str(request.POST.get('template_intro'))
        template_chapitres = str(request.POST.get('template_chapitres'))
        template_conclusion = str(request.POST.get('template_conclusion'))
        mots_cles = str(request.POST.get('mots_cles')).split('\n')
        # print(categories_redirections)
        google_check = bool(request.POST.get('google_check'))
        h3_check = bool(request.POST.get('h3_check'))

        # print('Googlecheck:h3check', google_check, h3_check)
        

        filenames = main(mot_cles=mots_cles, template_intro=template_intro, template_chapitres=template_chapitres, template_conclusion=template_conclusion, google_check=google_check, h3_check=h3_check)

        # filepath = BASE_DIR + '/scripts/' + filename
        # for filename, filepath in filenames.items():
        #     with open(filepath, 'r') as fh:
        #         mime_type, _ = mimetypes.guess_type(filepath)
        #         response = HttpResponse(fh.read(), content_type="mime_type")
        #         response['Content-Disposition'] = 'attachment; filename=' + str(filename).replace('\r', '')
        #         return response

        # render(request, 'open_csv/index.html', context)

        for filename, filepath in filenames.items():
            download(filename, filepath)

    return HttpResponse("Failed")
    
def download(filename, filepath):
    with open(filepath, 'r') as fh:
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(fh.read(), content_type="mime_type")
        response['Content-Disposition'] = 'attachment; filename=' + str(filename).replace('\r', '')
        return response
        
    # with zipfile.ZipFile('files.zip' , 'w') as my_zip:
    #     my_zip.write(filename)

    # remove the downloaded files
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # dir = BASE_DIR+"/upload"
    # for f in os.listdir(dir):
    #     os.remove(os.path.join(dir, f))

    # with open('upload/' + filename, 'wb+') as destination:
    #     for chunk in file.chunks():
    #         destination.write(chunk)