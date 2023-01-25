def sort_by_year(movies):
    sorted_movies = sorted(movies, key=lambda x: (x['year'], x['title']), reverse=True)
    return [movie['title'] for movie in sorted_movies]


def sort_by_title(movies):
    def trim_movie(title):
        for no_no in ["The ", "A ", "An "]:
            if title.startswith(no_no):
                return title.replace(no_no, "", 1)
        return title
    sorted_movies = sorted(movies, key=lambda x: trim_movie(x['title']))
    return [movie['title'] for movie in sorted_movies]

# def sort_by_year(movies):
#     for i in range(len(movies)):
#         for j in range(i+1, len(movies)):
#             if movies[i]['year'] < movies[j]['year']:
#                 movies[i], movies[j] = movies[j], movies[i]
#     return movies
#
#
# def sort_by_title(movies):
#     for i in range(len(movies)):
#         for j in range(i+1, len(movies)):
#             title1 = movies[i]['title']
#             title2 = movies[j]['title']
#             if title1.startswith("A ") or title1.startswith("An ") or title1.startswith("The "):
#                 title1 = title1.replace("An ", "").replace("A ", "").replace("The ", "")
#             if title2.startswith("A ") or title2.startswith("An ") or title2.startswith("The "):
#                 title2 = title2.replace("An ", "").replace("A ", "").replace("The ", "")
#             if title1 > title2:
#                 movies[i], movies[j] = movies[j], movies[i]
#     return movies


