
def range_visualizer(stop):
    range_visualizer(0, stop, 1)


def range_visualizer(start, stop, step=1):
    print(f'range({start}, {stop}, {step})')
    print(f'\tStart: {start}\n\tStop: {stop}\n\tStep: {step}')
    time_line = []
    for num in range(start, stop, step):
        time_line.append(f'[{num}]')
    print('-'.join(time_line))


range_visualizer(1, 10, 1)

