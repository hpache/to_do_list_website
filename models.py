from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class InfoModel(db.Model):

    __tablename__ = "info_table"

    id = db.Column(db.Integer, primary_key = True)
    item = db.Column(db.String())
    date = db.Column(db.String())
    priority = db.Column(db.String())
    tag = db.Column(db.String())


    def __init__(self, item, date, priority, tag) -> None:
        self.item = item
        self.date = date
        self.priority = priority
        self.tag = tag
    
    def __repr__(self) -> str:
        return f"{self.item}:{self.date, self.priority, self.tag}"