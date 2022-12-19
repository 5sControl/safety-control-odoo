from odoo import http
from odoo.http import request


class SafetyControl(http.Controller):
    @http.route('/safety/get_all_alerts', auth='user', crf=True, type='json', methods=['GET'])
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
            if rec['image']:
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
                return {'success': True,
                        'message': 'Success',
                        'ID': request.env['safety_control.safety_control'].sudo().create(vals).id}
            else:
                return {'success': False, 'message':'Something went wrong'}


    @http.route('/safety/update_alert', auth='user', website=False, crf=True, type='json', methods=['POST'])
    def edit(self, **rec):
        try:
            alert_last_time = request.env['safety_control.safety_control'].search([], limit=1)
            alert_last_time.lastTime = rec['lastTime']
            alert_last_time.write({'lastTime': rec['lastTime']})
        except KeyError:
            return {'success': False,
                    'message': 'KeyError'}
        else:
            return {'success': True,
               'message': 'Record was successfully updated'}


    @http.route('/safety/ping', type='json', auth='public', crf=False, methods=['POST'])
    def ping(self):
        return {'success': True}
