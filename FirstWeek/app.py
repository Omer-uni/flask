
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

tickets = []

@app.route('/')
def index():
    return redirect(url_for('create_ticket'))

@app.route('/create', methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        priority = request.form['priority']
        subject = request.form['subject']
        message = request.form['message']
        file = request.files['file']

        filename = None
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        ticket = {
            'id': len(tickets) + 1,
            'name': name,
            'email': email,
            'priority': priority,
            'subject': subject,
            'message': message,
            'file': filename,
            'status': 'İnceleme Bekliyor'
        }
        tickets.append(ticket)
        return render_template('ticket_created.html', ticket=ticket)

    return render_template('create_ticket.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', tickets=tickets)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/ticket/<int:ticket_id>')
def ticket_detail(ticket_id):
    ticket = next((t for t in tickets if t['id'] == ticket_id), None)
    if not ticket:
        return "Ticket bulunamadı", 404
    return render_template('ticket_detail.html', ticket=ticket)

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

from flask import session

users = {}

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users:
            return "Bu kullanıcı zaten var!", 400
        users[email] = password
        session['user'] = email
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if users.get(email) == password:
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            return "Geçersiz kullanıcı adı veya şifre!", 401
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/ticket/<int:ticket_id>/edit', methods=['GET', 'POST'])
def edit_ticket(ticket_id):
    ticket = next((t for t in tickets if t['id'] == ticket_id), None)
    if not ticket:
        return "Ticket bulunamadı", 404

    if request.method == 'POST':
        ticket['subject'] = request.form['subject']
        ticket['message'] = request.form['message']
        ticket['status'] = request.form['status']
        return redirect(url_for('ticket_detail', ticket_id=ticket_id))

    return render_template('edit_ticket.html', ticket=ticket)

@app.route('/')
def index():
    return render_template('index.html')
