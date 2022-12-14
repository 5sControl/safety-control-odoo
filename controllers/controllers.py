from odoo import http
from odoo.http import request


class SafetyControl(http.Controller):
    @http.route('/safety_control/get_all_alerts', auth='user', crf=True, type='json', methods=['POST'])
    def all_alerts(self, **kw):
        alert_rec = http.request.env['safety_control.safety_control'].sudo().search([])
        alerts = []
        for rec in alert_rec:
            alerts.append({
                'device': rec.device,

                'time': rec.time,
                'lastTime': rec.lastTime,
                'image': rec.image,

                'recognitionType': rec.recognitionType,

                'personWithoutHelmet': rec.personWithoutHelmet,
                'personWithoutHeadphones': rec.personWithoutHeadphones,
                'personWithoutJacket': rec.personWithoutJacket,
                'personWithoutGloves': rec.personWithoutGloves,
                'personWithoutMask': rec.personWithoutMask,
            })

        return alerts

    @http.route('/safety/create_alert', auth='user', website=False, crf=True, type='json', methods=['POST'])
    def create(self, **rec):
        if http.request.render:
            if rec['time']:
                vals = {
                    'device': rec['device'],

                    'time': rec['time'],
                    'lastTime': rec['lastTime'],
                    'image': rec['image'],

                    'recognitionType': rec['recognitionType'],

                    'personWithoutHelmet': rec['personWithoutHelmet'],
                    'personWithoutHeadphones': rec['personWithoutHeadphones'],
                    'personWithoutJacket': rec['personWithoutJacket'],
                    'personWithoutGloves': rec['personWithoutGloves'],
                    'personWithoutMask': rec['personWithoutMask'],
                }
                new_alert = request.env['safety_control.safety_control'].sudo().create(vals)
                args = {'success': True, 'message': 'Success', 'ID': new_alert.id}
        return args

    @http.route('/safety/ping', type='json', auth='public', crf=False, methods=['POST'])
    def ping(self):
        return {'success': True}
