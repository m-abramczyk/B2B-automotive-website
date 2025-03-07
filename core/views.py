from django.utils.translation import gettext as _
from django.shortcuts import render


#////////////////////////////////////////////////////
# Home Page
def home_page(request):

    context = {
    }

    return render(request, 'index.html', context)

def contact_page(request):

    context = {

    }

    return render(request, 'page-contact.html', context)