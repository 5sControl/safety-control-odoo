from odoo import models, fields, api
from ..scripts.safety_handlers import face_rec


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
        tracing_face = face_rec(vals['photo'].split(',')[-1])
        vals['photo'] = tracing_face
        return super(SafetyControl, self).create(vals)