import click
from datetime import datetime
from flask import current_app
from applications.extensions import db
from applications.models import Power
from ..models.coupon import Coupon

coupon_cli = click.Group('coupon', help='券码管理相关命令')

@coupon_cli.command("init")
def init_db():
    """初始化券码管理数据库与权限"""
    now_time = datetime.now()
    
    # 添加菜单权限
    top_power = Power(
        name='券码管理',
        type='1',
        code='system:coupon:main',
        url='/system/coupon/',
        open_type='_iframe',
        parent_id='1',  # 父菜单ID（根据实际调整）
        icon='layui-icon layui-icon-coupon',
        sort=9,
        create_time=now_time,
        enable=1
    )
    db.session.add(top_power)
    db.session.commit()  # 提交获取ID
    
    # 子权限（添加、编辑、删除等）
    power_data = [
        Power(name='券码列表', type='2', code='system:coupon:main', url='', parent_id=top_power.id, enable=1),
        Power(name='添加券码', type='2', code='system:coupon:add', url='', parent_id=top_power.id, enable=1),
        Power(name='编辑券码', type='2', code='system:coupon:edit', url='', parent_id=top_power.id, enable=1),
        Power(name='删除券码', type='2', code='system:coupon:remove', url='', parent_id=top_power.id, enable=1),
    ]
    db.session.add_all(power_data)
    
    # 示例券码
    sample_coupons = [
        Coupon(
            code='COUPON2024',
            discount=0.8,
            description='全场8折券',
            start_time=now_time,
            end_time=datetime(2024, 12, 31),
            enable=1
        )
    ]
    db.session.add_all(sample_coupons)
    db.session.commit()
    print("券码管理模块初始化完成")