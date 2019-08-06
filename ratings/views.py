from django.shortcuts import render, redirect
from django.views.generic.base import View

from ratings.models import Rating
from ratings.forms import RatingForm


def home(request):
    """ Show the entry point to the ratings app
    :param request: Django request object
    :return: rendered homepage
    """
    form_object = RatingCreate  # RatingCreate view as object

    # If post request comes from 'Delete' button:
    #   delete selection
    # Else:
    #   use post reqeust to add selection from 'New' button
    if request.POST:
        if 'delete' in request.POST:
            rating_id = request.POST['delete']
            rating = Rating.objects.get(pk=rating_id)
            rating.delete()
            return redirect(home)
        else:
            print(request.POST)
            form = form_object.form_class(request.POST)
            if form.is_valid():
                _ = form.save()
                return redirect(home)
    
    form = form_object.form_class()

    context = {
        'ratings': Rating.objects.all(),
        'form': form,
        'title': form_object.title
    }
    return render(request, 'home.html', context)


class RatingCreate(View):
    """ Create a new Rating """
    form_class = RatingForm
    title = "Enter a new rating"
    template_name = 'ratings/rating_form.html'

class RatingEdit(View):
    """ Edit a Rating """
    form_class = RatingForm
    title = 'Edit rating'
    template_name = 'ratings/rating_form.html'

    # Get request to pre-populate form fields with current data values
    def get(self, request, rating_id):
        """ get request to pre-populate form items
        :param rating_id: ID of the beer rating to display
        :return: rendered homepage
        """
        rating = Rating.objects.get(pk=rating_id)
        form = self.form_class(initial={'beer_name': rating.beer_name, 'score': rating.score, 'notes': rating.notes, 'brewery': rating.brewery})
        context = {
            'form': form,
            'title': self.title
        }
        return render(request, self.template_name, context)

    def post(self, request, rating_id):
        """ post request to update beer rating entry
        :param rating_id: ID of the beer rating to update
        :return: rendered homepage
        """
        rating = Rating.objects.get(pk=rating_id)
        form = self.form_class(request.POST, instance=rating)

        # If cancel edit:
        #   return to home
        # Else:
        #   edit entry
        if "cancel" in request.POST:
            return redirect(home)
        else:
            if form.is_valid():
                _ = form.save()
                return redirect(home)
