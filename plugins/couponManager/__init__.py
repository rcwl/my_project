from flask import Flask, Blueprint
import os
from .cli import coupon_cli
from .view.coupon import bp

def event_init(app: Flask):
    """初始化时注册蓝图和模板目录"""
    # 注册蓝图
    app.register_blueprint(bp)
    
    # 添加插件的模板目录到 Flask 模板搜索路径
    template_path = os.path.join(os.path.dirname(__file__), 'templates')
    app.jinja_loader.searchpath.append(template_path)  # 关键：添加模板路径

def event_finish(app: Flask):
    """启动完成后注册CLI命令"""
    app.cli.add_command(coupon_cli)