
from odoo import api, models, fields

class CrmTeam(models.Model):
	_inherit = 'crm.team'

	member_ids = fields.Many2many(
        'res.users', 
        #'sale_team_id', 
        string='Channel Members',
        check_company=True, 
        domain=[('share', '=', False)],
        help="Add members to automatically assign their documents to this sales team. You can only be member of one team.")
