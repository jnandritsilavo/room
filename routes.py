from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db, bcrypt
from models import User, Room, Reservation

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        role = request.form['role']
        new_user = User(username=username, email=email, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('Inscription réussie !', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Identifiants invalides', 'danger')
    return render_template('login.html')

@main.route('/dashboard')
@login_required
def dashboard():
    rooms = Room.query.all()
    reservations = Reservation.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', rooms=rooms, reservations=reservations)

@main.route('/logout')
def logout():
    logout_user()
    flash('Déconnexion réussie', 'success')
    return redirect(url_for('main.home'))


