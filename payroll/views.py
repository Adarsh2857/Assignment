from django.shortcuts import render
from .models import EmpAttendance, EmpBasicPay, EmpIncomeTax

def payroll_dashboard(request):
    emp_numbers = EmpBasicPay.objects.values_list('emp_no', flat=True).distinct()
    months = EmpAttendance.objects.values_list('month', flat=True).distinct()

    # Initialize session data if not already set
    if 'last_emp_no' not in request.session:
        request.session['last_emp_no'] = ''
    if 'last_month' not in request.session:
        request.session['last_month'] = ''
    if 'last_gross_pay' not in request.session:
        request.session['last_gross_pay'] = None
    if 'last_net_pay' not in request.session:
        request.session['last_net_pay'] = None

    if request.method == "POST":
        emp_no = request.POST['emp_no']
        month = request.POST['month']

        # Fetch basic pay
        basic_pay_record = EmpBasicPay.objects.filter(emp_no=emp_no).first()
        basic_pay = basic_pay_record.basic_pay if basic_pay_record else 0

        # Fetch income tax percentage
        income_tax_record = EmpIncomeTax.objects.filter(emp_no=emp_no).first()
        income_tax_percentage = income_tax_record.income_tax_percentage if income_tax_record else 0

        # Fetch number of days present
        attendance_record = EmpAttendance.objects.filter(emp_no=emp_no, month=month).first()
        days_present = attendance_record.days_present if attendance_record else 0

        # Calculate gross pay and net pay
        gross_pay = (basic_pay / 30) * days_present
        net_pay = gross_pay - (gross_pay * (income_tax_percentage / 100))

        # Store the last values in the session
        request.session['last_emp_no'] = emp_no
        request.session['last_month'] = month
        request.session['last_gross_pay'] = gross_pay
        request.session['last_net_pay'] = net_pay

    context = {
        'emp_numbers': emp_numbers,
        'months': months,
        'last_emp_no': request.session['last_emp_no'],
        'last_month': request.session['last_month'],
        'last_gross_pay': request.session['last_gross_pay'],
        'last_net_pay': request.session['last_net_pay'],
    }

    return render(request, 'payroll_dashboard.html', context)