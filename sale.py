# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv

class sale_order(osv.osv):
	_name = 'sale.order'
	_inherit = 'sale.order'

	def _fnct_margin_percent(self, cr, uid, ids, field_name, args, context=None):

	        if context is None:
        	    context = {}
        	res = {}
        	for order in self.browse(cr, uid, ids, context=context):
			order_cost = order.amount_untaxed - order.margin
			if order.amount_untaxed > 0:
				percent = (1-(order_cost/order.amount_untaxed))*100
                        	res[order.id] = percent
                	else:
                        	res[order.id] = 0
	        return res

	_columns = {
        	'margin_percent': fields.function(_fnct_margin_percent, string='% Margen'),
		}


sale_order()
