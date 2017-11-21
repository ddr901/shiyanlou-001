import sys
import csv
from collections import namedtuple

IncomeTaxQuickLookupItem = namedtuple(
    'IncomeTaxQuickLookupItem',
    ['start_point', 'tax_rate', 'quick_subtractor']
)

jibengongzi = 3500

INCOME_TAX_QUICK_LOOKUP_TABLE = [
    IncomeTaxQuickLookupItem(80000, 0.45, 13505),
    IncomeTaxQuickLookupItem(55000, 0.35, 5505),
    IncomeTaxQuickLookupItem(35000, 0.30, 2755),
    IncomeTaxQuickLookupItem(9000, 0.25, 1005),
    IncomeTaxQuickLookupItem(4500, 0.2, 555),
    IncomeTaxQuickLookupItem(1500, 0.1, 105),
    IncomeTaxQuickLookupItem(0, 0.03, 0)
]


class Args(object):

    def __init__(self):
        self.args = sys.argv[1:]

    def _value_after_option(self, option):
        try:
            index = self.args.index(option)
            return self.args[index + 1]
        except (ValueError, IndexError):
            print('Parameter Error')
            exit()
        @property
        def config_path(self):
            return self._value_after_option('-c')

        @property
        def userdata_path(self):
            return self._value_after_option('-d')

        @property
        def export_path(self):
            return self._value_after_option('-o')

args = Args()

class Config(object):
    def __init__(self):
        self._config = {}
        with open('d:\config.cfg','r') as f:
            for s in f.readlines() :
                (key ,value ) = s.strip().split(' = ')
                try:
                    self._config[id] = float(value)
                except ValueError:
                    print('ValueError')
                    exit()
    def _get_config(self,key):
        return self._config[key]
    @property
    def JiShuL(self):
        return self._config('JiShuL')

    @property
    def JiShuH(self):
        return self._config('JiShuH')

    @property
    def fivexian(self):
        return sum([
            self._get_config('YangLao'),
            self._get_config('YiLiao'),
            self._get_config('ShiYe'),
            self._get_config('GongShang'),
            self._get_config('ShengYu'),
            self._get_config('GongJiJin')])

config = Config()

class UserData(object):
    def __init__(self):
        userdata = []
        with open('d:\cuser.csv','r') as f:
            for s in f.readlines():
                (employee_id, income_string) = s.strip().split(',')

                try:
                    gongzi = int(income_string)
                except ValueError:
                    print('ValueError')
                    exit()
                userdata.append((employee_id,gongzi))
        return userdata
    def __iter__(self):
        return iter(self.userdata)

class IncomeTaxCalculator(object):
    def __init__(self,userdata):
        self.userdata = userdata
    @staticmethod
    def get_shehuibaoxian(gongzi):
        if gongzi < config.JiShuL():
            return config.JiShuL() * config.fivexian()
        if gongzi >config.JiShuH():
            return config.JiShuH() * config.fivexian()
        return gongzi * config.fivexian()
    @classmethod
    def gerensuodeshui(cls,gongzi):
        shehuibaoxian = cls.get_shehuibaoxian(gongzi)
        shiji_gongzi = gongzi - shehuibaoxian
        nashui = shiji_gongzi - jibengongzi
        if nashui <= 0:
            return '0.00', '{:.2f}'.format(shiji_gongzi)
        for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
            if nashui > item.start_point:
                tax = nashui * item.tax_rate - item.quick_subtractor
                return '{:.2f}'.format(tax), '{:.2f}'.format(shiji_gongzi - tax)

    def calc_for_all_userdata(self):
        result = []
        for employee_id, income in self.userdata:
            data = [employee_id, income]
            social_insurance_money = '{:.2f}'.format(self.calc_social_insurance_money(income))
            tax, remain = self.calc_income_tax_and_remain(income)
            data += [social_insurance_money, tax, remain]
            result.append(data)
        return result

    def export(self, default='csv'):
        result = self.calc_for_all_userdata()
        with open('d:\gongzi.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)

#if __name__ == '__main__':
    #calculator = IncomeTaxCalculator(UserData())
    #calculator.export()
    
