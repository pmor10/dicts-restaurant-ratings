"""Restaurant rating lister."""

def ratings_dictionary(filename):
    """Input a text file of restaurant ratings to return dictionary of ratings."""

    data = open(filename)

    restaurant_ratings = {}
    
    #Iterate through lines in file and adds key and value to dictionary
    for line in data:
        line = line.rstrip().split(":")
        restaurant_ratings[line[0]] = int(line[1])

    return restaurant_ratings

def sorted_ratings(filename):
    """Input a text file of ratings to return sorted print statements of ratings
    in original file only"""
    
    restaurant_ratings = ratings_dictionary(filename)

    # Iterate through the list to sort and write original ratings.
    for restaurant, rating in sorted(restaurant_ratings.items()):
        print(f'{restaurant} is rated at {rating}.')

def add_restaurant(filename):
    """User adds a restaurant to return sorted print statements of ratings
    including original file and user input.
    """

    restaurant_ratings = ratings_dictionary(filename)

    # print please add a rating 
    print("Please add a rating for the restaurant!")

    # Ask the user for the restaurant and rating
    restaurant = input("Enter a restaurant's name to rate: ")
    rating = int(input("Enter a rating for the restaurant (1-5): "))

    # print sorted_ratings including the new rating
    restaurant_ratings[restaurant] = rating

    # Iterate through the list to sort and write all ratings.
    for restaurant, rating in sorted(restaurant_ratings.items()):
        print(f'{restaurant} is rated at {rating}.')

add_restaurant('scores.txt')

