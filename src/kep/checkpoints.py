# NOT IMPLEMENTED:
#    - he have no coverage metrics - how many of the variables parsed are listed in checkpoints?
#    - checking time series not present in 1999 (INDPRO, PPI, some others) or discontinued ts 

ANNUAL_STR = """
year                                1999.0
AGROPROD_yoy                         103.8
CPI_ALCOHOL_rog                      143.2
CPI_FOOD_rog                         135.0
CPI_NONFOOD_rog                      139.2
CPI_SERVICES_rog                     134.0
CPI_rog                              136.5
EXPORT_GOODS_bln_usd                  75.6
GDP_bln_rub                         4823.0
GDP_yoy                              106.4
GOV_EXPENSE_CONSOLIDATED_bln_rub    1258.0
GOV_EXPENSE_FEDERAL_bln_rub          666.9
GOV_EXPENSE_SUBFEDERAL_bln_rub       653.8
GOV_REVENUE_CONSOLIDATED_bln_rub    1213.6
GOV_REVENUE_FEDERAL_bln_rub          615.5
GOV_REVENUE_SUBFEDERAL_bln_rub       660.8
GOV_SURPLUS_FEDERAL_bln_rub          -51.4
GOV_SURPLUS_SUBFEDERAL_bln_rub         7.0
IMPORT_GOODS_bln_usd                  39.5
INVESTMENT_bln_rub                   670.4
INVESTMENT_yoy                       105.3
RETAIL_SALES_FOOD_bln_rub            866.1
RETAIL_SALES_FOOD_yoy                 93.6
RETAIL_SALES_NONFOOD_bln_rub         931.3
RETAIL_SALES_NONFOOD_yoy              94.7
RETAIL_SALES_bln_rub                1797.4
RETAIL_SALES_yoy                      94.2
TRANSPORT_FREIGHT_bln_tkm           3372.0
UNEMPL_pct                            13.0
WAGE_NOMINAL_rub                    1523.0
WAGE_REAL_yoy                         78.0
INDPRO_yoy                             NaN
PPI_rog                                NaN
"""

QTR_STR = """
year                                                       1999.0
qtr                                                           1.0
AGROPROD_yoy                                                 97.2
CPI_ALCOHOL_rog                                             118.2
CPI_FOOD_rog                                                118.4
CPI_NONFOOD_rog                                             114.0
CPI_SERVICES_rog                                            109.5
CPI_rog                                                     116.0
EXPORT_GOODS_bln_usd                                         15.3
GDP_bln_rub                                                 901.0
GDP_yoy                                                      98.1
GOV_EXPENSE_CONSOLIDATED_bln_rub                            189.0
GOV_EXPENSE_FEDERAL_bln_rub                                 108.3
GOV_EXPENSE_SUBFEDERAL_bln_rub                               91.5
GOV_REVENUE_CONSOLIDATED_bln_rub                            171.9
GOV_REVENUE_FEDERAL_bln_rub                                  89.1
GOV_REVENUE_SUBFEDERAL_bln_rub                               93.6
GOV_SURPLUS_FEDERAL_bln_rub                                 -19.2
GOV_SURPLUS_SUBFEDERAL_bln_rub                                2.1
IMPORT_GOODS_bln_usd                                          9.1
INDPRO_rog                                                    NaN
INDPRO_yoy                                                    NaN
INVESTMENT_bln_rub                                           96.8
INVESTMENT_rog                                                NaN
INVESTMENT_yoy                                               93.8
I_EXSB_FUNDING_EXTERNAL_FUNDS_BUDGET_FEDERAL_bln_rub          3.3
I_EXSB_FUNDING_EXTERNAL_FUNDS_BUDGET_SUBFEDERAL_bln_rub       6.0
I_EXSB_FUNDING_EXTERNAL_FUNDS_BUDGET_bln_rub                 11.6
I_EXSB_FUNDING_EXTERNAL_FUNDS_bln_rub                        33.2
I_EXSB_FUNDING_OWN_FUNDS_bln_rub                             49.4
PPI_rog                                                       NaN
RETAIL_SALES_FOOD_bln_rub                                   186.8
RETAIL_SALES_FOOD_rog                                        85.0
RETAIL_SALES_FOOD_yoy                                        92.7
RETAIL_SALES_NONFOOD_bln_rub                                192.2
RETAIL_SALES_NONFOOD_rog                                     90.7
RETAIL_SALES_NONFOOD_yoy                                     84.3
RETAIL_SALES_bln_rub                                        379.0
RETAIL_SALES_rog                                             88.0
RETAIL_SALES_yoy                                             88.1
TRANSPORT_FREIGHT_bln_tkm                                   821.0
UNEMPL_pct                                                   14.3
WAGE_NOMINAL_rub                                           1248.0
WAGE_REAL_rog                                                80.9
WAGE_REAL_yoy                                                60.7"""

MONTHLY_STR="""
year                                1999.0
month                                  1.0
AGROPROD_yoy                          96.5
CORP_DEBT_OVERDUE_BUDGET_bln_rub     232.4
CORP_DEBT_OVERDUE_SUPPLIERS_bln_rub  583.5
CORP_DEBT_OVERDUE_bln_rub           1241.1
CORP_DEBT_bln_rub                   2347.0
CORP_RECEIVABLE_OVERDUE_bln_rub      772.0
CORP_RECEIVABLE_bln_rub             1550.6
CPI_ALCOHOL_rog                      109.7
CPI_FOOD_rog                         110.4
CPI_NONFOOD_rog                      106.2
CPI_SERVICES_rog                     104.1
CPI_rog                              108.4
EXPORT_GOODS_bln_usd                   4.5
GOV_EXPENSE_CONSOLIDATED_bln_rub      45.6
GOV_EXPENSE_FEDERAL_bln_rub           27.4
GOV_EXPENSE_SUBFEDERAL_bln_rub        22.7
GOV_REVENUE_CONSOLIDATED_bln_rub      49.0
GOV_REVENUE_FEDERAL_bln_rub           27.8
GOV_REVENUE_SUBFEDERAL_bln_rub        25.7
GOV_SURPLUS_FEDERAL_bln_rub            0.4
GOV_SURPLUS_SUBFEDERAL_bln_rub         3.0
IMPORT_GOODS_bln_usd                   2.7
INVESTMENT_bln_rub                    28.5
INVESTMENT_rog                        42.5
INVESTMENT_yoy                        92.2
RETAIL_SALES_FOOD_bln_rub             60.3
RETAIL_SALES_FOOD_rog                 82.5
RETAIL_SALES_FOOD_yoy                 90.3
RETAIL_SALES_NONFOOD_bln_rub          61.5
RETAIL_SALES_NONFOOD_rog              81.0
RETAIL_SALES_NONFOOD_yoy              79.0
RETAIL_SALES_bln_rub                 121.8
RETAIL_SALES_rog                      81.7
RETAIL_SALES_yoy                      84.0
TRANSPORT_FREIGHT_bln_tkm            277.7
UNEMPL_pct                            14.3
WAGE_NOMINAL_rub                    1167.0
WAGE_REAL_rog                         72.5
WAGE_REAL_yoy                         58.6
"""
from numpy import isnan

def from_year(year):    
    return str(int(year))

def from_month(year, month):
    year, month = int(year), int(month) 
    return f'{year}-{month}'

def from_qtr(year, qtr):
    month = qtr * 3
    return from_month(year, month)

def as_dict(s):
    result = {}
    for row in s.strip().split('\n'):
        d = [x for x in row.split(' ') if x] 
        val = float(d[-1])
        if not isnan(val):
            result[d[0]] = val
    return result

def extract_date(d):
    year = int(d.pop('year'))    
    if 'month' in d.keys():
        month = int(d.pop('month'))
        return from_month(year, month)
    elif 'qtr' in d.keys():
        qtr = int(d.pop('qtr'))
        return from_qtr(year, qtr)
    else:
        return from_year(year) 
    
def as_checkpoints(text):
    d = as_dict(text)
    dt_str = extract_date(d)
    return [dict(date=dt_str, 
                 name=name, 
                 value=d[name]) for name in d.keys()]

CHECKPOINTS = dict(   
    a = as_checkpoints(ANNUAL_STR),
    q = as_checkpoints(QTR_STR),
    m = as_checkpoints(MONTHLY_STR)  
)
        