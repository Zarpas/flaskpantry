import datetime, re

from app import db


def slugify(s):
	return re.sub('[^\w]+', '-', s).lower()


class Estanteria(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(20))
	descripcion = db.Column(db.String(100))
	fuera_de_uso = db.Column(db.Boolean)

	def __init__(self, *args, **kwargs):
		super(Estanteria, self).__init__(*args, **kwargs)   # Call parent constructor

	def __repr__(self):
		return '<Estanteria: %s>' % self.nombre

	alimento = db.relationship('Alimento', backref=db.backref('estanteria', lazy='joined'))


class Producto(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(40))
	descripcion = db.Column(db.String(100))
	unidad = db.Column(db.String(10))

	def __init__(self, *args, **kwargs):
		super(Producto, self).__init__(*args, **kwargs)

	def __repr__(self):
		return '<Producto: %s>' % self.nombre

	alimento = db.relationship('Alimento', backref=db.backref('producto', lazy='joined'))


class Alimento(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	estante_ref = db.Column(db.Integer, db.ForeignKey('estanteria.id'))
	producto_ref = db.Column(db.Integer, db.ForeignKey('producto.id'))
	cantidad = db.Column(db.Float)
	caducidad = db.Column(db.Date)
	estado = db.Column(db.String(20))

	def __init__(self, *args, **kwargs):
		super(Alimento, self).__init__(*args, **kwargs)

	def __repr__(self):
		return '<Alimento: %s>' % self.producto