#basic payroll converter from USD to Bitcoin w/commission
__author__='Marty Wilk || DWS'
#base hr/week
BASE_HOURS=40
#overtime multiplier
OT_MULTIPLIER=1.5
#withholding for tax
WITHHOLDING_RATE=0.25
#commission rate
COMMISSION_RATE=0.05
#input the hours worked, the hourly pay rate, sales amount and the current bitcoin price
hours=float(input('Enter the number of hours worked this week: '))
pay_rate=float(input('Enter the hourly pay rate: '))
sales_amount=float(input('Enter the Sales amount: '))
btc=float(input('Enter the current price of Bitcoin: '))
commission_amount=sales_amount*COMMISSION_RATE
#calculate gross pay and print
if hours >BASE_HOURS:
    #overtime pay
    overtime_hours=hours-BASE_HOURS
    overtime_pay=overtime_hours*pay_rate*OT_MULTIPLIER
    #gross pay
    gross_pay=BASE_HOURS*pay_rate+overtime_pay+commission_amount
else:
    #no overtime pay
    gross_pay=hours*pay_rate+commission_amount
#calculate withholdings,commission, net pay,and Bitcoin pay
withholdings=gross_pay*WITHHOLDING_RATE
net_pay=gross_pay-withholdings
#gross pay priced in Bitcoin
gross_satoshis=gross_pay/btc
btc_withholdings=gross_satoshis*WITHHOLDING_RATE
btc_commission_amount=commission_amount/btc
net_satoshis=gross_satoshis-btc_withholdings
#print gross pay, withholdings, net pay, satoshi price
print('Gross pay $ ', format(gross_pay, ',.2f'), sep='')
print('Current withholdings are $ ', format(withholdings, ',.2f'), sep='')
print('Commission earned $ ', format(commission_amount, ',.2f'), sep='')
print('Net pay is $ ', format(net_pay, ',.2f'), sep='')
print('Gross ₿ ', format(gross_satoshis,',.8f'),' satoshis', sep='')
print('Current withholdings are ₿ ', format(btc_withholdings,',.8f'),' satoshis', sep='')
print('Commission earned ₿ ', format(btc_commission_amount, ',.8f'),' satoshis', sep='')
print('Net ₿ ', format(net_satoshis,',.8f'),' satoshis', sep='')


