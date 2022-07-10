from flask import abort

from kalpas import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    punches = db.relationship('Punch', backref='user', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }

    def from_dict(self, data, partial_update=True):
        for field in ['id', 'first_name', 'last_name', 'email']:
            try:
                setattr(self, field, data[field])
            except KeyError:
                if not partial_update:
                    abort(400)

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def load_roles(self, roles):
        """
        Load default roles
        """
        for role in roles:
            r = Role(name=role)
            db.session.add(r)
        db.session.commit()

    def to_dict(self):
        return {
            'role': self.name
        }


class Punch(db.Model):
    __tablename__ = "punches"

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        nullable=False)

    def to_dict(self):
        return {
            'time': self.time,
            'user_id': self.user_id
        }

    def __repr__(self):
        return f'<Punch {self.user_id} {self.time}>'
