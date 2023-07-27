

async def test_create_user(client, get_user_from_database):
    user_data = {
      "name": "string",
      "email": "user_new@example.com"
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    resp = client.post("/user/", json=user_data, headers=headers)

    data_from_resp = resp.json()
    assert resp.status_code == 200
    assert data_from_resp["name"] == user_data["name"]
    assert data_from_resp["email"] == user_data["email"]

    users_from_db = await get_user_from_database(data_from_resp["user_id"])
    assert len(users_from_db) == 1
    user_from_db = dict(users_from_db[0])
    assert user_from_db["name"] == user_data["name"]
    assert user_from_db["email"] == user_data["email"]
    assert str(user_from_db["user_id"]) == data_from_resp["user_id"]


