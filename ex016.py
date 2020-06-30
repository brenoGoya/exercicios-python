# Challenge 016

"""" Ask the user if it is raining and convert their answer to lower case so it doesn't matter what
case they type it in. If they answer "yes", ask if it is windy. If they answer "yes" to this 
second question, diplay the message "It is too windy for an umbrella", otherwise  display the 
message "Take an umbrella". If they did not answer yes to the first question, display the answer "Enjoy
your day". """

answer = input('Is it raining today?\n>> ').lower()
if answer == 'yes':
    second_answer = input('Is it windy?\n>> ').lower()
    if second_answer == 'yes':
        print('It is too windy for an umbrella.')
    else:
        print('Take an umbrella.')
else:
    print('Enjoy your day.')

