from django.shortcuts import render

from match.forms import AddMatchForm
# Create your views here.

def add_match(request):
    form = AddMatchForm(request.POST or None)
    if request.method == 'POST':
    	if form.is_valid():
            obj = form.save()
            print("obj ++++++++++++++++++++++++++++++++++")
            print(obj)
            company_and_user_obj = UsersWithRolesInCompany.objects.get_or_create(user=user)
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('registration/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            messages.add_message(request, messages.SUCCESS, "We have sent you an email, please confirm your email address to complete registration!.")
            return redirect("login")
    else:
        form = AddMatchForm()
    return render(request, 'match/add.html', {'form': form})



