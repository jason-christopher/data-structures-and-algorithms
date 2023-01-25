def sort_by_year(movies):
  for i in range(len(movies)):
    for j in range(i+1, len(movies)):
      if movies[i]['year'] < movies[j]['year']:
        movies[i], movies[j] = movies[j], movies[i]
  return movies

def sort_by_title(movies):
  for i in range(len(movies)):
    for j in range(i+1, len(movies)):
      title1 = movies[i]['title']
      title2 = movies[j]['title']
      if title1.startswith("A ") or title1.startswith("An ") or title1.startswith("The "):
        title1 = title1.replace("An ", "").replace("A ", "").replace("The ", "")
      if title2.startswith("A ") or title2.startswith("An ") or title2.startswith("The "):
        title2 = title2.replace("An ", "").replace("A ", "").replace("The ", "")
      if title1 > title2:
        movies[i], movies[j] = movies[j], movies[i]
  return movies
