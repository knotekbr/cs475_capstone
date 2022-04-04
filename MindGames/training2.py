import time, random
from pylsl import StreamInfo, StreamOutlet

# Stream metadata and outlet for pushing marker strings
info = StreamInfo('openbci_markers', 'Markers', 1, 250, 'string', 'liyfvutr4e87i6fu')
outlet = StreamOutlet(info)

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

# Total number of calibration rounds
num_rounds = 10
# Length, in seconds, of individual trials
trial_length = 2
# Track completed and total trials to display progress
completed_trials = 0
total_trials = num_rounds * len(trials)

# List containing integers corresponding to indices in var trials
trial_pool = []
for i in range(0, num_rounds):
    for j in range(0, len(trials)):
        trial_pool.append(j)

# Shuffle trial_pool to increase randomness of trial selection
random.shuffle(trial_pool)

if __name__ == '__main__':
    # Wait for user input to begin calibration
    input('Press Enter to begin calibration')

    # Push a marker indicating that calibration has started and enter calibration loop
    outlet.push_sample(['start_train'])
    while len(trial_pool) > 0:
        # Choose a trial at random and remove it from the list of trials
        rand_index = random.randint(0, len(trial_pool) - 1)
        curr_trial = trials[trial_pool.pop(rand_index)]
        completed_trials += 1

        # Alert user of the next trial
        print(f'\nNext trial: {curr_trial["text"]} ({completed_trials} / {total_trials})')
        start = time.perf_counter()
        while time.perf_counter() - start < 2:
            pass

        # Alert user that the trial is about to begin
        print('\tReady...')
        start = time.perf_counter()
        while time.perf_counter() - start < 1:
            pass

        # Prompt user to begin the trial
        print('\tGo')
        outlet.push_sample([curr_trial['marker']])
        start = time.perf_counter()
        while time.perf_counter() - start < trial_length:
            pass

    # Push a marker indicating that calibration has ended
    outlet.push_sample(['end_train'])
    print('Ending calibration...')