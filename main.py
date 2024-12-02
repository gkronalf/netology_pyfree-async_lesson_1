def get_info():
    date = input('Введите дату:')
    task = input('Введите задачу:')
    print_task(date, task)

def print_task(date, task):
    print(f'{date} {task}')

if __name__ == '__main__':
    get_info()
