import requests


def get_token(client_id, client_secret):
    '''
    Get a temporary token from your client id app and clint secret app

    :param client_id: (str)
    :param client_secret: (str)
    :return: (str) a token
    '''
    r = requests.post(
        f"https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials")
    data = r.json()
    return data['access_token']


def get_user(token, client_id, user):
    '''
    Get information of a user

    :param token: (str) token from get_token method
    :param client_id: (str)
    :param user: (str) user in twitch
    :return: information of the user in json format
    '''
    r = requests.get(f"https://api.twitch.tv/helix/users?login={user}",
                     headers={'Authorization': f'Bearer {token}', 'Client-Id': client_id})

    data = r.json()
    return data


if __name__ == "__main__":
    pass
    # print(get_user(get_token(client_id, client_secret),client_id, "solary"))
