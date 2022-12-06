# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class safety_control(models.Model):
#     _name = 'safety_control.safety_control'
#     _description = 'safety_control.safety_control'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
