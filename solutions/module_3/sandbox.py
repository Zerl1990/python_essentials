tasks = []
force_exit = False
total = 0
done = 0
while not force_exit:
    menu = (
        'Options:\n'
        '\t1) Add new task\n'
        '\t2) Delete task\n'
        '\t3) Get metrics\n'
        '\t4) Exit\n'
    )
    print(menu)
    selected_option = int(input('Please select an option from [1-4]: '))
    if selected_option == 1:
        name = input('New task name: ')
        tasks.append(name)
        total += 1
        print(f'Task added to list: {tasks[-1]}')
    elif selected_option == 2:
        print(f'Available tasks: {tasks}')
        index = int(input(f'Please select a task to remove [0-{len(tasks)-1}]: '))
        tmp = tasks[index]
        del tasks[index]
        print(f'Task {tmp} deleted!')
        done += 1
    elif selected_option == 3:
        print(f'TOTAL: {total}')
        print(f'DONE: {done}')
        print(f'ACTIVE: {len(tasks)}')
    elif selected_option == 4:
        force_exit = True
    else:
        print(f'Please Select a valid option from [0-4], selected {selected_option}')
