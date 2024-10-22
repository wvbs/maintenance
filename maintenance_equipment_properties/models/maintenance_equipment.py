# Copyright 2024 Worldwide Vision Business Solutions S.L. (https://wvbs.eu)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    equipment_properties = fields.Properties(
        "Properties",
        definition="category_id.equipment_properties_definition",
        copy=True,
    )
