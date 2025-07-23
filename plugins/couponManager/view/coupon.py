from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from applications.common.utils.rights import authorize
from applications.common.utils.curd import get_one_by_id, delete_one_by_id
from ..models.coupon import Coupon
from applications.extensions import db

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

# 添加券码
@bp.post('/save')
@login_required
@authorize("system:coupon:add")
def save():
    data = request.get_json()
    coupon = Coupon(
        code=data['code'],
        discount=data['discount'],
        description=data['description'],
        start_time=data['start_time'],
        end_time=data['end_time']
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
    coupon = get_one_by_id(Coupon, data['id'])
    coupon.code = data['code']
    coupon.discount = data['discount']
    coupon.enable = data['enable']
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