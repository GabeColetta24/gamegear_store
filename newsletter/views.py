from django.shortcuts import render, redirect
from .forms import NewsletterSignupForm


# Newsletter signup view
# Allows users to submit their email address for marketing updates
def newsletter_signup(request):

    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = NewsletterSignupForm()

    context = {
        'form': form,
    }

    return render(request, 'newsletter/newsletter_signup.html', context)