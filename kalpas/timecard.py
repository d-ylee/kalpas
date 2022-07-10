# import datetime

from flask import (
    Blueprint
)

bp = Blueprint('timecard', __name__, url_prefix='/timecard')


@bp.get("/punch/<id>")
def punch(id: str):
    """
    Add a punch at with current time for a user ID
    """
    print(id)
    pass


@bp.get("/times")
def get_times():
    """
    Get all times
    """
    return ''


@bp.get("/times/<id>")
def get_user_times(id: str):
    """
    Get the times for a specific user
    """
    print(id)

    return ''

