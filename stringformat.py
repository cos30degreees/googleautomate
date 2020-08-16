def format_name(first_name, last_name):
	# code goes here
    if len(first_name) > 0 and len(last_name) > 0:
        string = 'Name: {}, {}'.format(last_name, first_name)
    elif len(first_name) > 0:
        string = 'Name: {}'.format(first_name)
    elif len(last_name) > 0:
        string = 'Name: {}'.format(last_name)
    else:
        string = ""
    return string

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
def decade_counter():
	while year < 50:
		year += 10
	return year
