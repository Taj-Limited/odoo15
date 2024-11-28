import datetime

from odoo import models, fields


class ReportTripProfit(models.Model):
    _name = 'report.trip.profit'
    _description = "Report Trip Profit"

    order_id = fields.Many2one('sale.order', 'Order')
    truck = fields.Char("Truck")
    root = fields.Many2one('product.template', 'Root')
    trip = fields.Char("Trip")
    size = fields.Char("Size")
    date = fields.Date("Year")
    operating_income = fields.Float("Operating Income")
    total_going = fields.Float("Total Going")
    total_return = fields.Float("Total Return")
    total_fuel = fields.Float("Total Fuel")
    total_cost = fields.Float("Total Cost")
    expenses = fields.Float("Expenses")
    cross_profit = fields.Float('Cross Profit')
    percentage = fields.Float('%')
    mbeya = fields.Float('Mbeya')
    kibaha = fields.Float('Kibaha')
    morogoro = fields.Float('Morogoro')
    tunduma = fields.Float('Tunduma')
    transit_fees_documentation_fees = fields.Float('Transit Fees Documentation Fees')
    transit_fees_levy_council_fee_nakonde = fields.Float('Transit fees Levy Fee Nakonde')
    transit_fees_levy_council_fee_kapiri = fields.Float('Transit fees Levy Council Fee Kapiri')
    transit_fees_parking_security_fees_going = fields.Float('Transit fees Parking Security Fees Going')
    transit_fees_road_permit = fields.Float('Transit fees Road Permit')
    transit_fees_electronic_seal = fields.Float('Transit fees Electronic Seal')
    transit_fees_border_fees = fields.Float('Transit fees Border Fees')
    transit_fees_first_entry = fields.Float('Transit fees First Entry')
    transit_fees_lashing_fees = fields.Float('Transit fees Lashing Fees')
    transit_fees_abnormalm_signage = fields.Float('Transit fees Abnormalm Signage')
    transit_fees_gcla_loading_facilitation_permit = fields.Float('Transit fees GCLA Loading Facilitation Permit')
    transit_fees_weighbridge_fees = fields.Float('Transit fees Weighbridge Fees')
    transit_fees_peage = fields.Float('Transit fees Peage')
    transit_fees_levy_council_fee_tunduma = fields.Float('Transit fees Levy Council Fee Tunduma')
    transit_fees_cargo_rearrangement = fields.Float('Transit fees Cargo Rearrangement')
    transit_fees_demurrage_fee = fields.Float('Transit fees Demurrage Fee')
    driver_trip_allowance_expense_transit = fields.Float('Driver Trip Allowance Expense Transit')
    transit_fees_bond_going = fields.Float('Transit fees Bond going')
    transit_fees_tollRoad = fields.Float('Transit fees TollRoad')
    transit_fees_gcla_loading_facilitation_other_going = fields.Float(
        'Transit fees GCLA Loading Facilitation Other going')
    toll_gates_going = fields.Float('Toll Gates going')
    return_fees_container_tAX_going = fields.Float('Return fees Container TAX going')
    late_exit_note_going = fields.Float('Late Exit Note going')
    carbon_tax_going = fields.Float('Carbon Tax going')
    return_fees_weight_pridje_going = fields.Float('Return fees weight pridje going')
    wating_charges_going = fields.Float('wating charges going')
    return_fees_carrier_license = fields.Float('Return fees Carrier License')
    return_fee_over_stay = fields.Float('Return fee Over Stay')
    return_fees_cargo_rearrangement = fields.Float('Return fees Cargo Rearrangement')
    return_fees_radiation_protection_fee = fields.Float('Return fees Radiation Protection Fee')
    return_fees_weight_check_ndola = fields.Float('Return fees Weight Check Ndola')
    return_fees_parking_security_fees = fields.Float('Return fees Parking Security Fees')
    return_fee_over_stay_2 = fields.Float('Return fee Over Stay')
    return_fees_entry_card = fields.Float('Return fees Entry Card')
    return_fees_kanyaka = fields.Float('Return fees Kanyaka')
    return_fees_levy_council_fee_kapiri = fields.Float('Return fees Levy Council Fee Kapiri')
    return_fees_penalty_over_wight = fields.Float('Return fees Penalty over wight')
    transit_fees_bond = fields.Float('Transit fees Bond')
    transit_fees_road_toll = fields.Float('Transit fees Road Toll')
    transit_fees_gcla_loading_facilitation_other = fields.Float('Transit fees GCLA Loading Facilitation Other')
    toll_gates = fields.Float('Toll Gates')
    late_exit_note = fields.Float('Late Exit Note')
    return_fees_container_tax = fields.Float('Return fees Container TAX')
    carbon_tax = fields.Float('Carbon Tax')
    return_fees_weight_pridje = fields.Float('Return fees weight pridje')
    wating_charges = fields.Float('wating_charges')
    return_fees_empty_container_offloading_fees = fields.Float('Return fees Empty Container Offloading Fees')
    return_fees_visa = fields.Float('Return fees Visa')
    return_fees_weight_check_tunduma = fields.Float('Return fees Weight Check Tunduma')
    return_fees_chemical_transportation = fields.Float('Return fees Chemical transportation')
    driver_trip_allowance_expense_return = fields.Float('Driver Trip Allowance Expense Return')
    return_fees_parking_security_fees_ret = fields.Float('Return fees Parking Security Fees Ret')
    return_fees_peage = fields.Float('Return Fees peage')
