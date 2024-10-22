import datetime
import logging
from odoo import models

_logger = logging.getLogger(__name__)


class ReportTajProfitExcel(models.AbstractModel):
    _name = 'report.send_report_via_mail.profit_loss_report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        # print('data:::', data['products'])
        bold = workbook.add_format(
            {'bold': True, 'align': 'center', 'bg_color': '#757171', 'border': 1, 'color': 'white'})

        total_fuel_details = workbook.add_format(
            {'align': 'center', 'bg_color': '#a7a7a7', 'border': 1, 'bold': True})
        total_return_details = workbook.add_format(
            {'align': 'center', 'bg_color': '#e2efda', 'border': 1, 'bold': True})
        total_going_details = workbook.add_format(
            {'align': 'center', 'bg_color': '#fff2cc', 'border': 1, 'bold': True})
        sheet = workbook.add_worksheet("sheet")
        # sheet.column_dimensions.group("A", "D", hidden=True)
        sheet.set_column(0, 80, 30)
        sheet.write(0, 0, 'Truck', bold)
        sheet.write(0, 1, 'Order', bold)
        sheet.write(0, 2, 'Rout', bold)
        sheet.write(0, 3, 'Trip', bold)
        sheet.write(0, 4, 'Weight', bold)
        sheet.write(0, 5, 'Year', bold)
        sheet.write(0, 6, 'Operating Income', bold)
        sheet.write(0, 7, 'Transit fees Documentation Fees', total_going_details)
        sheet.write(0, 8, 'Transit fees Levy Council Fee Nakonde', total_going_details)
        sheet.write(0, 9, 'Transit fees Levy Council Fee Kapiri', total_going_details)
        sheet.write(0, 10, 'Transit fees Parking Security Fees', total_going_details)
        sheet.write(0, 11, 'Transit fees Road Permit', total_going_details)
        sheet.write(0, 12, 'Transit fees Electronic Seal', total_going_details)
        sheet.write(0, 13, 'Transit fees Border Fees', total_going_details)
        sheet.write(0, 14, 'Transit fees First Entry', total_going_details)
        sheet.write(0, 15, 'Transit fees Lashing Fees', total_going_details)
        sheet.write(0, 16, 'Transit fees Abnormalm Signage', total_going_details)
        sheet.write(0, 17, 'Transit fees GCLA Loading Facilitation Permit', total_going_details)
        sheet.write(0, 18, 'Transit fees Weighbridge Fees', total_going_details)
        sheet.write(0, 19, 'Transit fees Peage', total_going_details)
        sheet.write(0, 20, 'Transit fees Levy Council Fee Tunduma', total_going_details)
        sheet.write(0, 21, 'Transit fees Cargo Rearrangement', total_going_details)
        sheet.write(0, 22, 'Transit fees Demurrage Fee', total_going_details)
        sheet.write(0, 23, 'Driver Trip Allowance Expense Transit', total_going_details)
        sheet.write(0, 24, 'Transit fees Bond ', total_going_details)
        sheet.write(0, 25, 'Transit fees TollRoad', total_going_details)
        sheet.write(0, 26, 'Transit fees GCLA Loading Facilitation Other', total_going_details)
        sheet.write(0, 27, 'Toll Gates going', total_going_details)
        sheet.write(0, 28, 'Return fees Container TAX', total_going_details)
        sheet.write(0, 29, 'Late Exit Note going', total_going_details)
        sheet.write(0, 30, 'Carbon Tax going', total_going_details)
        sheet.write(0, 31, 'Return fees weight pridje', total_going_details)
        sheet.write(0, 32, 'wating charges', total_going_details)
        sheet.write(0, 33, 'Total Going', total_going_details)
        sheet.write(0, 34, 'Mbeya', total_fuel_details)
        sheet.write(0, 35, 'kibaha', total_fuel_details)
        sheet.write(0, 36, 'Morogoro', total_fuel_details)
        sheet.write(0, 37, 'Tunduma', total_fuel_details)
        sheet.write(0, 38, 'Total Fuel', total_fuel_details)
        sheet.write(0, 39, 'Return fees Carrier License', total_return_details)
        sheet.write(0, 40, 'Return fee Over Stay', total_return_details)
        sheet.write(0, 41, 'Return fees Cargo Rearrangement', total_return_details)
        sheet.write(0, 42, 'Return fees Radiation Protection Fee', total_return_details)
        sheet.write(0, 43, 'Return fees Weight Check Ndola', total_return_details)
        sheet.write(0, 44, 'Return fees Parking Security Fees', total_return_details)
        sheet.write(0, 45, 'Return fee Over Stay', total_return_details)
        sheet.write(0, 46, 'Return fees Peage', total_return_details)
        sheet.write(0, 47, 'Return fees Entry Card', total_return_details)
        sheet.write(0, 48, 'Return fees Kanyaka', total_return_details)
        sheet.write(0, 49, 'Return fees Levy Council Fee Kapiri', total_return_details)
        sheet.write(0, 50, 'Return fees Penalty over wight', total_return_details)
        sheet.write(0, 51, 'Transit fees Bond', total_return_details)
        sheet.write(0, 52, 'Transit fees Road Toll', total_return_details)
        sheet.write(0, 53, 'Transit fees GCLA Loading Facilitation Other', total_return_details)
        sheet.write(0, 54, 'Toll Gates', total_return_details)
        sheet.write(0, 55, 'Late Exit Note', total_return_details)
        sheet.write(0, 56, 'Return fees Container TAX', total_return_details)
        sheet.write(0, 57, 'Carbon Tax', total_return_details)
        sheet.write(0, 58, 'Return fees weight pridje', total_return_details)
        sheet.write(0, 59, 'wating charges', total_return_details)
        sheet.write(0, 60, 'Return fees Empty Container Offloading Fees', total_return_details)
        sheet.write(0, 61, 'Return fees Visa', total_return_details)
        sheet.write(0, 62, 'Return fees Weight Check Tunduma', total_return_details)
        sheet.write(0, 63, 'Return fees Chemical transportation', total_return_details)
        sheet.write(0, 64, 'Driver Trip Allowance Expense Return', total_return_details)
        sheet.write(0, 65, 'Return fees Parking Security Fees', total_return_details)
        sheet.write(0, 66, 'Levy council fee Tanzania', total_return_details)
        sheet.write(0, 67, 'Levy council fee Kenya', total_return_details)
        sheet.write(0, 68, 'Mineral Tax Kenya', total_return_details)
        sheet.write(0, 69, 'Ferry Fees', total_return_details)
        sheet.write(0, 70, 'Total Return', total_return_details)
        sheet.write(0, 71, 'Expenses', bold)
        sheet.write(0, 72, 'Gross Profit', bold)
        sheet.write(0, 73, '%', bold)

        # sheet.write(0, 13, 'Details', bold)

        # sheet.write(0, 5, 'Jt I sh', bold)
        # sheet.write(0, 6, 'Jt I Ml', bold)
        # sheet.write(0, 7, 'Jt I Ml Liq', bold)
        # sheet.write(0, 8, 'Last Purchase Date', bold)
        # sheet.write(0, 9, 'Out Of Stock Date', bold)
        # sheet.write(0, 10, 'Days Of Published', bold)
        # sheet.write(0, 11, 'Sales Price', bold)
        # sheet.write(0, 12, 'Quantity', bold)
        row = 0
        for obj in data['products']:
            row += 1
            sheet.write(row, 0, obj['license_plate'], bold)
            sheet.write(row, 1, obj['order_name'], bold)
            sheet.write(row, 2, obj['root'], bold)
            sheet.write(row, 3, obj['trip'], bold)
            sheet.write(row, 4, obj['size'], bold)
            sheet.write(row, 5, obj['date'], bold)
            sheet.write(row, 6, obj['operating_income'], bold)
            sheet.write(row, 7, obj['Transit_fees_Documentation_Fees'], total_going_details)
            sheet.write(row, 8, obj['Transit_fees_Levy_Council_Fee_Nakonde'], total_going_details)
            sheet.write(row, 9, obj['Transit_fees_Levy_Council_Fee_Kapiri'], total_going_details)
            sheet.write(row, 10, obj['Transit_fees_Parking_Security_Fees_going'], total_going_details)
            sheet.write(row, 11, obj['Transit_fees_Road_Permit'], total_going_details)
            sheet.write(row, 12, obj['Transit_fees_Electronic_Seal'], total_going_details)
            sheet.write(row, 13, obj['Transit_fees_Border_Fees'], total_going_details)
            sheet.write(row, 14, obj['Transit_fees_First_Entry'], total_going_details)
            sheet.write(row, 15, obj['Transit_fees_Lashing_Fees'], total_going_details)
            sheet.write(row, 16, obj['Transit_fees_Abnormalm_Signage'], total_going_details)
            sheet.write(row, 17, obj['Transit_fees_GCLA_Loading_Facilitation_Permit'], total_going_details)
            sheet.write(row, 18, obj['Transit_fees_Weighbridge_Fees'], total_going_details)
            sheet.write(row, 19, obj['Transit_fees_Peage'], total_going_details)
            sheet.write(row, 20, obj['Transit_fees_Levy_Council_Fee_Tunduma'], total_going_details)
            sheet.write(row, 21, obj['Transit_fees_Cargo_Rearrangement'], total_going_details)
            sheet.write(row, 22, obj['Transit_fees_Demurrage_Fee'], total_going_details)
            sheet.write(row, 23, obj['Driver_Trip_Allowance_Expense_Transit'], total_going_details)
            sheet.write(row, 24, obj['Transit_fees_Bond_going'], total_going_details)
            sheet.write(row, 25, obj['Transit_fees_TollRoad'], total_going_details)
            sheet.write(row, 26, obj['Transit_fees_GCLA_Loading_Facilitation_Other_going'], total_going_details)
            sheet.write(row, 27, obj['Toll_Gates_going'], total_going_details)
            sheet.write(row, 28, obj['Return_fees_Container_TAX_going'], total_going_details)
            sheet.write(row, 29, obj['Late_Exit_Note_going'], total_going_details)
            sheet.write(row, 30, obj['Carbon_Tax_going'], total_going_details)
            sheet.write(row, 31, obj['Return_fees_weight_pridje_going'], total_going_details)
            sheet.write(row, 32, obj['wating_charges_going'], total_going_details)
            sheet.write(row, 33, obj['total_going'], total_going_details)
            sheet.write(row, 34, obj['mbeya'], total_fuel_details)
            sheet.write(row, 35, obj['kibaha'], total_fuel_details)
            sheet.write(row, 36, obj['morogoro'], total_fuel_details)
            sheet.write(row, 37, obj['tunduma'], total_fuel_details)
            sheet.write(row, 38, obj['total_fuel'], total_fuel_details)
            sheet.write(row, 39, obj['Return_fees_Carrier_License'], total_return_details)
            sheet.write(row, 40, obj['Return_fee_Over_Stay'], total_return_details)
            sheet.write(row, 41, obj['Return_fees_Cargo_Rearrangement'], total_return_details)
            sheet.write(row, 42, obj['Return_fees_Radiation_Protection_Fee'], total_return_details)
            sheet.write(row, 43, obj['Return_fees_Weight_Check_Ndola'], total_return_details)
            sheet.write(row, 44, obj['Return_fees_Parking_Security_Fees'], total_return_details)
            sheet.write(row, 45, obj['Return_fee_Over_Stay'], total_return_details)
            sheet.write(row, 46, obj['Return_fees_Peage'], total_return_details)
            sheet.write(row, 47, obj['Return_fees_Entry_Card'], total_return_details)
            sheet.write(row, 48, obj['Return_fees_Kanyaka'], total_return_details)
            sheet.write(row, 49, obj['Return_fees_Levy_Council_Fee_Kapiri'], total_return_details)
            sheet.write(row, 50, obj['Return_fees_Penalty_over_wight'], total_return_details)
            sheet.write(row, 51, obj['Transit_fees_Bond'], total_return_details)
            sheet.write(row, 52, obj['Transit_fees_Road_Toll'], total_return_details)
            sheet.write(row, 53, obj['Transit_fees_GCLA_Loading_Facilitation_Other'], total_return_details)
            sheet.write(row, 54, obj['Toll_Gates'], total_return_details)
            sheet.write(row, 55, obj['Late_Exit_Note'], total_return_details)
            sheet.write(row, 56, obj['Return_fees_Container_TAX'], total_return_details)
            sheet.write(row, 57, obj['Carbon_Tax'], total_return_details)
            sheet.write(row, 58, obj['Return_fees_weight_pridje'], total_return_details)
            sheet.write(row, 59, obj['wating_charges'], total_return_details)
            sheet.write(row, 60, obj['Return_fees_Empty_Container_Offloading_Fees'], total_return_details)
            sheet.write(row, 61, obj['Return_fees_Visa'], total_return_details)
            sheet.write(row, 62, obj['Return_fees_Weight_Check_Tunduma'], total_return_details)
            sheet.write(row, 63, obj['Return_fees_Chemical_transportation'], total_return_details)
            sheet.write(row, 64, obj['Driver_Trip_Allowance_Expense_Return'], total_return_details)
            sheet.write(row, 65, obj['Return_fees_Parking_Security_Fees_ret'], total_return_details)
            sheet.write(row, 66, obj['Levy_council_fee_Tanzania'], total_return_details)
            sheet.write(row, 67, obj['Levy_council_fee_Kenya'], total_return_details)
            sheet.write(row, 68, obj['Mineral_Tax_Kenya'], total_return_details)
            sheet.write(row, 69, obj['Ferry_Fees'], total_return_details)
            sheet.write(row, 70, obj['total_return'], total_return_details)
            sheet.write(row, 71, obj['expenses'], bold)
            sheet.write(row, 72, obj['cross_profit'], bold)
            sheet.write(row, 73,
                        (round(obj['cross_profit'] / obj['operating_income'] * 100, 2)) if obj[
                                                                                               'operating_income'] != 0 else 0,
                        bold)

            # sheet.write(row, 13, obj['from_sum'])
