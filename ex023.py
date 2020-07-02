# Challenge 023

""" Ask the user to type in the first line of a nursery rhyme and display the length of the string.
    Ask for a starting number and an ending number and then display just that section of the text 
    (remember Python starts counting from 0 and not 1). """

nursery = input('Enter the first line of a nursery rhyme:\n>> ').capitalize()
    
print(f'The lenght of the string: {len(nursery)} characters.')

start = int(input('Enter a starting number:\n>> '))

end = int(input('Enter a end number:\n>> '))

print(nursery[start:end])




