import csv

with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    data = list(reader)[1:]

project_id = input()
while project_id != 'СТОП':
    founded = False
    for id,Name, titleProject_id, clas, score in data:
        if titleProject_id == project_id:
            Name = Name.split()
            surname = Name[0]
            name = Name[1][0]
            print(f'Проект № {titleProject_id} делал: {name}. {surname} он(а) получил(а) оценку - {score}')
            founded = True
    if not founded:
        print('Ничего не найдено')
    project_id = input()
