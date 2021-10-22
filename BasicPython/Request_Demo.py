import requests

# Get the HTML content
r = requests.get('https://google.com')
# print(r.text)


# Download the image
# re = requests.get('https://imgs.xkcd.com/comics/1_1000th_scale_world.png')
# with open('xkcdimage.png', 'wb') as f:
    # f.write(re.content)


# POST Request

payload = {'username': 'corey', 'password': 'test'}
r = requests.post('https://httpbin.org/post', data=payload)
r_dict = r.json()
print(r_dict['form'])