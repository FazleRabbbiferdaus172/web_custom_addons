# -*- coding: utf-8 -*-

from odoo import models, fields, api


class drop_down_x2m_lines(models.Model):
    _name = 'drop_down_x2m_lines.drop_down_x2m_lines'
    _description = 'drop_down_x2m_lines.drop_down_x2m_lines'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    lines = fields.One2many('drop.down.x2m.lines.inside', 'main_ddXM_id', string='lines')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100


class DropDownlineInside(models.Model):
    _name = 'drop.down.x2m.lines.inside'
    _description = 'drop_down_x2m_lines_inside'

    ddXM_id = fields.Many2one(string='Product', comodel_name='drop_down_x2m_lines.drop_down_x2m_lines')
    price = fields.Float(string='Price', default=0)
    main_ddXM_id = fields.Many2one(string='Parent', comodel_name='drop_down_x2m_lines.drop_down_x2m_lines')


class ImSaleOrder(models.Model):
    _name = 'im.sale.order'
    _description = 'sale order replica'

    name = fields.Char(name='name')
    lines = fields.One2many('im.sale.order.line', 'im_sale_order_id', string='lines')

    def add_to_line(self):
        lines = []
        main = self.env['drop_down_x2m_lines.drop_down_x2m_lines'].search([('id', '=', 3)])
        for i in main.lines:
            lines.append(
                (0, 0, {
                    'drop_down_id': i.ddXM_id.id,
                    'price': i.price,
                })
            )
        lines.append(
            (0, 0, {
                'drop_down_id': main.id,
                'price': 0,
            })
        )
        self.update({
            'lines': lines,
        })


class ImSaleOrderLine(models.Model):
    _name = 'im.sale.order.line'
    _description = 'sale order line replica'

    drop_down_id = fields.Many2one(comodel_name='drop_down_x2m_lines.drop_down_x2m_lines', string='Product')
    price = fields.Float(string='Price')
    im_sale_order_id = fields.Many2one(comodel_name='im.sale.order', string='im sale order')
