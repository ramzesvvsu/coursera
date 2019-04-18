import requests
import json
from datetime import datetime

def calc_age(uid):

    #user_id = '4480809'
    access_token = '3d6a2c075b65b406918e6f2d901b48c3007b83741a1986f58e50f1d455a6c0111f438f3a6ec59043204c9'
    r = requests.get(f'https://api.vk.com/method/users.get?v=5.71&access_token={access_token}&fields=bdate&user_ids={uid}')
    r_data = json.loads(r.text)
    id = r_data['response'][0]['id']
    #print(r.text)
    f = requests.get(
        f'https://api.vk.com/method/friends.get?v=5.71&access_token={access_token}&fields=bdate&user_id={id}')
    f_data = json.loads(f.text)
    result = {}
    current_year = datetime.now().year
    for current_friend in f_data['response']['items']:
        if 'bdate' in current_friend:
            bdate = current_friend['bdate'].split('.')
            if len(bdate) == 3:
                age = current_year - int(bdate[2])
                if age not in result:
                    result[age] = 0
                result[age] += 1
    result_values = sorted([(x, y) for x, y in result.items()], key=lambda x: x[0], reverse=False)
    result_values = sorted(result_values, key=lambda x: x[1], reverse=True)
    return result_values

if __name__ == '__main__':
    res = calc_age('lvklimenko')
    print(res)
