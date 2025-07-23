from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from applications.common.utils.rights import authorize
from applications.common.curd import get_one_by_id, delete_one_by_id
from ..models.coupon import Coupon
from applications.extensions import db
from  datetime import datetime


bp = Blueprint('coupon', __name__, url_prefix='/system/coupon')

# 券码管理首页
@bp.get('/')
@login_required
@authorize("system:coupon:main")
def main():
    return render_template('system/coupon/main.html')

# 券码数据接口
@bp.get('/data')
@login_required
@authorize("system:coupon:main")
def data():
    code = request.args.get('code', '')
    coupons = Coupon.query.filter(
        Coupon.code.like(f'%{code}%')
    ).order_by(Coupon.create_time.desc()).all()
    return jsonify({
        "code": 0,
        "msg": "success",
        "data": [{"id": c.id, "code": c.code, "discount": c.discount, 
                 "description": c.description, "enable": c.enable, 
                 "used": c.used, "create_time": c.create_time} for c in coupons]
    })

from datetime import datetime  # 顶部添加导入

# 添加券码
@bp.post('/save')
@login_required
@authorize("system:coupon:add")
def save():
    data = request.get_json()
    
    # 关键修改：将字符串日期转换为datetime对象
    try:
        start_time = datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(data['end_time'], '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        return jsonify({"success": False, "msg": f"日期格式错误: {str(e)}"})
    
    # 转换折扣为浮点数
    try:
        discount = float(data['discount'])
    except ValueError:
        return jsonify({"success": False, "msg": "折扣必须是数字"})
    
    coupon = Coupon(
        code=data['code'],
        discount=discount,
        description=data.get('description', ''),
        start_time=start_time,  # 使用转换后的datetime对象
        end_time=end_time,      # 使用转换后的datetime对象
        enable=int(data.get('enable', 1))  # 确保状态是整数
    )
    db.session.add(coupon)
    db.session.commit()
    return jsonify({"success": True, "msg": "添加成功"})

# 编辑券码
@bp.put('/update')
@login_required
@authorize("system:coupon:edit")
def update():
    data = request.get_json()
    
    # 转换日期
    try:
        start_time = datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(data['end_time'], '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        return jsonify({"success": False, "msg": f"日期格式错误: {str(e)}"})
    
    # 转换折扣
    try:
        discount = float(data['discount'])
    except ValueError:
        return jsonify({"success": False, "msg": "折扣必须是数字"})
    
    coupon = get_one_by_id(Coupon, data['id'])
    coupon.code = data['code']
    coupon.discount = discount
    coupon.description = data.get('description', '')
    coupon.start_time = start_time
    coupon.end_time = end_time
    coupon.enable = int(data['enable'])
    db.session.commit()
    return jsonify({"success": True, "msg": "更新成功"})

# 删除券码
@bp.delete('/remove/<int:_id>')
@login_required
@authorize("system:coupon:remove")
def remove(_id):
    if delete_one_by_id(Coupon, _id):
        return jsonify({"success": True, "msg": "删除成功"})
    return jsonify({"success": False, "msg": "删除失败"})

# 券码兑换接口（用户端）
@bp.post('/exchange')
@login_required
def exchange():
    code = request.get_json().get('code')
    coupon = Coupon.query.filter_by(code=code).first()
    if not coupon:
        return jsonify({"success": False, "msg": "券码不存在"})
    if coupon.used == 1:
        return jsonify({"success": False, "msg": "券码已使用"})
    if coupon.enable == 0:
        return jsonify({"success": False, "msg": "券码已禁用"})
    coupon.used = 1  # 标记为已使用
    db.session.commit()
    return jsonify({"success": True, "msg": f"兑换成功！获得{coupon.discount*10}折优惠"})

# 新增券码页面
@bp.get('/add')
@login_required
@authorize("system:coupon:add")
def add():
    return render_template('system/coupon/add.html')

# 编辑券码页面
@bp.get('/edit/<int:_id>')
@login_required
@authorize("system:coupon:edit")
def edit(_id):
    coupon = get_one_by_id(Coupon, _id)
    return render_template('system/coupon/edit.html', coupon=coupon)