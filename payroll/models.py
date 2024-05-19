from django.db import models

class EmpAttendance(models.Model):
    emp_no = models.IntegerField()
    month = models.CharField(max_length=20)
    days_present = models.IntegerField()

    def __str__(self):
        return f"Emp No: {self.emp_no}, Month: {self.month}"

class EmpBasicPay(models.Model):
    emp_no = models.IntegerField()
    basic_pay = models.IntegerField()

    def __str__(self):
        return f"Emp No: {self.emp_no}, Basic Pay: {self.basic_pay}"

class EmpIncomeTax(models.Model):
    emp_no = models.IntegerField()
    income_tax_percentage = models.FloatField()

    def __str__(self):
        return f"Emp No: {self.emp_no}, Income Tax %: {self.income_tax_percentage}"