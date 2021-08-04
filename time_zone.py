from datetime import datetime
import pytz

bogota_timezone = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_timezone)
print('Bogota: ', bogota_date.strftime("%d/%m/%y, %H:%M:%S"))

mexico_timezone = pytz.timezone('America/Mexico_City')
mexico_date = datetime.now(mexico_timezone)
print('Ciudad de Mexico: ', mexico_date.strftime("%d/%m/%y, %H:%M:%S"))

caracas_timezone = pytz.timezone('America/Caracas')
caracas_date = datetime.now(caracas_timezone)
print('Caracas: ', caracas_date.strftime("%d/%m/%y, %H:%M:%S"))




def format_timezone(date_format: str = "%d/%m/%y  %H:%M:%S", timezone: str ='America/Mexico_City', date: str='00/00/00 00:00:00') -> str:
    city_timezone = pytz.timezone(timezone)

    if date !='00/00/00 00:00:00':
        create_date = datetime.strptime(date, date_format)
    else:
        create_date = datetime.now(city_timezone)

    str_date = create_date.strftime(date_format)
    return str_date


mexico_date = '11/29/18 13:55:26'
mexico_timezone = 'America/Mexico_City'
print('-'*50)
print('Mandando una fecha')
print(format_timezone("%m/%d/%y %H:%M:%S", mexico_timezone, mexico_date))
print('-'*50)
print('Obteniendo la fecha actual')
print(format_timezone("%m/%d/%y %H:%M:%S", mexico_timezone))
