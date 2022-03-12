import bizdays
from bizdays import load_holidays
holidays = load_holidays('ANBIMA.txt')
cal = Calendar(holidays, ['Sunday', 'Saturday'], name = 'ANBIMA')
cal