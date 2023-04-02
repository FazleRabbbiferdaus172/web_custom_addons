# -*- coding: utf-8 -*-
# from odoo import http


# class DropDownX2mLines(http.Controller):
#     @http.route('/drop_down_x2m_lines/drop_down_x2m_lines', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/drop_down_x2m_lines/drop_down_x2m_lines/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('drop_down_x2m_lines.listing', {
#             'root': '/drop_down_x2m_lines/drop_down_x2m_lines',
#             'objects': http.request.env['drop_down_x2m_lines.drop_down_x2m_lines'].search([]),
#         })

#     @http.route('/drop_down_x2m_lines/drop_down_x2m_lines/objects/<model("drop_down_x2m_lines.drop_down_x2m_lines"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('drop_down_x2m_lines.object', {
#             'object': obj
#         })
