import pandas as pd

from jinja2 import Environment, FileSystemLoader


# Načtení dat z Excelu

excel_file = 'specifikace.xlsx'

df = pd.read_excel(excel_file)


# Převedení dat na slovník

data = df.set_index('Kategorie')['Hodnota'].to_dict()


# Vytvoření HTML šablony

env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('template.html')


# Vygenerování HTML

output = template.render(data=data)


# Uložení do souboru

with open('output.html', 'w', encoding='utf-8') as f:

    f.write(output)


print("HTML soubor byl úspěšně vytvořen.")
