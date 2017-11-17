#!/usr/bin/env python3
import sys
def cul(salary):
   point = 3500
   five_one_money = salary*(0.08+0.02+0.005+0.06)
   rest_money = salary - five_one_money - point
   res_money = rest_money - five_one_money
   if rest_money <0:
      res_money = rest_money*0
   elif rest_money >0 and rest_money <= 1500:
        res_money = rest_money*0.03
   elif rest_money > 1500 and rest_money <= 4500:
        res_money = rest_money*0.1 -105
   elif rest_money > 4500 and rest_money <= 9000:
        res_money = rest_money*0.2 -555 
   elif rest_money > 9000 and rest_money <= 35000:
        res_money = rest_money*0.25 -1005
   elif rest_money >35000 and rest_money <= 55000:
        res_money = rest_money*0.3 -2755
   elif rest_money >55000 and rest_money <= 80000:
        res_money = rest_money*0.35 -5505
   elif rest_money >80000:
        res_money = rest_money*0.45 -13505
   re_money = salary - five_one_money - res_money
   return re_money
try:
    for arg in sys.argv[1:]:
        arg = arg.split(':')
        a_num = int(arg[0])
        b_salary = cul(int(arg[1]))
        print(str(a_num)+':'+format(b_salary,'.2f'))
except:
    print("Parameter Error")




    
