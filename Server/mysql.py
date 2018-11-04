from flask_sqlalchemy import SQLAlchemy
from Server import app

db = SQLAlchemy(app)

class Base(db.Model):

    __abstract__ = True

    @property
    def serialize(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

    def serialize_list(self, items):
        return [item.serialize for item in items]


class Site(Base):

    __tablename__ = 'site'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    url = db.Column(db.String(200), primary_key=True)
    count = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    check = db.Column(db.Boolean)

    def __init__(self, url, count, time, check):
        self.url = url
        self.count = count
        self.check = check
        self.time = time

    @property
    def serialize(self):
        return {
            'count' : self.count,
            'url' : self.url,
            'time' : self.time,
            'check' : self.check
        }

    def serialize_list(self, items):
        return [item.serialize for item in items]