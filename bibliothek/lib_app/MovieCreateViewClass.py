from django.views.generic.edit import CreateView
from .models import Film  # Import the Film model from your app

class MovieCreateView(CreateView):
    model = Film  # Specify the model for the view
    fields = ['title', 'director', 'FSK', 'IMDb', 'genre', 'language', 'description', 'cover_image', 'release_year']  # Define the fields to be displayed in the form
    template_name = 'movie_form.html'  # Specify the template for the form (replace with your actual template name)

    def form_valid(self, form):
        # Add any additional processing or validation logic here
        return super().form_valid(form)

