from django.shortcuts import render
from base_app.models import Test
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound


def reg_auth(request):
    if request.method == 'POST':
        if "regButton" in request.POST:
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
                print(34324)
                # Create a new user object but avoid saving it yet
                new_user = user_form.save(commit=False)
                # Set the chosen password
                new_user.set_password(user_form.cleaned_data['password'])
                # Save the User object
                new_user.save()
                return HttpResponseRedirect('/account')
        if "authButton" in request.POST:

            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:

                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    return HttpResponseRedirect('/my-tests')
                else:
                    # Return a 'disabled account' error message
                    ...
            else:
                # Return an 'invalid login' error message.
                ...
    return render(request, 'account_app/registration/reg_auth.html')
