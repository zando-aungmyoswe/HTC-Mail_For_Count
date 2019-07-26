# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PropertyType(models.Model):
    _name = 'property.type'

    name = fields.Char("Name")
    code = fields.Char("Code")

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            code = record.code
            result.append((record.id, code))
        return result


class MlMall(models.Model):
    _name = 'ml.mall'

    name = fields.Char("Property Name", required=True)
    code = fields.Char("Code", required=True)
    property_type = fields.Many2one("property.type", "Property Type")
    uom = fields.Many2one("uom.uom", "Unit of Measure")
    gross_floor_area = fields.Char('GFA')
    net_lett_able_area = fields.Char('NLA')
    web_site_url = fields.Char("Web site of Property")
    address_no = fields.Char("No")
    address_street = fields.Char("Street")
    city = fields.Many2one("res.state.city", "City")
    state = fields.Many2one("res.country.state", "State")
    postal_code = fields.Char("Postal Code")
    country_id = fields.Many2one("res.country", "Country")
    auto_generate_posid = fields.Boolean("Auto Generate Pos ID")
    next_pos_id = fields.Char("Next Pos ID")
    pos_id_format = fields.Char("POS ID Format")
    management_team = fields.Many2one("management.team","Management Team")
    position = fields.Char("Position")
    phone = fields.Char("Phone")
    bank_info = fields.Char("Bank Name")
    management = fields.Char("Management Company")
    mgt_address1 = fields.Char('Address1')
    mgt_address2 = fields.Char('Address2')
    mgt_city = fields.Many2one('res.state.city', "City")
    mgt_postal_code = fields.Char("Postal Code")
    mgt_state = fields.Many2one("res.country.state", "State")
    mgt_country = fields.Many2one("res.country", "Country")
    office_phone = fields.Char("Office Phone")
    contact_person = fields.Char("Contact Person")

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            code = record.code
            result.append((record.id, code))
        return result

    # @api.model
    # def create(self, values):
    # 	if values.get('name', 'New') == 'New':
    # 		values['name'] = 'Mall(' + self.mall.code + ')/Unit('+ self.unit_no +')'
    # 	return super(MlMall, self).create(values)


class ManagementTeam(models.Model):
    _name = "management.team"

    name = fields.Char("Name")
        
class MlFloor(models.Model):
    _name = 'ml.floor'

    name = fields.Char("Description", required=True)
    code = fields.Char("Code")
    remark = fields.Text("Remark")

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            code = record.code
            result.append((record.id, code))
        return result


class MlMeterType(models.Model):
    _name = "ml.meter.type"

    name = fields.Char("Meter Type")
    i_lmr_date = fields.Date("Installed Date")
    s_lmr_value = fields.Integer("Start Reading Value")
    e_lmr_value = fields.Integer("End Reading Value")
    uom_id = fields.Many2one("uom.uom", 'UOM')
    digit = fields.Selection([('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
                              ('7', '7'), ('8', '8'), ('9', '9')],
                             "Display Digits")
    end_date = fields.Date("Inactive On")
    status = fields.Boolean("Status")
    utility = fields.Many2one("ml.space.utility", "Utility")
    display_type = fields.Many2one('ml.display.type', 'Display Type')
    charge_type = fields.Selection([('fixed', 'Fixed'),
                                    ('variable', 'Variable')],
                                   string="Charge Type")


class MlMeterType(models.Model):
    _name = "utility.type"

    name = fields.Char("Utility Name")
    code = fields.Char("Utility Type")

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            code = record.code
            result.append((record.id, code))
        return result


class MeterNumber(models.Model):
    _name = 'meter.number'

    name = fields.Char("Name")
    number = fields.Integer('Number')

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            number = record.number
            result.append((record.id, number))
        return result


class MlSpaceUtility(models.Model):
    _name = 'ml.space.utility'

    name = fields.Char("New")
    utility_type = fields.Many2one('utility.type', "Utility Type")
    utility_code = fields.Char("Code", related="utility_type.code", store=True)
    meter_no = fields.Many2one("meter.number")
    start_date = fields.Date("Start Date")
    utt_idd = fields.Boolean("IDD")
    utt_local = fields.Boolean("LOCAL")
    utt_mobile = fields.Boolean("MOBILE")
    utt_std = fields.Boolean("STD")
    utt_gen = fields.Boolean("GEN")
    utt_sub = fields.Boolean("SUB")
    interface_type = fields.Selection([('auto', 'Auto'), ('manual', 'Manual'),
                                       ('mobile', 'Mobile')], "Interface Type")
    remark = fields.Text("Remark")
    meter_type_id = fields.One2many("ml.meter.type", 'utility', "Meter Type")
    unit_id = fields.Many2one("ml.space", string='Space Unit')


class MlSpace(models.Model):
    _name = 'ml.space'

    name = fields.Char("Name", default="New", readonly=True)
    mall = fields.Many2one("ml.mall", string="Property", required=True)
    floor = fields.Many2one("ml.floor", string="Floor")
    unit_no = fields.Char("Space Unit No", required=True)
    # meter_no = fields.Char("Meter No")
    area = fields.Integer("Space Area")
    date = fields.Date("Start Date")
    enddate = fields.Date("End Date")
    uom = fields.Many2one("uom.uom", "UOM")
    remark = fields.Text("Remark")
    status = fields.Boolean("Status", default=True)
    utility_id = fields.One2many("ml.space.utility", "unit_id", "Facility")

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            code = record.unit_no
            result.append((record.id, code))
        return result

    @api.model
    def create(self, values):
        if values.get('name', 'New') == 'New':
            values['name'] = 'Mall(' + self.env['ml.mall'].browse(
                values['mall']).code + ')/Unit(' + values['unit_no'] + ')'
        return super(MlSpace, self).create(values)


class MlDisplayType(models.Model):
    _name = "ml.display.type"

    name = fields.Char("Display Name")
    code = fields.Char("Display Code")

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            code = record.code
            result.append((record.id, code))
        return result


class ResStateCity(models.Model):
    _name = 'res.state.city'

    name = fields.Char("Name")
    state_id = fields.Many2one("res.country.state", "State")
