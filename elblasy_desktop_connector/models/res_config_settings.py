# -*- coding: utf-8 -*-
from odoo import models, fields, api
import random
from datetime import datetime


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    desktop_connection_enabled = fields.Boolean(
        string='Enable Desktop Connection',
        default=False,
        help='Enable connection between Odoo and desktop application'
    )

    connection_code = fields.Char(
        string='Connection Code',
        readonly=True,
        help='Auto-generated connection code'
    )

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()

        # Get saved values
        enabled = params.get_param('desktop_connection.enabled', 'False') == 'True'
        code = params.get_param('desktop_connection.code', '')

        res.update(
            desktop_connection_enabled=enabled,
            connection_code=code
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        params = self.env['ir.config_parameter'].sudo()

        # Save enabled state
        params.set_param('desktop_connection.enabled', self.desktop_connection_enabled)

        # Generate code only when enabled and no code exists
        if self.desktop_connection_enabled:
            if not self.connection_code:
                new_code = f"{random.randint(100000, 999999)}-{datetime.now().strftime('%Y-%m-%d')}"
                params.set_param('desktop_connection.code', new_code)
        else:
            # Clear code when disabled
            params.set_param('desktop_connection.code', '')