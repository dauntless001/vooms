from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.forms import forms, ModelForm
from django.http import HttpResponseRedirect
from django.views.generic import CreateView


class CssForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs["placeholder"] = field.label

            if field.widget.attrs.get("class"):
                field.widget.attrs["class"] += " form-control"
            else:
                field.widget.attrs["class"] = "form-control"



def contact_form_mailer(view: CreateView, form: ModelForm):
    contact = form.save()

    send_mail(
        from_email=contact.email,
        subject=contact.subject,
        message=contact.message,
        recipient_list=[settings.DEFAULT_FROM_EMAIL],
        fail_silently=True
    )

    messages.success(view.request, "Message sent successfully")
    return HttpResponseRedirect(view.request.path_info)
