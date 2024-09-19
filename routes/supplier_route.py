
from flask import Blueprint, render_template, request, redirect, url_for
from models.supplier import Supplier
from init_db import session  # Assuming session is set up in init_db.py

supplier_bp = Blueprint('supplier', __name__)

@supplier_bp.route('/')
def list_suppliers():
    suppliers = session.query(Supplier).all()
    return render_template('supplier_view.html', suppliers=suppliers)

@supplier_bp.route('/add', methods=['GET', 'POST'])
def add_supplier():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        address2 = request.form['address2']
        postal_code = request.form['postal_code']
        city = request.form['city']
        country = request.form['country']
        phone = request.form['phone']
        email = request.form['email']
        website = request.form['website']
        contact1 = request.form['contact1']
        contact2 = request.form['contact2']
        notes = request.form['notes']
        visibility = request.form.get('visibility') == 'on'
        new_supplier = Supplier(name=name, address=address, address2=address2, postal_code=postal_code,
                          city=city, country=country, phone=phone, email=email, website=website,
                          contact1=contact1, contact2=contact2, notes=notes, visibility=visibility)
        session.add(new_supplier)
        session.commit()
        return redirect(url_for('supplier.list_suppliers'))
    return render_template('add_supplier.html')

@supplier_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_supplier(id):
    supplier = session.query(Supplier).get(id)
    if request.method == 'POST':
        supplier.name = request.form['name']
        supplier.address = request.form['address']
        supplier.address2 = request.form['address2']
        supplier.postal_code = request.form['postal_code']
        supplier.city = request.form['city']
        supplier.country = request.form['country']
        supplier.phone = request.form['phone']
        supplier.email = request.form['email']
        supplier.website = request.form['website']
        supplier.contact1 = request.form['contact1']
        supplier.contact2 = request.form['contact2']
        supplier.notes = request.form['notes']
        supplier.visibility = request.form.get('visibility') == 'on'
        session.commit()
        return redirect(url_for('supplier.list_suppliers'))
    return render_template('edit_supplier.html', supplier=supplier)

@supplier_bp.route('/delete/<int:id>', methods=['POST'])
def delete_supplier(id):
    supplier = session.query(Supplier).get(id)
    session.delete(supplier)
    session.commit()
    return redirect(url_for('supplier.list_suppliers'))
