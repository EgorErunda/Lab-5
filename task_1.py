import re

# task 1
pattern = r'\b\d{4,}(?:\.\d+)?(?<!\.)\b'

with open('task1-en.txt', 'r') as file:
    txt_task = file.read()
initial_nums = re.findall(r"[-+]?(?:\d+(?:\."
                            r"\d*)?|\.\d+)(?:[eE][-+]?\d+)?", txt_task)
res_numbers = [nums for nums in initial_nums if len(nums)>=4]
words3 = re.findall(r"\b\w{3}\b", txt_task)
words4 = re.findall(r"\b\w{4}\b", txt_task)
words5 = re.findall(r"\b\w{5}\b", txt_task)

print(res_numbers, words3, words4, words5, sep='\n')


