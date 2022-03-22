import time, random
from pylsl import StreamInfo, StreamOutlet

# Stream metadata and outlet for pushing marker strings
info = StreamInfo('openbci_markers', 'Markers', 1, 250, 'string', 'liyfvutr4e87i6fu')
outlet = StreamOutlet(info)
# Total number of calibration rounds
num_rounds = 10
# Length, in seconds, of individual trials
trial_length = 5

if __name__ == '__main__':
    # Wait for user input to begin calibration
    input('Press Enter to begin calibration')

    # Push a marker indicating that calibration has started and enter calibration loop
    outlet.push_sample(['start_train'])
    for i in range(1, num_rounds + 1):
        # Prompt text and associated marker for each trial to be completed
        trials = [
            {
                'text': 'Left Arm',
                'marker': 'train_left'
            },
            {
                'text': 'Right Arm',
                'marker': 'train_right'
            },
            {
                'text': 'Hard Blink',
                'marker': 'train_up'
            },
            {
                'text': 'Jaw Clench',
                'marker': 'train_down'
            },
            {
                'text': 'Neutral',
                'marker': 'train_neutral'
            }
        ]

        print(f'\nCalibration round {i} of {num_rounds}')
        # Wait 2 seconds before beginning first trial
        start = time.perf_counter()
        while time.perf_counter() - start < 2:
            pass

        # Loop as long as uncompleted trials remain
        while len(trials) > 0:
            # Choose a trial at random and remove it from the list of trials
            rand_index = random.randint(0, len(trials) - 1)
            curr_trial = trials.pop(rand_index)

            # Prompt user to begin trial and push associated marker
            print(f'\t{curr_trial["text"]} - Train for {trial_length} seconds')
            outlet.push_sample([curr_trial['marker']])
            # Wait for trial to end
            start = time.perf_counter()
            while time.perf_counter() - start < trial_length:
                pass

            # Alert user that the trial has ended
            print('\tStop')
            # Wait 2 seconds before beginning next trial
            start = time.perf_counter()
            while time.perf_counter() - start < 2:
                pass

    # Push a marker indicating that calibration has ended
    outlet.push_sample(['end_train'])
    print('Ending calibration...')