import requests

client_id = "92nbijbjqmva7avblj2ioubxs7572z"
client_secret = "p29grwwbarugrwhsuu5wurgz8wpub4"
user = "solary"


def get_token(client_id, client_secret):
    r = requests.post(
        f"https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials")
    data = r.json()
    return data['access_token']


def get_user(token, user):
    r = requests.get(f"https://api.twitch.tv/helix/users?login={user}",
                     headers={'Authorization': f'Bearer {token}', 'Client-Id': client_id})

    data = r.json()
    return data


if __name__ == "__main__":
    print(get_user(get_token(client_id,client_secret), "solary"))
