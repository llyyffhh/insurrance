from flask import request, render_template, redirect, url_for, session, current_app, g, abort
from app.api import Api
from app.application import user_bp as bp
from app.application.models import User, db
from app.application.wtf.user_wtf import LoginForm, ResetPwdForm, AddUserForm
from app.libs.login import login_required
from app.libs.permission import permission_required

@bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            login_name = form.login_name.data
            password = form.password.data
            remember = form.remember.data
            user = User.query.filter_by(login_name=login_name).first()
            if user and user.check_pwd(password):
                session[current_app.config['USER_ID']] = user.id
                if remember:
                    session.permanent = True
                return Api.success()
            else:
                return Api.params_error(msg='用户名或密码错误,请重新输入')

        else:
            return Api.params_error(msg=form.get_error)

@bp.route('/logout')
@login_required
def logout():
    session.pop(current_app.config['USER_ID'])
    return redirect(url_for('user.login'))

@bp.route('/reset_pwd',methods=['GET','POST'])
@login_required
def reset_pwd():
    if request.method == 'GET':
        return render_template('cms_resetpwd.html')
    else:
        form = ResetPwdForm(request.form)
        if form.validate():
            old_pwd = form.old_pwd.data
            new_pwd = form.new_pwd.data
            user = g.cms_user
            if user.check_pwd(old_pwd):
                user.password = new_pwd
                db.session.commit()
                return Api.success()
            else:
                return Api.params_error(msg='旧密码错误!')
        else:
            return Api.params_error(msg=form.get_error)


@bp.route('/profile')
@login_required
def profile():
    return render_template('cms_profile.html')


@bp.route('/cms_users')
@login_required
@permission_required
def cms_user():
    users = User.query.all()
    context = {'users':users}
    return render_template('cms_cmsusers.html',**context)


@bp.route('/add_user',methods=['GET','POST'])
@login_required
@permission_required
def add_user():
    if request.method == "GET":
        return render_template('cms_addcmsuser.html')
    else:
        form = AddUserForm(request.form)
        if form.validate():
            login_name = form.login_name.data
            name = form.name.data
            user = User(login_name=login_name,name=name)
            user.password = '123456'
            db.session.add(user)
            db.session.commit()
            return Api.success()
        else:
            return Api.params_error(form.get_error)

@bp.route('/edit_user',methods=['GET','POST'])
@login_required
@permission_required
def edit_user():
    user_id = request.args.get('user_id')
    if request.method == 'GET':
        if not user_id:
            abort(404)
        user = User.query.get(user_id)
        context = {'user':user}
        return render_template('/cms_editcmsuser.html',**context)
    else:
        permission = request.form.get('permission')
        if permission:
            user = User.query.get(user_id)
            user.permission = '管理员' if permission =='1' else '操作员'
            db.session.commit()
            return Api.success()
        else:
            return Api.params_error(msg='没有相应的权限')

@bp.route('/del_user',methods=['GET','POST'])
@login_required
@permission_required
def del_user():
    user_id = request.args.get('user_id')
    if not user_id:
        abort(404)
    user = User.query.get(user_id)
    try:
        db.session.delete(user)
        db.session.commit()
        return Api.success()
    except:
        db.session.rollback()
        return Api.unauth_error(msg='无法删除此用户')





# @bp.route('/register')
# def register():
#     user = User(login_name='liyan',name='李岩',permission='管理员')
#     user.password = '123456'
#     db.session.add(user)
#     db.session.commit()
#     return 'success'


