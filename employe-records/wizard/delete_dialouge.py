from odoo import models, fields, api


class DeleteDialouge(models.TransientModel):
    _name = "delete.dialouge.wizard"
    _description = "employee record"

    message = fields.Text( required=True, default="Are You Sure Want To Delete ?", readonly=True )

    # def unlink(self):
    #     super(EmployeeRecord,self).unlink()
    def confirm_delete(self):
        rec = self.env.context.get('active_id')
        self.env['employee.record'].search([('id', '=', rec)]).unlink()
