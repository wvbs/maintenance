# Copyright 2024 Worldwide Vision Business Solutions S.L. (https://wvbs.eu)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class MaintenanceEquipmentCategory(models.Model):
    _inherit = "maintenance.equipment.category"

    equipment_properties_definition = fields.PropertiesDefinition(
        "Equipment Properties"
    )
