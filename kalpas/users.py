from flask import (
    Blueprint,
    jsonify,
    request,
    abort,
    url_for
)
from .models import User
from kalpas import db

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.get("/<id>")
def get_user(id: str):
    """
    Get a user's information
    """
    user = User.query.filter_by(id=id).first()

    if user is None:
        abort(404)

    return jsonify({'user': user.to_dict()})


@bp.get("/")
def get_users():
    """
    Get a user's information
    """
    users = User.query.all()
    return jsonify({'users': [e.to_dict() for e in users]})


@bp.post("/")
def add_user():
    """
    Add an user
    """
    user = User()
    user.from_dict(request.get_json(), partial_update=False)
    if User.query.filter_by(id=user.id).first() is not None:
        abort(400)
    db.session.add(user)
    db.session.commit()
    r = jsonify(user.to_dict())
    r.status_code = 201
    r.headers['Location'] = url_for('users.get_user', id=user.id)

    return r
