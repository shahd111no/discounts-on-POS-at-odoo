from odoo import api, fields, models, tools

class PosSessionload(models.Model):
    _inherit = 'pos.session'


    def _loader_params_res_partner(self):
        result = super()._loader_params_res_partner()

        result['search_params']['fields'].append('discount')
        return result