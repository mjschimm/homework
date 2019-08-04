from django.shortcuts import render, redirect
from django.views.generic.base import View

from ratings.models import Rating
from ratings.forms import RatingForm


def home(request):
    """ Show the entry point to the ratings app
    :param request: Django request object
    :return: rendered homepage
    """
    
    form_object = RatingCreate

    """
        If post request comes from a delete button:
            delete selection
        Else:
            use post reqeust to add selection
    """
    if request.POST:
        if 'delete' in request.POST:
            rating_id = request.POST['delete']
            rating = Rating.objects.get(pk=rating_id)
            rating.delete()
            return redirect(home)
        else:
            form = form_object.form_class(request.POST)
            if form.is_valid():
                _ = form.save()
                return redirect(home)
    
    form = form_object.form_class()

    context = {
        'ratings': Rating.objects.all(),
        'form': form,
    }
    return render(request, 'home.html', context)


class RatingCreate(View):
    """ Create a new Rating """
    form_class = RatingForm
    template_name = 'ratings/rating_form.html'

    # def get(self, request):
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form': form})

    # def post(self, request):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         _ = form.save()
    #         return redirect(home)
    #     return render(request, self.template_name, {'form: form'})


class RatingEdit(View):
    """ Edit a Rating """
    form_class = RatingForm
    template_name = 'ratings/rating_edit_form.html'

    def get(self, request, rating_id):
        rating = Rating.objects.get(pk=rating_id)
        form = self.form_class(initial={'beer_name': rating.beer_name, 'score': rating.score, 'notes': rating.notes, 'brewery': rating.brewery})
        return render(request, self.template_name, {'form': form})

    def post(self, request, rating_id):
        rating = Rating.objects.get(pk=rating_id)
        form = self.form_class(request.POST, instance=rating)
        if "cancel" in request.POST:
            return redirect(home)
        else:
            if form.is_valid():
                _ = form.save()
                return redirect(home)
        return render(request, self.template_name, {'form: form'})

