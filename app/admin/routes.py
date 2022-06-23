from flask import url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from app import db
from app.admin import bp
from app.admin.models import CustomerServiceView
from app.models import User


@bp.route('/')
@bp.route('index')
@login_required
def admin():
    if current_user.is_authenticated:
        if current_user.username == 'VadimM':
            return CustomerServiceView(User, db.session).render('index.html')
        return redirect(url_for('main.index'))
    return redirect(url_for('auth.login'))

#
# @admin.route('/list')
# @login_required
# def admin_list():
#     return render_template('list.html')

# @app.route('/schedule/add', methods=['GET', 'POST'])
# def edit_time_options():
#     if request.method == 'POST':
#         time_choices = request.form.getlist('time_checkbox')
#         time_select_form = UserView()
#         time_select_form.service_time.choices = time_choices
#         flash(f'New time choices {time_choices} was added')
