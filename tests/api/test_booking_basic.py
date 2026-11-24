import pytest


def test_get_booking_ids_returns_list(api, base_url):
    response = api.get(f"{base_url}/booking", timeout=15)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "bookingid" in data[0]


def test_get_booking_ids_basic_quality(api, base_url):
    response = api.get(f"{base_url}/booking", timeout=15)

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    assert response.elapsed.total_seconds() < 3


def test_create_booking_and_read_it_back(api, base_url, booking_payload):
    create_resp = api.post(f"{base_url}/booking", json=booking_payload, timeout=15)
    assert create_resp.status_code == 200
    booking_id = create_resp.json()["bookingid"]

    get_resp = api.get(f"{base_url}/booking/{booking_id}", timeout=15)
    assert get_resp.status_code == 200
    assert get_resp.json() == booking_payload


@pytest.mark.parametrize("bad_id", ["999999999", "0", "-1", "abc"])
def test_get_invalid_booking_id(api, base_url, bad_id):
    response = api.get(f"{base_url}/booking/{bad_id}", timeout=15)
    print(bad_id, response.status_code)
    assert response.status_code in (404, 400)