var stripe_public_key = $('#id_stripe_public_key').text.slice(1,-1);
var client_secret = $('#id_client_secret').text.slice(1,-1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#000'
        }
    },
    invalid: {
        color: '#F39C12',
        iconColor: '#F39C12'
    }
};
var card =elements.create(card);
card.mount('#card-element', {style: style});