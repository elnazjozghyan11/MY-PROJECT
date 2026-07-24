tasks = [

]
start =input('do you wanna start?and make new tasks?')
if start == 'no':
    print('ok,bye')
elif start =='yes':
    while True:
        task = input('enter your task: ')
        if task == 'exit':
            break
        tasks.append(task)
    show_tasks = input('do you wanna see tasks?')
    if show_tasks == 'no':
        print('ok,i do not care')
    elif show_tasks == 'yes':
        print('your tasks are:', tasks)
        print('do you wanna remove a task?')
    if input('yes/no: ').strip().lower() == 'yes':
        task_to_remove = input('enter the task you want to remove: ')
        if task_to_remove in tasks:
            tasks.pop(tasks.index(task_to_remove))
            print('task removed:', task_to_remove)
        else:
           print('task not found:', task_to_remove)
        print('your tasks are:', tasks)
    