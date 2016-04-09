import csv

class Movie:
    def __init__(self, movie_id, title):
        self.id = movie_id
        self.title = title
    #need id, movie name

    def __str__(self):
        return '{}: {}'.format(self.id, self.title)

class User:
    def __init__(self, row):
        self.user_id = row[0]
    #find all the user's ratings
    # find all movies the user has rated
    def __str__(self):
        return str(self.user)

class Rating:
    def __init__(self, row):
        self.user_id = row[0]
        self.movie_id = row[1]
        self.rating = row[2]
        # count the number of ratings per movie
        # find all ratings for a movie, add them together and divide the sum by the number of ratings
        # sort movies by rating average

    def __str__(self):
        return ('User: {}, Movie: {}, Rating: {}'.format(self.user_id, self.movie_id, self.rating))

movies = {}
with open('u.item', encoding='latin_1') as f:
    reader = csv.DictReader(f, fieldnames=['movie_id', 'title'], delimiter='|')
    for row in reader:
        movie = Movie(row['movie_id'], row['title'])
        movies[movie.id] = movie

def movie_by_name():
    movies_list = [movies[key] for key in movies]
    user_input = input('\nEnter part of a movie title: ').lower()
    print()
    for movie in movies_list:
        if user_input in movie.title.lower():
            print(movie)
movie_by_name()

users_list = []
with open('u.user', encoding='latin_1') as f:
    reader = csv.reader(f, delimiter = '|')
    for row in reader:
        users_list.append(User(row))

# for user in users_list:
#     print(user)

rating_list = []
with open('u.data', encoding='latin_1') as f:
    reader = csv.reader(f, delimiter = '\t')
    for row in reader:
        rating_list.append(Rating(row))

# for rating in rating_list:
#     print(rating)

def ratings_by_movie_id(ratings, movie_id):
    movie_ratings = []
    for rating in rating_list:
        if movie_id == rating.movie_id:
            movie_ratings.append(int(rating.rating))
    count = len(movie_ratings)
    average = sum(movie_ratings) / count
    print('\nNumber of user ratings: ', count)
    print('Average rating: ', "%.2f" % average)
    return movie_ratings

movie_id = input('\nEnter the movie ID number for the \nmovie you want to see ratings for: ')

id_sorted = ratings_by_movie_id(rating_list, movie_id)
