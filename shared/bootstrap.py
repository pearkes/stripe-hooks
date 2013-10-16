from .app import app
from shared.helpers import jsonify_with_status
from web.hook import hook
import stripe

app.register_blueprint(hook, url_prefix='/webhook')


@app.errorhandler(404)
def page_not_found(error):
    return jsonify_with_status(404, {"error": "resource not found"})

# Configurat stripe
stripe.api_key = app.config.get('STRIPE_KEY')
