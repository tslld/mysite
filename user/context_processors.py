from .forms import LoginForm


def login_modal_form(request):
    return {'cd login_modal_form': LoginForm()}
