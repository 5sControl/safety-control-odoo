from odoo import http
from odoo.http import request


class SafetyControl(http.Controller):
    @http.route('/safety_control/get_all_alerts', auth='user', crf=True, type='json', methods=['POST'])
    def all_alerts(self, **kw):
        alert_rec = http.request.env['safety_control.safety_control'].sudo().search([])
        alerts = []
        for rec in alert_rec:
            alerts.append({
                'action': rec.action,
                'date': rec.date,
                'area': rec.area,
                'photo': rec.photo,
            })

        return alerts

    @http.route('/safety/create_alert', auth='user', website=False, crf=True, type='json', methods=['POST'])
    def create(self, **rec):
        if http.request.render:
            if rec['action']:
                vals = {
                    'action': rec['action'],
                    'date': rec['date'],
                    'area': rec['area'],
                    'photo': rec['photo'],
                }
                new_alert = request.env['safety_control.safety_control'].sudo().create(vals)
                args = {'success': True, 'message': 'Success', 'ID': new_alert.id}
        return args

    @http.route('/safety/ping', type='json', auth='public', crf=False, methods=['POST'])
    def ping(self):
        return {'success': True}
