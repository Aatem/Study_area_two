import pytest


@pytest.fixture()
def separator():
    print('=' * 10)
    yield 'value'
    print('finish')


#выполняется в рамках всей сессии
@pytest.fixture(scope='session')
def all_tests():
    print('before')
    yield
    print('after')