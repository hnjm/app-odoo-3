# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 广州尚鹏，https://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# https://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.sunpop.cn/odoo10_developer_document_offline/
# description:

{
    'name': "Multi Add Sale Product,订单批量加产品",
    'version': '13.21.12.30',
    'author': 'Sunpop.cn',
    'category': 'Base',
    'website': 'https://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'USD',
    'summary': """
    App Sale Order Product Multi Batch Add, mass add
    Odoo App of Sunpop.cn
    """,
    'description': """
    App Sale Order Product Multi Add. 
    1. One Click to add multi product to Sale Order.
    2. All the product can filter and group.
    3. Pop a detail form to add sale line with detail.
    销售订单批量增加产品.
    1. 可以一键快速将多个产品加到销售订单中
    2. 可对产品进行过滤、分组，然后批量加入
    3. 可以弹出一个明细录入界面添加，便于同时支持列表添加及表单添加
    """,
    'depends': [
        # 'app_web_one2many_multi_add',
        'sale_management',
    ],
    'images': ['static/description/banner.gif'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'js': [
    ],
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}
