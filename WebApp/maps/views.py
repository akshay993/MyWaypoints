from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.generic import TemplateView
from maps.inputform import InputForm
from django.http import HttpResponseRedirect



#def index(request):
#    if request.method == "GET":
#        return render(request, 'maps/index.html', context=None)
#    if request.method == "GET":
#        return render(request, 'maps/map.html', context=None)

class HomeView(TemplateView):
    template_name = 'maps/index.html'

    def get(self, request):
        form = InputForm()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):

        form = InputForm(request.POST)

        if form.is_valid():
            start = form.cleaned_data['Start']
            destination = form.cleaned_data['End']

            #return HttpResponseRedirect('/search/')

        args = {'form': form, 'start': start, 'End': destination}
        return render(request, self.template_name, args)


def search(request):
    return render(request, 'maps/map.html', context=None)




