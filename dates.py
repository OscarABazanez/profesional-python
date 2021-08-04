from datetime import datetime

# Obteniendo la fecha actual del ordenador o Coordinated Universal Time (UTC).
print('Obteniendo la fecha actual')
my_time = datetime.now()
print(my_time)
print('-'*50)


print('Obteniendo la fecha actual')
my_day = datetime.today()
print(my_day)
print(f'Year: {my_day.year}')
print(f'Month: {my_day.month}')
print(f'Day: {my_day.day}')
print('-'*50)

# Formateo de fechas
    # %Y    Year
    # %m    Month
    # %d    Day
    # %H    Hour
    # %M    Minute
    # %S    Second

print('Formateo de fechas')
my_day = datetime.now()
my_str = my_day.strftime('%d/%m/%y')
print(f'Formato LATAM: {my_str}')

my_str = my_day.strftime('%m/%d/%y')
print(f'Formato USA: {my_str}')

my_str = my_day.strftime('Estamos en el año %y')
print(f'Formato Random: {my_str}')
print('-'*50)
