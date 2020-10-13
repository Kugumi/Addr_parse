import PySimpleGUI as sg
# import tkinter as tk
# import tk-dev as tkdev

def interface(df):
	n = -1
	incorrect_counter = 0
	addr_parts = ['address', 'result_string', 'region', 'town', 'settlement', 'street', 'building', 'place']
	cbs = ['region', 'town', 'settlement', 'street', 'building', 'place']
	addr_found_dict = {'address': 0, 'result_string': 0, 'region': 0, 'town': 0, 'settlement': 0, 'street': 0, 'building': 0, 'place': 0}
	addr_true_found_dict = {'region_true': 0, 'town_true': 0, 'settlement_true': 0, 'street_true': 0,
					  'building_true': 0, 'place_true': 0}
	addr_not_found_dict = {'address': 0, 'result_string': 0, 'region': 0, 'town': 0, 'settlement': 0, 'street': 0, 'building': 0, 'place': 0}

	layout = [[sg.Text('Press Next to start', size=(100,0),key='nxt')],
			  [sg.Text('Address:        ', font='Any 18'), sg.Text('', size=(700, 0), key='address', font='Any 18')],
			  [sg.Text('Parsed address: ', font='Any 18'), sg.Text('', size=(700,0),key='result_string', font='Any 18')],
			  [sg.Button('ALL PARSED ITEMS ARE CORRECT', font='Any 18')],
			  [sg.Checkbox(text = 'Correct', key='region_true', font='Any 18'), sg.Checkbox(text = 'Not Parsed', key='region_false', font='Any 18'), sg.Text('Region:         ', font='Any 18'), sg.Text('', size=(100,0),key='region', font='Any 18')],
			  [sg.Checkbox(text = 'Correct', key='town_true', font='Any 18'), sg.Checkbox(text = 'Not Parsed', key='town_false', font='Any 18'), sg.Text('Town:           ', font='Any 18'), sg.Text('', size=(100, 0), key='town', font='Any 18')],
			  [sg.Checkbox(text = 'Correct', key='settlement_true', font='Any 18'), sg.Checkbox(text = 'Not Parsed', key='settlement_false', font='Any 18'), sg.Text('Settlement:     ', font='Any 18'), sg.Text('', size=(500, 0), key='settlement', font='Any 18')],
			  [sg.Checkbox(text = 'Correct', key='street_true', font='Any 18'), sg.Checkbox(text = 'Not Parsed', key='street_false', font='Any 18'), sg.Text('Street:         ', font='Any 18'), sg.Text('', size=(500, 0), key='street', font='Any 18')],
			  [sg.Checkbox(text = 'Correct', key='building_true', font='Any 18'), sg.Checkbox(text = 'Not Parsed', key='building_false', font='Any 18'), sg.Text('Building:       ', font='Any 18'), sg.Text('', size=(500, 0), key='building', font='Any 18')],
			  [sg.Checkbox(text = 'Correct', key='place_true', font='Any 18'), sg.Checkbox(text = 'Not Parsed', key='place_false', font='Any 18'), sg.Text('Place:          ', font='Any 18'), sg.Text('', size=(500, 0), key='place', font='Any 18')],
			  [sg.Button('Incorrect Address', font='Any 18'), sg.Button('Next', font='Any 18'), sg.Button('End', font='Any 18')]]

	# Create the Window
	window = sg.Window('Window Title', layout, size=(1500, 500))
	# Event Loop to process "events" and get the "values" of the inputs
	while True:
		event, values = window.read()
		if event == 'Next' or event == 'ALL PARSED ITEMS ARE CORRECT' or event == 'Incorrect Address':
			n += 1
			if event == 'Incorrect Address':
				incorrect_counter += 1
			elif event == 'ALL PARSED ITEMS ARE CORRECT':
				for cb in cbs:
					element = window.FindElement(cb)
					if element.get():
						addr_true_found_dict.update({cb + "_true": addr_true_found_dict.get(cb + "_true") + 1})
			elif event == 'Next':
				for cb in cbs:
					element = window.FindElement(cb + "_true")
					if element.get():
						addr_true_found_dict.update({cb + "_true": addr_true_found_dict.get(cb + "_true") + 1})
						# element.Update(value=False)

					element = window.FindElement(cb + "_false")
					if element.get():
						addr_not_found_dict.update({cb: addr_not_found_dict.get(cb) + 1})
						# element.Update(value=False)
			for addr_part in addr_parts:
				if window.FindElement(addr_part).get():
					addr_found_dict.update({addr_part: addr_found_dict.get(addr_part) + 1})
			if n == df.shape[0]:
				print(addr_found_dict)
				print(addr_true_found_dict)
				print(addr_not_found_dict)
				print(n)
				print(incorrect_counter)
				break
			element = window.FindElement('nxt')
			element.Update(value="INDEX " + str(n + 1) + "/" + str(df.shape[0]))
			for cb in cbs:
				element = window.FindElement(cb + "_true")
				element.Update(value=False)
				element = window.FindElement(cb + "_false")
				element.Update(value=False)
			for addr_part in addr_parts:
				element = window.FindElement(addr_part)
				x = df[df.index == n][addr_part].values[0]
				element.Update(value=x)
		if event == sg.WIN_CLOSED or event == 'End':  # if user closes window or clicks cancel
			print(addr_found_dict)
			print(addr_true_found_dict)
			print(addr_not_found_dict)
			print(n)
			print(incorrect_counter)
			break
		# print('You entered ', values[0])

	window.close()

