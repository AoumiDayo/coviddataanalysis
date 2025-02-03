import os
import pandas as pd
# Путь к папке с данными
data_path = "./datasets"

# Вывод списка файлов в папке
if os.path.exists(data_path):
    print("Содержимое папки с данными:")
    for file in os.listdir(data_path):
        print(file)
else:
    print(f"Папка {data_path} не найдена.")
    # Путь к файлу
file_path = os.path.join(data_path, "covid_19_clean_complete.csv")

# Чтение файла
try:
    df = pd.read_csv(file_path)
    print("Первые 5 строк датасета:")
    print(df.head())
except FileNotFoundError:
    print(f"Файл {file_path} не найден.")
    # Сводная информация о датасете
print("Общая информация о датасете:")
print(df.info())

# Подсчет общего количества случаев
total_confirmed = df['Confirmed'].sum()
total_deaths = df['Deaths'].sum()
total_recovered = df['Recovered'].sum()

print("\nОбщие статистики:")
print(f"Подтвержденные случаи: {total_confirmed}")
print(f"Смерти: {total_deaths}")
print(f"Выздоровления: {total_recovered}")

# Топ-5 стран по количеству подтвержденных случаев
top_countries = df.groupby('Country/Region')['Confirmed'].sum().nlargest(5)
print("\nТоп-5 стран по количеству подтвержденных случаев:")
print(top_countries)
import matplotlib.pyplot as plt
import seaborn as sns

# Группировка данных по странам
country_data = df.groupby('Country/Region').sum()[['Confirmed', 'Deaths', 'Recovered']].sort_values(by='Confirmed', ascending=False).head(10)

# Создание графика
plt.figure(figsize=(12, 8))
sns.barplot(x=country_data.index, y=country_data['Confirmed'], palette='viridis')
plt.title('Топ-10 стран по количеству подтвержденных случаев COVID-19')
plt.xlabel('Страна')
plt.ylabel('Количество подтвержденных случаев')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()