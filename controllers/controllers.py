# -*- coding: utf-8 -*-
# from odoo import http


# class SafetyControl(http.Controller):
#     @http.route('/safety_control/safety_control', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/safety_control/safety_control/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('safety_control.listing', {
#             'root': '/safety_control/safety_control',
#             'objects': http.request.env['safety_control.safety_control'].search([]),
#         })

#     @http.route('/safety_control/safety_control/objects/<model("safety_control.safety_control"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('safety_control.object', {
#             'object': obj
#         })
