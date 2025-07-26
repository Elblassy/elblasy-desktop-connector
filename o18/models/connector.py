# -*- coding: utf-8 -*-
from odoo import models, fields, api
import random
from datetime import datetime

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    desktop_connection_enabled = fields.Boolean(
        string='Desktop Connection',
        default=True,
        help='Enable desktop connection'
    )

    connection_code = fields.Char(
        string='Connection Code',
        readonly=True,
        help='Auto-generated connection code'
    )

    @api.onchange('desktop_connection_enabled')
    def _onchange_desktop_connection_enabled(self):
        """Generate connection code when desktop connection is enabled"""
        if self.desktop_connection_enabled:
            self.connection_code = self._generate_connection_code()

    def _generate_connection_code(self):
        """Generate connection code with date"""
        # Generate random 6-digit number
        random_number = random.randint(100000, 999999)

        # Today's date
        today = datetime.now().strftime('%Y-%m-%d')

        # Combine code
        connection_code = f"{random_number}-{today}"

        return connection_code
