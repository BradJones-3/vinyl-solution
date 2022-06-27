from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Strip Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handles genric/unknown and unexpected webhook events"""
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_successful(self, event):
        """Handles payment intent succeeded webhook from Stripe"""
        intent = event.data.object
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handles payment intent failed webhook from Stripe"""
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
