tasks =[

]
while True:
    add_task = input("enter your tasks: ")
    if add_task == 'exit':
        break
    tasks.append(add_task)
show_tasks = input('do you want to see your tasks? (yes/no): ').strip().lower()
if show_tasks == 'yes':
    print('your tasks are:')
    number = 1
    for task in tasks:
        print(number, task)
        number += 1
    task_to_remove = input('do you want to remove any task? (yes/no): ').strip().lower()
    if task_to_remove == 'yes':
        task_number = int(input('enter the task number you want to remove: '))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f'task removed: {removed_task}')
        else:
            print('invalid task number')
elif show_tasks == 'no':
    print('go away')
else:
    print('just(yes/no)')