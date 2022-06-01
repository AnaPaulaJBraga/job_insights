from src.sorting import sort_by
import pytest


@pytest.fixture
def jobs():
    return [
        {
            "date_posted": "1994-06-15",
            "max_salary": "20000",
            "min_salary": "3000",
        },
        {
            "date_posted": "2000-07-27",
            "max_salary": "15000",
            "min_salary": "1500",
        },
        {
            "date_posted": "1995-01-29",
            "max_salary": "6000",
            "min_salary": "2000",
        },
        {"date_posted": "", "max_salary": "", "min_salary": ""},
    ]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == "1500"
    assert jobs[2]["min_salary"] == "3000"
    assert jobs[-1]["min_salary"] == ""

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == "20000"
    assert jobs[2]["max_salary"] == "6000"
    assert jobs[-1]["max_salary"] == ""

    sort_by(jobs, "date_posted")
    assert jobs[0]["date_posted"] == "2000-07-27"
    assert jobs[2]["date_posted"] == "1994-06-15"
    assert jobs[-1]["date_posted"] == ""
