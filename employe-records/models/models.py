from odoo import models, fields, api, _
from odoo.exceptions import UserError


class EmployeeRecord(models.Model):
    _name = "employee.record"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _discription = "employee record"
    #
    # @api.model
    # def default_get(self, fields):
    #     res = super(EmployeeRecord, self).default_get(fields)
    #     print(test)
    #     res['user_id'] = self.env.user.id
    #
    #     return res
    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char("Phone", copy=False)
    desigination = fields.Char(string='Desigination', required=True)
    employee_dob = fields.Date(string="Date of Birth")
    employee_gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')
    employee_image = fields.Binary("employee Image")

    user_id = fields.Many2one('res.users', string="recruiter", readonly=True, default=lambda self: self.env.uid)

    state = fields.Selection([
        ('new', 'New'),
        ('used', 'Used')], string='Status', readonly=True, default='new')


    @api.model
    def create(self, vals):
        # vals['state'] = 'new'
        return super(EmployeeRecord, self).create(vals)


    def state_changer(self):
        self.state = "used"
        msg = ("a new employee has been created")
        for s in self:
            s.message_post(body=msg)
            #   raise UserError("state of the record should be new")

    def delete_method(self):
        context = {}
        context['active_id'] = self.id
        return {'type': 'ir.actions.act_window',
                'name': _('Confirmation Message'),
                'res_model': 'delete.dialouge.wizard',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': context,
                }



    # def unlink(self):
    #      super("employee.record",self).unlink()
    #      return  {
    #              'warning': {
    #              'title': 'Warning!',
    #               'message': 'The warning text'}
    #               }
    #     def unlink(self):
    #         # code to delete
    #
    #         action = self.env["ir.actions.actions"]._for_xml_id("employe-records.employee_records_view_form.unlink")
    #         return action
    #
    #     def unlink(self):
    #         # ....        # ....
    #         # ....
    #         return {
    #             'warning': {
    #                 'title': 'Information',
    #                 'message': 'Testmessage!'
    #             }
    #         }

#
# def delete_record(self):
#     self.unlink()

# def delete_record(self):
#         self.with_context(active_test=False).project_ids.unlink()
#         return self.env["ir.actions.actions"]._for_xml_id("project.open_view_project_all_config")
