from flask_wtf import Form
from wtforms import StringField, FileField, TextAreaField
from wtforms.validators import DataRequired, regexp
from photolog import db

class ImageForm(Form):
    name = StringField("Nome", validators=[DataRequired()])
    description = TextAreaField("Descrição")
    image = FileField("Imagem", validators=[DataRequired() ])
    tags = StringField("Tags")



class ImageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(2048))
    filename = db.Column(db.String(200), unique=True)
    tags = db.Column(db.String(1024))

    def __init__(self, name, description, filename, tags):
        self.name = name
        self.description = description
        self.filename = filename
        self.tags = tags

    def __repr__(self):
        return '<Image %r>' % self.name