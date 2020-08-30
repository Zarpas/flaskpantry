from flask import render_template, redirect, request, url_for

from helpers import object_list

from app import app, db
from models import Estanteria, Producto, Alimento
from forms import EstanteriaForm, ProductoForm, AlimentoForm


@app.route('/')
def homepage():
	return render_template('index.html')


@app.route('/estanteria/') # ok
def list_estanteria():
	estanterias =  Estanteria.query.order_by(Estanteria.nombre)
	return object_list('estanteria/index.html', estanterias)

@app.route('/estanteria/<id>') # ok
def detail_estanteria(id):
	estanteria = Estanteria.query.get(id)
	return render_template('estanteria/detail.html', estanteria=estanteria)

@app.route('/estanteria/new/', methods=['GET', 'POST']) # ok
def new_estanteria():
	if request.method == 'POST':
		form = EstanteriaForm(request.form)
		if form.validate():
			estanteria = form.save_entry(Estanteria())
			db.session.add(estanteria)
			db.session.commit()
			return redirect(url_for('detail_estanteria', id=estanteria.id))
	else:
		form = EstanteriaForm()

	return render_template('estanteria/new.html', form=form)

@app.route('/estanteria/<id>/edit', methods=['GET', 'POST']) # ok
def edit_estanteria(id):
	estante = Estanteria.query.filter(Estanteria.id == id).first_or_404()
	if request.method == 'POST':
		form = EstanteriaForm(request.form, obj=estante)
		if form.validate():
			estante = form.save_entry(estante)
			db.session.add(estante)
			db.session.commit()
			return redirect(url_for('detail_estanteria', id=estante.id))
	else:
		form = EstanteriaForm(obj=estante)

	return render_template('estanteria/edit.html', estante=estante, form=form)

@app.route('/estanteria/<id>/delete', methods=['GET', 'POST']) # ok
def delete_estanteria(id):
	estanteria = Estanteria.query.filter(Estanteria.id == id).one()
	if request.method == 'POST':
		db.session.delete(estanteria)
		db.session.commit()
		return redirect('/estanteria/')  #url_for(list_estanteria))
	
	return render_template('estanteria/delete.html', estanteria=estanteria)


@app.route('/producto/')
def list_producto():
	productos =  Producto.query.order_by(Producto.nombre)
	return object_list('producto/index.html', productos)

@app.route('/producto/<id>') # ok
def detail_producto(id):
	producto = Producto.query.get(id)
	return render_template('producto/detail.html', producto=producto)

@app.route('/producto/new/', methods=['GET', 'POST']) # ok
def new_producto():
	if request.method == 'POST':
		form = ProductoForm(request.form)
		if form.validate():
			producto = form.save_entry(Producto())
			db.session.add(producto)
			db.session.commit()
			return redirect(url_for('detail_producto', id=producto.id))
	else:
		form = ProductoForm()

	return render_template('producto/new.html', form=form)

@app.route('/producto/<id>/edit', methods=['GET', 'POST']) # ok
def edit_producto(id):
	producto = Producto.query.filter(Producto.id == id).first_or_404()
	if request.method == 'POST':
		form = ProductoForm(request.form, obj=producto)
		if form.validate():
			producto = form.save_entry(producto)
			db.session.add(producto)
			db.session.commit()
			return redirect(url_for('detail_producto', id=producto.id))
	else:
		form = ProductoForm(obj=producto)

	return render_template('producto/edit.html', producto=producto, form=form)

@app.route('/producto/<id>/delete', methods=['GET', 'POST']) # ok
def delete_producto(id):
	producto = Producto.query.filter(Producto.id == id).one()
	if request.method == 'POST':
		db.session.delete(producto)
		db.session.commit()
		return redirect(url_for(list_producto))
	
	return render_template('producto/delete.html', producto=producto)


@app.route('/alimento/')
def list_alimento():
	alimentos =  Alimento.query.order_by(Alimento.producto_ref)
	return object_list('alimento/index.html', alimentos)

@app.route('/alimento/<id>') # ok
def detail_alimento(id):
	alimento = Alimento.query.get(id)
	return render_template('alimento/detail.html', alimento=alimento)

@app.route('/alimento/new/', methods=['GET', 'POST']) # ok
def new_alimento():
	if request.method == 'POST':
		form = AlimentoForm(request.form)
		if form.validate():
			alimento = form.save_entry(Alimento())
			db.session.add(alimento)
			db.session.commit()
			return redirect(url_for('detail_alimento', id=alimento.id))
	else:
		form = AlimentoForm()

	return render_template('alimento/new.html', form=form)

@app.route('/alimento/<id>/edit', methods=['GET', 'POST']) # ok
def edit_alimento(id):
	alimento = Alimento.query.filter(Alimento.id == id).first_or_404()
	if request.method == 'POST':
		form = AlimentoForm(request.form, obj=alimento)
		if form.validate():
			producto = form.save_entry(alimento)
			db.session.add(alimento)
			db.session.commit()
			return redirect(url_for('detail_alimento', id=alimento.id))
	else:
		form = AlimentoForm(obj=alimento)

	return render_template('alimento/edit.html', alimento=alimento, form=form)

@app.route('/alimento/<id>/delete', methods=['GET', 'POST']) # ok
def delete_alimento(id):
	alimento = Alimento.query.filter(Alimento.id == id).one()
	if request.method == 'POST':
		db.session.delete(alimento)
		db.session.commit()
		return redirect(url_for(homepage))
	
	return render_template('alimento/delete.html', alimento=alimento)