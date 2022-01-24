from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe

@require_POST
@csrf_exempt
def webhook(request):
    """ Listen for stripe's webhooks """
    """ Setup """
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    """ Get webhook data and verify signature """
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhok.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        """ Invaliid payload """
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        """ Invalid Signature """
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    print('Success')
    return HttpResponse(status=200)
