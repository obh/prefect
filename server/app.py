from flask import Flask, request, jsonify
from db import db
from flask_injector import FlaskInjector
from models import models
from injector import inject
from datetime import datetime

app = Flask(__name__)


@app.route('/client', methods=['POST'])
@inject
def add_client(db_conn: db.Database) -> jsonify:
    json = request.get_json()
    provider = json.get('provider')
    if provider == 'cashfree':
        provider = models.Provider.Cashfree
    elif provider == 'razorpay':
        provider = models.Provider.Razorpay
    else:
        return jsonify({'error': 'Invalid provider'}), 400

    credentials = json.get('credentials')
    missing_fields = [field for field in models.ProviderFields[provider] if field not in credentials]
    if missing_fields:
        return jsonify({'error': f'Missing fields: {missing_fields}'}), 400

    now = datetime.now()
    client = models.CredEntry(provider=provider, client_id=json.get("client_id"), credentials=credentials,
                              status=models.Status.INACTIVE, added_on=now, updated_on=now)
    db_conn.add_client(client=client)
    return jsonify({'message': 'Client added'}), 200


@app.route('/providers', methods=['GET'])
def get_providers() -> jsonify:
    return models.ProviderFields


def configure(binder):
    binder.bind(
        db.Database,
        to=db.MySqlDatabase(),
        scope=request,
    )


if __name__ == '__main__':
    FlaskInjector(app=app, modules=[configure])
    app.run(port=2345)
