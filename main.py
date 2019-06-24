# created: 11 May 2019
# author: Alexander Hungerford
# description: While Loops: accepting input &
#       letting the user choose when to quit.

# when you create a new project with PyCharm you can add VCS
# VCS > Import into Version Control > Share Project on Github

# define a prompt
prompt = '\nTell me something and I will repeat it. '
prompt += "Enter 'quit' to end the program.\n"

# set up a variable (empty string) to store whatever value the user enters
# this gives message an initial value
message = ""

# so long as user input does not equal 'quit'
while message != 'quit':
    message = input(prompt)
    print(message)
