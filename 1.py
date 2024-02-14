import csv

with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    data = list(reader)[1:]
    class_summ = {}
    class_count = {}
    for id, name, titleProject_id, clas, score in data:
        if 'Хадаров Владимир' in name:
            print(f'Ты получил: {score}, за проект - {titleProject_id}')
        if score != 'None':
            class_summ[clas] = class_summ.get(clas, 0) + int(score)
            class_count[clas] = class_count.get(clas, 0) + 1

for i in range(len(data)):
    id, name, titleProject_id, clas, score = data[i]
    if score == 'None':
        data[i] = [id, name, titleProject_id, clas, round(class_summ[clas] / class_count[clas], 3)]

with open('students_new.csv', 'w', encoding='utf8') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
    writer.writerows(data)
