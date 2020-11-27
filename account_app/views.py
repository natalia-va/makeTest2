from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from django.http import HttpResponseRedirect, HttpResponseNotFound



def logout_user(request):
    logout(request)
    return render(request, 'account_app/registration/logged_out.html')

def reg_auth(request):
    if request.method == 'POST':
        if "regButton" in request.POST:
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
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
