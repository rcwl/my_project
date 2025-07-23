from flask import Flask
from .cli import coupon_cli
from .view.coupon import bp

def event_init(app: Flask):
    """初始化时注册蓝图"""
    app.register_blueprint(bp)

def event_finish(app: Flask):
    """启动完成后注册CLI命令"""
    app.cli.add_command(coupon_cli)