import time
from pylsl import StreamInfo, StreamOutlet

info = StreamInfo('openbci_markers', 'Markers', 1, 250, 'string', 'liyfvutr4e87i6fu')
outlet = StreamOutlet(info)

if __name__ == '__main__':
    start = time.perf_counter()

    print('Calibration beginning in 10 seconds')
    while time.perf_counter() - start < 10:
        pass

    outlet.push_sample(['start_train'])
    for i in range(1, 6):
        print(f'\nCalibration round {i} of 5')

        print('Visualize holding your left arm out')
        outlet.push_sample(['train_left'])
        start = time.perf_counter()
        while time.perf_counter() - start < 5:
            pass

        print('Visualize holding your right arm out')
        outlet.push_sample(['train_right'])
        start = time.perf_counter()
        while time.perf_counter() - start < 5:
            pass

        print('Visualize standing up as tall as possible')
        outlet.push_sample(['train_up'])
        start = time.perf_counter()
        while time.perf_counter() - start < 5:
            pass

        print('Visualize crouching down as low as possible')
        outlet.push_sample(['train_down'])
        start = time.perf_counter()
        while time.perf_counter() - start < 5:
            pass

        print('Relax')
        outlet.push_sample(['train_neutral'])
        start = time.perf_counter()
        while time.perf_counter() - start < 5:
            pass

    outlet.push_sample(['end_train'])
    print('Ending calibration...')