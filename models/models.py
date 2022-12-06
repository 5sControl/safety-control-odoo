from odoo import models, fields, api


class SafetyControl(models.Model):
    _name = 'safety_control.safety_control'
    _description = 'Safety Control'
    _rec_name = 'action'

    action = fields.Char()
    date = fields.Char()
    area = fields.Char()
    photo = fields.Binary(
        string="Image",
        compute="_compute_image",
        store=True,
        attachment=False
    )

    @api.model
    def create(self, vals):
        vals['photo'] = vals['photo'].split(',')[1]
        return super(SafetyControl, self).create(vals)