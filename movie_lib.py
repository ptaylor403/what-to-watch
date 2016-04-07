import csv

class Movie:
    def __init__(self, row):
        self.id = row[0]
        self.title = row[1]
    #need id, movie name
    #u.item


class User:
    def __init__(self, row):
        self.user_id = row[0]
    #find all the user's ratings
    #u.user


class Rating:
    def __init__(self, row):
        self.user_id = row[0]
        self.movie_id = row[1]
        self.rating = row[2]
    # find all ratings for a movie, find how many ratings there are - add them together and divide the sum by the number of ratings
    # find all ratings for each movie and associate the rating with the user
    #calculate average rating for each movie
    #u.info


movie_list = []
with open('u.item', encoding='latin_1') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        movie_list.append(Movie(row))

# print(len(movie_list))

user_list = []
with open('u.user', encoding='latin_1') as f:
    reader = csv.reader(f, delimiter = '|')
    for row in reader:
        user_list.append(User(row))

# print(len(user_list))

rating_list = []
with open('u.data', encoding='latin_1') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        rating_list.append(Rating(row))

# print(len(rating_list))
    ##??
