from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    dict_jobs = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    for job in dict_jobs:
        assert 'title' in job.keys() and 'titulo' not in job.keys()
        assert 'salary' in job.keys() and 'salario' not in job.keys()
        assert 'type' in job.keys() and 'tipo' not in job.keys()
