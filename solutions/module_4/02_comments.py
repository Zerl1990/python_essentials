import random


def emulate_activity(iterations):
    tasks = init_tasks()
    for iteration in range(iterations):
        add_rnd_tasks(tasks)
        task = consume_tasks(tasks)
        print(f'Executed task: {task}')


def init_tasks():
    return [1, 3, 4, 1, 4, 5, 6, 7, 9]


def consume_tasks(tasks):
    if len(tasks) > 0:
        tasks.sort()
        task = tasks.pop()
        return task
    else:
        return None


def add_rnd_tasks(tasks):
    total = random.randint(10)
    for task in range(total):
        add_task(tasks, task)


def add_task(tasks, task):
    tasks.append(task)


emulate_activity(100)