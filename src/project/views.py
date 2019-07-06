from flask import Blueprint, request, jsonify
from project.models import Delivery
from project import db
from project.users import get_user


blueprint = Blueprint('routes', __name__)


@blueprint.route('/')
def index():
    return '<h1>Hello World!</h1>'


@blueprint.route('/deliveries')
@get_user
def list(user):
    deliveries = Delivery.query.filter_by(user_id=user.id).all()

    return jsonify(
        [delivery_to_dict(delivery) for delivery in deliveries]), 200


@blueprint.route('/deliveries', methods=['POST'])
@get_user
def create(user):
    data = request.get_json()

    delivery = Delivery(
        description=data.get('description'),
        status='En Curso',
        user_id=user.id)

    db.session.add(delivery)
    db.session.commit()

    return jsonify(delivery_to_dict(delivery))


def delivery_to_dict(delivery):
    return {
        'id': delivery.id,
        'description': delivery.description,
        'status': delivery.status,
        'creation': delivery.creation
    }
