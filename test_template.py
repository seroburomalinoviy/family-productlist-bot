from datetime import date
inp = 'продукты\nМолоко\nкартошка\nнидейка в упаковке'

txt = inp.split('\n')

template = f'''Список продутов от {date.today().strftime('%d %b (%A)')}\n\n'''
for i in txt:
    template += f'- {i.capitalize():<10} /отметить\n'

template += '\n/Отметить все\n\n#список_покупок'

print(template)


