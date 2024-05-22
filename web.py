from flask import Flask, render_template, request, redirect, url_for, flash
from web_config import db
from web_db import Complaintone

app = Flask(__name__)
app.config['SECRET_KEY'] = '40685579'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Compliantformone.db'
db.init_app(app)

@app.route('/compliant_form', methods=['GET', 'POST'])
def com_send_message():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_id = request.form['user_id']
        user_email = request.form['user_email']
        user_phone = request.form['user_phone']
        user_selector = request.form['user_selector']
        user_mail_one = request.form['user_mail_one']


        if not user_name or not user_id or not user_email or not user_phone or not user_selector or not user_mail_one:
            flash('Please fill out all fields')
            return redirect(url_for('com_send_message'))

        new_complaint = Complaintone(
            user_name=user_name,
            user_id=user_id,
            user_email=user_email,
            user_phone=user_phone,
            user_selector=user_selector,
            user_mail_one=user_mail_one
        )

        try:
            db.session.add(new_complaint)
            db.session.commit()
            flash('Complaint submitted successfully!')
            return redirect(url_for('com_send_message'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error submitting complaint: {e}')
            return redirect(url_for('com_send_message'))

    return render_template('compliant_form.html')

if __name__ == '__main__':
    app.run(debug=True)
