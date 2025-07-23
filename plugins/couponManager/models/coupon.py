import datetime
from applications.extensions import db

class Coupon(db.Model):
    __tablename__ = 'admin_coupon'
    id = db.Column(db.Integer, primary_key=True, comment="唯一ID")
    code = db.Column(db.String(50), unique=True, comment="券码")
    discount = db.Column(db.Float, comment="折扣（如0.8表示8折）")
    description = db.Column(db.String(200), comment="券码描述")
    start_time = db.Column(db.DateTime, comment="生效时间")
    end_time = db.Column(db.DateTime, comment="过期时间")
    enable = db.Column(db.Integer, default=1, comment="是否启用（1=启用，0=禁用）")
    used = db.Column(db.Integer, default=0, comment="是否使用（1=已用，0=未用）")
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment="创建时间")