"""empty message

Revision ID: b180f4732795
Revises: 
Create Date: 2025-07-23 19:48:23.050281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b180f4732795'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_admin_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('method', sa.String(length=10), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('ip', sa.String(length=255), nullable=True),
    sa.Column('success', sa.Integer(), nullable=True),
    sa.Column('user_agent', sa.Text(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin_dept',
    sa.Column('id', sa.Integer(), nullable=False, comment='部门ID'),
    sa.Column('parent_id', sa.Integer(), nullable=True, comment='父级编号'),
    sa.Column('dept_name', sa.String(length=50), nullable=True, comment='部门名称'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='排序'),
    sa.Column('leader', sa.String(length=50), nullable=True, comment='负责人'),
    sa.Column('phone', sa.String(length=20), nullable=True, comment='联系方式'),
    sa.Column('email', sa.String(length=50), nullable=True, comment='邮箱'),
    sa.Column('status', sa.Integer(), nullable=True, comment='状态(1开启,0关闭)'),
    sa.Column('remark', sa.Text(), nullable=True, comment='备注'),
    sa.Column('address', sa.String(length=255), nullable=True, comment='详细地址'),
    sa.Column('create_at', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_at', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin_dict_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_label', sa.String(length=255), nullable=True, comment='字典类型名称'),
    sa.Column('data_value', sa.String(length=255), nullable=True, comment='字典类型标识'),
    sa.Column('type_code', sa.String(length=255), nullable=True, comment='字典类型描述'),
    sa.Column('is_default', sa.Integer(), nullable=True, comment='是否默认'),
    sa.Column('enable', sa.Integer(), nullable=True, comment='是否开启'),
    sa.Column('remark', sa.String(length=255), nullable=True, comment='备注'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin_dict_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_name', sa.String(length=255), nullable=True, comment='字典类型名称'),
    sa.Column('type_code', sa.String(length=255), nullable=True, comment='字典类型标识'),
    sa.Column('description', sa.String(length=255), nullable=True, comment='字典类型描述'),
    sa.Column('enable', sa.Integer(), nullable=True, comment='是否开启'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin_mail',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='邮件编号'),
    sa.Column('receiver', sa.String(length=1024), nullable=True, comment='收件人邮箱'),
    sa.Column('subject', sa.String(length=128), nullable=True, comment='邮件主题'),
    sa.Column('content', sa.Text(), nullable=True, comment='邮件正文'),
    sa.Column('user_id', sa.Integer(), nullable=True, comment='发送人id'),
    sa.Column('create_at', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin_photo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('href', sa.String(length=255), nullable=True),
    sa.Column('mime', sa.CHAR(length=50), nullable=False),
    sa.Column('size', sa.CHAR(length=30), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin_power',
    sa.Column('id', sa.Integer(), nullable=False, comment='权限编号'),
    sa.Column('name', sa.String(length=255), nullable=True, comment='权限名称'),
    sa.Column('type', sa.String(length=1), nullable=True, comment='权限类型'),
    sa.Column('code', sa.String(length=30), nullable=True, comment='权限标识'),
    sa.Column('url', sa.String(length=255), nullable=True, comment='权限路径'),
    sa.Column('open_type', sa.String(length=10), nullable=True, comment='打开方式'),
    sa.Column('parent_id', sa.Integer(), nullable=True, comment='父类编号'),
    sa.Column('icon', sa.String(length=128), nullable=True, comment='图标'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='排序'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('enable', sa.Integer(), nullable=True, comment='是否开启'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin_role',
    sa.Column('id', sa.Integer(), nullable=False, comment='角色ID'),
    sa.Column('name', sa.String(length=255), nullable=True, comment='角色名称'),
    sa.Column('code', sa.String(length=255), nullable=True, comment='角色标识'),
    sa.Column('enable', sa.Integer(), nullable=True, comment='是否启用'),
    sa.Column('remark', sa.String(length=255), nullable=True, comment='备注'),
    sa.Column('details', sa.String(length=255), nullable=True, comment='详情'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='排序'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='用户ID'),
    sa.Column('username', sa.String(length=20), nullable=True, comment='用户名'),
    sa.Column('realname', sa.String(length=20), nullable=True, comment='真实名字'),
    sa.Column('avatar', sa.String(length=255), nullable=True, comment='头像'),
    sa.Column('remark', sa.String(length=255), nullable=True, comment='备注'),
    sa.Column('password_hash', sa.String(length=128), nullable=True, comment='哈希密码'),
    sa.Column('enable', sa.Integer(), nullable=True, comment='启用'),
    sa.Column('dept_id', sa.Integer(), nullable=True, comment='部门id'),
    sa.Column('create_at', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_at', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin_role_power',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='标识'),
    sa.Column('power_id', sa.Integer(), nullable=True, comment='用户编号'),
    sa.Column('role_id', sa.Integer(), nullable=True, comment='角色编号'),
    sa.ForeignKeyConstraint(['power_id'], ['admin_power.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['admin_role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin_user_role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='标识'),
    sa.Column('user_id', sa.Integer(), nullable=True, comment='用户编号'),
    sa.Column('role_id', sa.Integer(), nullable=True, comment='角色编号'),
    sa.ForeignKeyConstraint(['role_id'], ['admin_role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['admin_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin_user_role')
    op.drop_table('admin_role_power')
    op.drop_table('admin_user')
    op.drop_table('admin_role')
    op.drop_table('admin_power')
    op.drop_table('admin_photo')
    op.drop_table('admin_mail')
    op.drop_table('admin_dict_type')
    op.drop_table('admin_dict_data')
    op.drop_table('admin_dept')
    op.drop_table('admin_admin_log')
    # ### end Alembic commands ###
