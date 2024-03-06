import requests
import pytest


# Получение списка всех пород собак
def test_get_all_breeds():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response.status_code == 200
    breeds = response.json()["message"]
    assert len(breeds) > 0


# Получение случайной фотографии собаки
def test_get_random_dog_image():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"].startswith("https://")


# Получение списка случайных фотографий определенной породы собак
@pytest.mark.parametrize("breed", ["hound", "bulldog", "retriever"])
def test_get_random_images_by_breed(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random/3")
    assert response.status_code == 200
    assert len(response.json()["message"]) == 3
    for image_url in response.json()["message"]:
        assert image_url.startswith("https://")


# Получение списка всех подпород определенной породы собак
@pytest.mark.parametrize("breed", ["hound", "bulldog", "retriever"])
def test_get_all_subbreeds(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/list")
    assert response.status_code == 200
    subbreeds = response.json()["message"]
    assert len(subbreeds) > 0


# Получение случайной фотографии определенной подпороды собаки
@pytest.mark.parametrize("breed, sub_breed", [("hound", "afghan"), ("bulldog", "boston"), ("retriever", "golden")])
def test_get_random_image_by_sub_breed(breed, sub_breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"].startswith("https://")
