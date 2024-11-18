from random import choice, triangular
import json
import os
# Составляем списки мужских и женских имен, фамилий и название штата сша для дальнейшей генерации 
m_name = ['John', 'Michael', 'William', 'David', 'Richard',
         'Joseph', 'Thomas', 'Charles', 'Christopher', 'Daniel',
         'Matthew', 'Anthony', 'Mark', 'Paul', 'Steven']
fm_name = ['Mary', 'Elizabeth', 'Jennifer', 'Linda', 'Barbara', 
           'Susan', 'Jessica', 'Sarah', 'Karen', 'Lisa',
           'Nancy', 'Margaret', 'Donna', 'Michele', 'Laura']
surname = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 
           'Miller', 'Davis', 'Wilson', 'Moore', 'Taylor', 
           'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 
           'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 
           'Clark', 'Lewis', 'Lee', 'Walker', 'Hall', 
           'Allen', 'Young', 'Hernandez', 'King', 'Wright']
state =  ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 
'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 
'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 
'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 
'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 
'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 
'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 
'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 
'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']


def generate_values(n):
    arr = []
    # цикл для генерации случайноого списка    
    for n in range(1,n+1):
        arr.append(( 
                    choice([*m_name, *fm_name]),
                    choice(surname),
                    choice(state),
                    # будем брать возраст работающего населения, с модой - 30
                    int(triangular(18, 65, mode=30))))
    return arr
# Делаем возможность указывать размер сгенерированного списка через переменную окружения 
# или используем значение по умолчанию - 50
values = generate_values(int(os.environ.get('VALUES_SIZE',50)))
# Сохранение данных в файл
with open('/app/data/values.json', 'w') as f:
    json.dump(values, f)