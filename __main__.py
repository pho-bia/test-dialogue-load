from declutter import *

import sys

def debug_call():
	print(f'{BLUE} Line split: {DEBUG_DICT['events'] + END}')
	print(f'{GREEN}::: dia_diction event value: {DEBUG_DICT['events_iter'] + END}')
	print(f'{NEGATIVE}:::::: Current part: {DEBUG_DICT['part']} ({DEBUG_DICT['part_iter']}){END + LIGHT_PURPLE} -> {DEBUG_DICT['line']}{END}')
	print(f'::::::::: Completed text: \033[1;33m{DEBUG_DICT['complete_line']}\033[0m\n')

dialogue = open(sys.argv[1])

load_dialogue = false
line_entry = ''

dia_diction = {}
line = ''

for line in dialogue:
	line_entry = ''
	events = line.split(' ')

	dia_diction[events[0]] = [events[1], '']
	if DEBUG:
		DEBUG_DICT['events'] = str(events)
		DEBUG_DICT['events_iter'] = str(dia_diction[events[0]])

	iteration = 0
	for part in events:
		if DEBUG:
			DEBUG_DICT['part_iter'] = str(iteration)
			DEBUG_DICT['part'] = str(part)
			debug_call()

		if iteration <= 2:
			iteration += 1
			continue

		line_entry += ' ' + part if part[-1] != '\n' else part[:-1]
		iteration += 1

		if DEBUG:
			DEBUG_DICT['line'] = str(line_entry)
			debug_call()

	dia_diction[events[0]][1] = line_entry[1:]
	if DEBUG:
		DEBUG_DICT['complete_line'] = str(dia_diction[events[0]][1])
		debug_call()

print(dia_diction)