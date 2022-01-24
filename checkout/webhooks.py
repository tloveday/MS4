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
        event = stripe.Webhook.construct_event(
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

    """ Set Up Webhook handler """
    handler = StripeWH_Handler(request)

    """ Map Webhooks to relevant handlers """
    event_map = {
        'payment_intent.succeeded' : handler.handle_payment_intent_succeeded
        'payment_intent.payment_failed' : handler.handle_payment_intent_payment_failed(event)
    }

    """ Attain Webhook from Stripe """
    event_type = event['type']

    """ If handler exsists get it from map. """
    event_handler = event_map.get(event_type, handler.handle_event

    """ Call the event handler with the event """
    response = event_handler(event)
    return response 