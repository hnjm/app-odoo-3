# -*- coding: utf-8 -*-

# Created on 2018-08-15
# author: 广州尚鹏，https://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo在线中文用户手册（长期更新）
# https://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.sunpop.cn/odoo10_developer_document_offline/
# description:

{
    'name': "Project and task browse by partner,user, stage navigator",
    'version': '13.21.06.09',
    'author': 'Sunpop.cn',
    'category': 'Base',
    'website': 'https://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    Browse project by company / partner / user. Project task by user, tags.
    project superbar.
    Easy to navigator and browse any data. Support list, kanban, pivot, graph view. 
    ztree widget.Hierarchy Tree.
    """,
    'description': """
    Superbar, zTree widget. 
    Advance search with real parent children tree, ListView or KanbanView. parent tree, children tree,
    eg: Product category tree ,Department tree, stock location tree.
    超级方便的查询，树状视图。
    """,
    'price': 0.00,
    'currency': 'EUR',
    'depends': [
        'project',
    ],
    'images': ['static/description/superbar.gif'],
    'data': [
        'views/project_project_views.xml',
        'views/project_task_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'js': [
    ],
    'post_load': None,
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}