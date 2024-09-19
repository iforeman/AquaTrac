
from flask import Blueprint, render_template, request, redirect, url_for
from models.expense import Expense
from init_db import session  # Assuming session is set up in init_db.py

expense_bp = Blueprint('expense', __name__)

@expense_bp.route('/')
def list_expenses():
    expenses = session.query(Expense).all()
    return render_template('expense_view.html', expenses=expenses)

@expense_bp.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        aquarium_id = request.form['aquarium_id']
        date = request.form['date']
        item = request.form['item']
        category = request.form['category']
        supplier_id = request.form['supplier_id']
        unit_price = request.form['unit_price']
        quantity = request.form['quantity']
        total = request.form['total']
        notes = request.form['notes']
        new_expense = Expense(aquarium_id=aquarium_id, date=date, item=item, category=category,
                              supplier_id=supplier_id, unit_price=unit_price, quantity=quantity,
                              total=total, notes=notes)
        session.add(new_expense)
        session.commit()
        return redirect(url_for('expense.list_expenses'))
    return render_template('add_expense.html')

@expense_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    expense = session.query(Expense).get(id)
    if request.method == 'POST':
        expense.aquarium_id = request.form['aquarium_id']
        expense.date = request.form['date']
        expense.item = request.form['item']
        expense.category = request.form['category']
        expense.supplier_id = request.form['supplier_id']
        expense.unit_price = request.form['unit_price']
        expense.quantity = request.form['quantity']
        expense.total = request.form['total']
        expense.notes = request.form['notes']
        session.commit()
        return redirect(url_for('expense.list_expenses'))
    return render_template('edit_expense.html', expense=expense)

@expense_bp.route('/delete/<int:id>', methods=['POST'])
def delete_expense(id):
    expense = session.query(Expense).get(id)
    session.delete(expense)
    session.commit()
    return redirect(url_for('expense.list_expenses'))
