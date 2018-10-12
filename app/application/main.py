from flask import render_template, g, request,jsonify
from app.application.ViewModle.insurance import QueryModel, todayModel,historyModel
from app.application.models import db
from app.api import Api
from app.application.ViewModle.insurance import QueryModel
from app.application.models.insurance import Raw_data,Insurance
from app.application import main_bp as bp
from app.application.wtf.main_wtf import AddDataForm, EditForm
from app.libs.login import login_required
from datetime import date, datetime


@bp.route('/')
@login_required
def index():
    today_data = Insurance.today_data()
    return render_template('cms_index.html',**today_data)

@bp.route('/work',methods=['GET','POST'])
@login_required
def work():
    query_result = QueryModel()
    if request.method == 'GET':
        return render_template('work.html')
    else:
        query_name = request.json.get('name').strip('')
        query_num = request.json.get('num').strip('')
        if query_num:
            result = Raw_data.query.filter_by(num_id=query_num).all()
            return jsonify(query_result.api(result))
        elif query_name:
            result = Raw_data.query.filter_by(name=query_name).all()
            return jsonify(query_result.api(result))
        else:
            return Api.params_error(msg='参数错误')

@bp.route('/add_data',methods=['POST'])
@login_required
def add_data():
    form = AddDataForm(request.form)
    if form.validate():
        name = form.name.data.strip()
        num = form.num.data.strip()
        money = form.money.data.strip()
        tel = form.tel.data.strip()
        low = form.low.data
        query_data = Insurance.query.filter_by(num_id=num).first()
        if not query_data:
            new_insurance = Insurance(name=name,num_id=num,money=money,telephone=tel,new=1,low=low)
            try:
                db.session.add(new_insurance)
                db.session.commit()
                return Api.success('添加数据成功')
            except Exception as e:
                db.session.rollback()
                return Api.params_error(msg='数据输入有误')
        else:
            date = str(query_data.join_time).split(' ')[0]
            return Api.params_error(msg='该客户已缴费，不能重复缴费，缴费日期为{}'.format(date))
    else:
        return Api.params_error(msg=form.get_error)

@bp.route('/pay',methods=['post'])
@login_required
def pay():
    form = AddDataForm(request.form)
    if form.validate():
        name = form.name.data.strip()
        num = form.num.data.strip()
        money = form.money.data.strip()
        tel = form.tel.data.strip()
        low = QueryModel.low(form.low.data)
        raw_data = Raw_data.query.filter_by(num_id=num).first()
        query_data = Insurance.query.filter_by(num_id=num).first()
        if not query_data:
            new_insurance = Insurance(name=name, num_id=num, money=money, telephone=tel, new=0, low=low)
            try:
                raw_data.state = '1'
                db.session.add(new_insurance)
                db.session.commit()

                return Api.success('缴费成功')
            except Exception as e:
                db.session.rollback()
                return Api.params_error(msg='数据输入有误')
        else:
            date = str(query_data.join_time).split(' ')[0]
            return Api.params_error(msg='该客户已缴费，不能重复缴费，缴费日期为{}'.format(date))
    else:
        return Api.params_error(msg=form.get_error)

@bp.route('/today_detail',methods=["POST"])
@login_required
def today_detail():
    parse_result = todayModel()
    today = date.today()
    result = Insurance.query.filter_by(join_time=today).all()
    query_result = parse_result.api(result)
    return jsonify(query_result)

@bp.route('/history',)
@login_required
def history():
    return render_template('history.html')

@bp.route('/history_detail',methods=['POST'])
@login_required
def history_detail():
    name = request.json.get('name').strip('')
    num = request.json.get('num').strip('')
    date = request.json.get('date')
    if date:
       date = datetime.strptime(request.json.get('date'), '%Y-%m-%d')
    else:
       date = ''
    parse_data = historyModel()
    result = parse_data.api(Insurance.history_data(name=name,num=num,date=date))
    return jsonify(result)

@bp.route('/delete',methods=['POST'])
@login_required
def delete():
    name = request.form.get('name')
    num = request.form.get('num')
    result1 = Insurance.query.filter_by(num_id=num).first()
    result2 = Insurance.query.filter_by(name=name).first()
    if result1:
        raw_data1 = Raw_data.query.filter_by(num_id=num).first()
        if raw_data1:
            raw_data1.state = '0'
        db.session.delete(result1)
        db.session.commit()
        return Api.success('删除成功!')
    elif result2:
        raw_data2 = Raw_data.query.filter_by(name=name).first()
        if raw_data2:
            raw_data2.state = '0'
        db.session.delete(result2)
        db.session.commit()
        return Api.success('删除成功!')
    else:
        return Api.params_error(msg='没有此信息')


@bp.route('/edit',methods=['POST'])
@login_required
def edit():
    form = EditForm(request.form)
    if form.validate():
        raw_name = form.raw_name.data
        raw_num = form.raw_num.data
        raw_tel = form.raw_tel.data
        raw_money = form.raw_money.data
        raw_low = QueryModel.low(form.raw_low.data)

        new_name = form.name.data
        new_num = form.num.data
        new_tel = form.tel.data
        new_money = form.money.data
        new_low = form.low.data

        raw_data = db.session.query(Insurance).filter(Insurance.name==raw_name,
                                           Insurance.num_id==raw_num,
                                           Insurance.money==raw_money,
                                           Insurance.telephone==raw_tel,
                                           Insurance.low==raw_low).first()
        if raw_data:
            raw_data.name = new_name
            raw_data.num_id = new_num
            raw_data.telephone = new_tel
            raw_data.money = new_money
            raw_data.low = new_low
            try:
                db.session.commit()
                return Api.success('修改成功')
            except Exception as e:
                db.session.rollback()
                return Api.params_error(msg='数据错误')
        else:
            return Api.params_error('没有此信息')
    else:
        return Api.params_error(msg=form.get_error)





