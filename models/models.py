import random

from odoo import models, fields, api


class SafetyControl(models.Model):
    _name = 'safety_control.safety_control'
    _description = 'Safety Control'
    _rec_name = 'action'

    device = fields.Char()

    action = fields.Char(string="Action")
    time = fields.Char(string="Time of Report")
    lastTime = fields.Char(string="Time of Report")
    area = fields.Char(string="Area")
    image = fields.Binary(
        string="Image",
        store=True,
        attachment=False
    )

    recognitionType = fields.Text()

    personWithoutHelmet = fields.Boolean(string="Person Without Helmet", default=False)
    personWithoutHeadphones = fields.Boolean(string="Person Without Headphones", default=False)
    personWithoutJacket = fields.Boolean(string="Person Without Jacket", default=False)
    personWithoutGloves = fields.Boolean(string="Person Without Gloves", default=False)
    personWithoutMask = fields.Boolean(string="Person Without Mask", default=False)

    color = fields.Integer(string='Color')

    @api.model
    def create(self, vals):

        vals['image'] = vals['image'].split(',')[-1]
        vals['color'] = random.randint(0, 255)

        return super(SafetyControl, self).create(vals)
