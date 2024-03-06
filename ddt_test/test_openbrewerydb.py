import requests
import pytest


# Получение списка всех пивоварен
def test_get_all_breweries():
    response = requests.get("https://api.openbrewerydb.org/breweries")
    assert response.status_code == 200
    breweries = response.json()
    assert len(breweries) > 0


# Получение списка пивоварен по штату
@pytest.mark.parametrize("state", ["California", "Colorado", "New York"])
def test_get_breweries_by_state(state):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_state={state}")
    assert response.status_code == 200
    breweries = response.json()
    assert len(breweries) > 0
    for brewery in breweries:
        assert brewery["state"] == state


# Получение списка пивоварен по типу
@pytest.mark.parametrize("brewery_type", ["micro", "brewpub", "regional"])
def test_get_breweries_by_type(brewery_type):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_type={brewery_type}")
    assert response.status_code == 200
    breweries = response.json()
    assert len(breweries) > 0
    for brewery in breweries:
        assert brewery["brewery_type"] == brewery_type


# Получение списка пивоварен по городу
@pytest.mark.parametrize("city", ["San Diego", "South Portland", "Denver"])
def test_get_breweries_by_city(city):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_city={city}")
    assert response.status_code == 200
    breweries = response.json()
    assert len(breweries) > 0
    for brewery in breweries:
        assert brewery["city"] == city


# Получение списка пивоварен по почтовому индексу
@pytest.mark.parametrize("postal_code", ["92101-6618", "97201-5125", "80202-6002"])
def test_get_breweries_by_postal_code(postal_code):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_postal={postal_code}")
    assert response.status_code == 200
    breweries = response.json()
    assert len(breweries) > 0
    for brewery in breweries:
        assert brewery["postal_code"] == postal_code
