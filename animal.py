import random

def animal_or_not(animal_done_set):
    """
    Generates three-letter combinations, occasionally picking real animal names.
    Keeps track of which animals have been seen and ensures new selections.
    Returns updated set of seen animals or "All Done!" when complete.
    
    Play Ideas:
    1. teach how code works
    2. child calls script
    3. if it is an animal: draw it
    4. if not, do something else (run in a circle)
    """
    # kludge clear screen
    print("\n" * 50)  # prints 50 blank lines
    
    print(f"So far: {animal_done_set}\n")
    
    # List of three-letter animal names
    three_letter_animal_names = [
        "pup", "dog", "cat", "rat", "fox",
        "hen", "bug", "ant", "fly", "pig",
        "bat", "cow", "hog", "ape", "owl",
        "bee", "hen", 
    ]
    
    if set(three_letter_animal_names) == animal_done_set:
        print("All Done!")
        return "All Done!"
    
    # 25% chance to just return a real animal name
    if random.random() < 0.25:
        # Get list of animals not yet seen
        available_animals = [animal for animal in three_letter_animal_names 
                           if animal not in animal_done_set]
        if available_animals:  # if there are still unseen animals
            word = random.choice(available_animals)
            animal_done_set.add(word)
            print(word, "\n")
            return animal_done_set
    
    
    # Create lists of letters from each position
    first_letters = list(set([name[0] for name in three_letter_animal_names]))
    second_letters = list(set([name[1] for name in three_letter_animal_names]))
    third_letters = list(set([name[2] for name in three_letter_animal_names]))
    
    # Add some common consonants and vowels if not already present
    extra_first = ['t', 'l', 'b', 'p', 's']
    # extra_second = ['a', 'e', 'i', 'o', 'u']
    extra_second = []
    # extra_third = ['t', 'p', 'd', 'g', 'n']
    extra_third = []
    
    first_letters.extend([x for x in extra_first if x not in first_letters])
    second_letters.extend([x for x in extra_second if x not in second_letters])
    third_letters.extend([x for x in extra_third if x not in third_letters])
    
    # Filter second_letters to only include vowels
    vowels = set('aeiou')
    second_letters = [letter for letter in second_letters if letter.lower() in vowels]
    
    # If no vowels in second_letters, add them
    if not second_letters:
        second_letters = list(vowels)
    
    
    # Generate random combination
    word = ''.join([
        random.choice(first_letters),
        random.choice(second_letters),
        random.choice(third_letters)
    ])
    
    # Check if it's a real animal name
    is_animal = word.lower() in [name.lower() for name in three_letter_animal_names]
    
    # print(f"{word} {'(animal)' if is_animal else '(not an animal)'}")
    # keep set of done
    if word in three_letter_animal_names:
        animal_done_set.add(word)
            
    print(word, "\n")
    
    return animal_done_set

def main():
    """
    Main function to generate and print random combinations of three letters.
    Print and wait for user to hit enter
    """
    done_set = set()
    while True:
    	# run and save result
        done_set = animal_or_not(done_set)
        
        if done_set == "All Done!":
            return "All Done!"
        
        # hit enter (or exits by typing "exit")
        exits = input()
        
        # user exists
        if exits == "exit":
            return "OK!"

if __name__ == "__main__":
    main()
