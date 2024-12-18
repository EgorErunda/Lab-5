import re
import csv

# Задание 3
with open('task3.txt', 'r', encoding='utf-8') as f:
    t3txt = f.read()

res_dateor = re.findall(r"\d{4}-\d{2}-\d{2}", t3txt)
t3txt = re.sub(r"\d{4}-\d{2}-\d{2}", ' ', t3txt)
res_url = re.findall(r"http\S+\w+", t3txt)
end_letters = {'.ne': '.net', '.inf': '.info', '.co': '.com', '.bi': '.biz', '.or': '.org'}
for i, url in enumerate(res_url):
    extension = url[url.rfind('.'):]
    res_url[i] = url.replace(extension, end_letters.get(extension, extension))
t3txt = re.sub(r"http\S+\w+", ' ', t3txt)
res_surname = re.findall(r"[A-Z][a-z]{1,7}", t3txt)
t3txt = re.sub(r"[A-Z][a-z]{1,7}", ' ', t3txt)
initial_res_email = re.findall(r'[a-z0-9]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', t3txt)
res_email = [re.sub(r'^\d+|\d+$', '', email) for email in initial_res_email]
res_id = list(range(1, 10001))
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Фамилия', 'Почта', 'URL', 'Дата регистрации'])
    for row in zip(res_id, res_surname, res_email, res_url, res_dateor):
        writer.writerow(row)

print("Task 3: watch file data.csv")