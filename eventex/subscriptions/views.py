from django.views.generic import DetailView

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.mixins import EmailCrCreateView
from eventex.subscriptions.models import Subscription

new = EmailCrCreateView.as_view(model=Subscription,
                                form_class=SubscriptionForm,
                                email_subject='Confirmacão de inscricão')

detail = DetailView.as_view(model=Subscription)
