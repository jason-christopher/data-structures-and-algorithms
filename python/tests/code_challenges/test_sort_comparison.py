import pytest
from code_challenges.sort_comparison import sort_by_title, sort_by_year


# @pytest.mark.skip("TODO")
def test_sort_by_title_exists():
  assert sort_by_title


# @pytest.mark.skip("TODO")
def test_sort_by_year_exists():
  assert sort_by_year


# @pytest.mark.skip("TODO")
def test_sort_by_year(movies):
  actual = sort_by_year(movies)
  expected = [{'title': 'An Ordinary Day', 'year': 2010}, {'title': 'Dodgeball', 'year': 2005}, {'title': "A Bug's Life", 'year': 1998}, {'title': 'The Apple', 'year': 1993}, {'title': 'Batman', 'year': 1989}]
  assert actual == expected


# @pytest.mark.skip("TODO")
def test_sort_by_title(movies):
  actual = sort_by_title(movies)
  expected = [{'title': 'The Apple', 'year': 1993}, {'title': 'Batman', 'year': 1989}, {'title': "A Bug's Life", 'year': 1998}, {'title': 'Dodgeball', 'year': 2005}, {'title': 'An Ordinary Day', 'year': 2010}]
  assert actual == expected


# @pytest.mark.skip("TODO")
def test_sort_by_year_empty():
  actual = sort_by_year([])
  expected = []
  assert actual == expected


# @pytest.mark.skip("TODO")
def test_sort_by_title_empty():
  actual = sort_by_title([])
  expected = []
  assert actual == expected


@pytest.fixture
def movies():
  movie_list = [{'title': 'Batman', 'year': 1989}, {'title': "A Bug's Life", 'year': 1998}, {'title': 'Dodgeball', 'year': 2005}, {'title': 'The Apple', 'year': 1993}, {'title': 'An Ordinary Day', 'year': 2010}]
  return movie_list
