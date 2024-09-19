
from flask import Blueprint, render_template, request, redirect, url_for
from models.income import Income
from init_db import session  # Assuming session is set up in init_db.py

income_bp = Blueprint('income', __name__)

@income_bp.route('/')
def list_incomes():
    incomes = session.query(Income).all()
    return render_template('income_view.html', incomes=incomes)

@income_bp.route('/add', methods=['GET', 'POST'])
def add_income():
    if request.method == 'POST':
        aquarium_id = request.form['aquarium_id']
        date = request.form['date']
        designation = request.form['designation']
        amount = request.form['amount']
        supplier_id = request.form['supplier_id']
        notes = request.form['notes']
        new_income = Income(aquarium_id=aquarium_id, date=date, designation=designation,
                            amount=amount, supplier_id=supplier_id, notes=notes)
        session.add(new_income)
        session.commit()
        return redirect(url_for('income.list_incomes'))
    return render_template('add_income.html')

@income_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_income(id):
    income = session.query(Income).get(id)
    if request.method == 'POST':
        income.aquarium_id = request.form['aquarium_id']
        income.date = request.form['date']
        income.designation = request.form['designation']
        income.amount = request.form['amount']
        income.supplier_id = request.form['supplier_id']
        income.notes = request.form['notes']
        session.commit()
        return redirect(url_for('income.list_incomes'))
    return render_template('edit_income.html', income=income)

@income_bp.route('/delete/<int:id>', methods=['POST'])
def delete_income(id):
    income = session.query(Income).get(id)
    session.delete(income)
    session.commit()
    return redirect(url_for('income.list_incomes'))
