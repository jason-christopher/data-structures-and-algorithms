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
    expected = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_sort_by_title(movies):
    actual = sort_by_title(movies)
    expected = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"]
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
    movie_list = [
        {
            "title": "Beetlejuice",
            "year": 1988,
            "genres": ["Comedy", "Fantasy"],
        },
        {
            "title": "The Cotton Club",
            "year": 1984,
            "genres": ["Crime", "Drama", "Music"],
        },
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genres": ["Crime", "Drama"],
        },
        {
            "title": "Crocodile Dundee",
            "year": 1986,

            "genres": ["Adventure", "Comedy"],
        },
        {
            "title": "Valkyrie",
            "year": 2008,
            "genres": ["Drama", "History", "Thriller"],
        },
        {
            "title": "Ratatouille",
            "year": 2007,
            "genres": ["Animation", "Comedy", "Family"],
        },
        {
            "title": "City of God",
            "year": 2002,

            "genres": ["Crime", "Drama"],
        },
        {
            "title": "Memento",
            "year": 2000,

            "genres": ["Mystery", "Thriller"],
        },
        {
            "title": "The Intouchables",
            "year": 2011,

            "genres": ["Biography", "Comedy", "Drama"],
        },
        {
            "title": "Stardust",
            "year": 2007,
            "genres": ["Adventure", "Family", "Fantasy"],
        },
    ]
    return movie_list
