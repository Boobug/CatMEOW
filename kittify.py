
import re
import requests
import random
import re
from bs4 import BeautifulSoup

def get_response(legends_url):
    response = requests.get(legends_url)
    return response.url


def check_valid_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if response.headers.get('content-type') in ['image/jpeg', 'image/png', 'image/gif']:
                return True
            else:
                return False
        else:
            return False
    except:
        return False



import re

def detect_emotion(emotion_str):
    # returns integers
    if re.match(r'^f[1-9]\d*$', emotion_str):
        # If so, extract the numeral and return it as an integer
        return int(emotion_str[1:])

    # Check if the input string matches any of the emotion keywords
    emotion_str = emotion_str.lower()
    if emotion_str == "default":
        return 0
    elif emotion_str == "hit":
        return 1
    elif emotion_str == "smile":
        return 2
    elif emotion_str == "troubled":
        return 3
    elif emotion_str == "cry":
        return 4
    elif emotion_str == "angry":
        return 5
    elif emotion_str == "bewildered":
        return 6
    elif emotion_str == "stunned":
        return 7
    elif emotion_str == "blaze":
        return 8
    elif emotion_str == "bowing":
        return 9
    elif emotion_str == "cheers":
        return 10
    elif emotion_str == "chu":
        return 11
    elif emotion_str == "dam":
        return 12
    elif emotion_str == "despair":
        return 13
    elif emotion_str == "glitter":
        return 14
    elif emotion_str == "hot":
        return 15
    elif emotion_str == "hum":
        return 16
    elif emotion_str == "love":
        return 17
    elif emotion_str == "oops":
        return 18
    elif emotion_str == "pain":
        return 19

    # If no match is found, return None
    return False



# def get_gender(name):
#     url = f"https://maplelegends.com/api/character?name={name}"
#     response = requests.get(url)
#     data = response.json()
#     gender = data["gender"]
#     return gender

def get_gender(name):
    gender_api_key = "your_gender_api_key_here"
    url = f"https://genderapi.io/api/?name={name}&key={gender_api_key}"
    response = requests.get(url)
    data = response.json()
    try:
        gender = data["gender"]
    except KeyError:
        gender = "female"  # default to female if gender not found in response
    return gender



def replace_item_id(link, replacement):
    # Find the index of the first occurrence of "itemId"
    start_index = link.find("itemId")
    if start_index == -1:
        return link  # "itemId" not found in link
    # Find the index of the colon (:) after "itemId"
    colon_index = link.find(":", start_index)
    if colon_index == -1:
        return link  # Colon not found after "itemId"
    # Find the index of the comma (,) after the colon
    comma_index = link.find(",", colon_index)
    if comma_index == -1:
        return link  # Comma not found after colon
    # Extract the item ID and replace the first 4 digits
    item_id = link[colon_index+1:comma_index].strip()
    new_id = replacement + item_id[4:]
    # Construct the new link with the replaced item ID
    return link[:colon_index+1] + new_id + link[comma_index:]

def replace_last_digit(url, new_digit):
    # Find the index of the first occurrence of "itemId"
    item_id_index = url.find("itemId")

    # If "itemId" is not found, return the original URL
    if item_id_index == -1:
        return url

    # Find the start index of the 5-digit number
    start_index = url.find(":", item_id_index) + 1

    # Find the end index of the 5-digit number
    end_index = url.find(",", start_index)

    # If the end index is not found, use the end of the string
    if end_index == -1:
        end_index = len(url)

    # Get the 5-digit number and replace the last digit
    number = url[start_index:end_index]
    new_number = number[:-1] + str(new_digit)

    # Replace the old number with the new number in the URL
    return url[:start_index] + new_number + url[end_index:]

# def hair_color_changing(url, color):
# def hair_color_changing(url_str, color):
#     if color == False:
#         return url_str
#     else:
#         color_dict = {
#             'BLACK': 0,
#             'RED': 1,
#             'ORANGE': 2,
#             'WHITE': 2,
#             'BLONDE': 3,
#             'GREEN': 4,
#             'BLUE': 5,
#             'PURPLE': 6,
#             'BROWN': 7,
#             0: 'BLACK',
#             1: 'RED',
#             2: 'WHITE',
#             2: 'ORANGE',
#             3: 'BLONDE',
#             4: 'GREEN',
#             5: 'BLUE',
#             6: 'PURPLE',
#             7: 'BROWN'
#         }
#         if isinstance(color, str):
#             color_str = color.upper()
#             if color_str not in color_dict:
#                 raise ValueError(f'Invalid color: {color}')
#             color_code = color_dict[color_str]
#         elif isinstance(color, int):
#             if color not in color_dict:
#                 raise ValueError(f'Invalid color code: {color}')
#             color_code = color
#         else:
#             raise TypeError(f'Invalid color type: {type(color)}')
#         new_url = replace_last_digit(url_str, color_code)
#         try:
#             response = requests.get(new_url)
#             response.raise_for_status()
#         except (requests.exceptions.HTTPError, requests.exceptions.RequestException) as e:
#             raise ValueError(f'Invalid URL or image not found: {new_url}') from e
#         return new_url
def get_optional_arg(url_str, arg_name):
    arg_value = re.findall(fr'{arg_name}=([^&]*)', url_str, re.IGNORECASE)
    return arg_value[0] if arg_value else None


def hair_color_changing(url_str, hair_color_change):
    if hair_color_change is None:
        return url_str

    color = get_optional_arg(url_str, 'color')
    if color is None:
        raise ValueError('No color specified for hair color change')

    color_code = hair_color_detect(color)
    if color_code is None:
        raise ValueError(f'Invalid color: {color}')

    # apply color change to image URL
    url_str = re.sub(r'(&bgColor=)([0-9])', r'\g<1>' + str(color_code), url_str)

    return url_str


def hair_color_detect(color_str):
    color_dict = {
        'BLACK': 0,
        'RED': 1,
        'ORANGE': 2,
        'WHITE': 2,
        'BLONDE': 3,
        'GREEN': 4,
        'BLUE': 5,
        'PURPLE': 6,
        'BROWN': 7
    }
    regex = re.compile('|'.join(color_dict.keys()), re.IGNORECASE)
    matches = regex.findall(color_str)
    if not matches:
        return False
    color_code = color_dict[matches[0].upper()]
    return color_code



def kittifying(url,ign_now):
    #let's combine everything nicely above
    if get_gender(ign_now) == 'female':
        hair_digit_4 = '3445'
    else:
        hair_digit_4 = '3343'
    return replace_item_id(url, hair_digit_4)


##this is the start of all the important request and url edits##



def get_avatar_image(input_str):
    variables = parse_input_string(input_str)
    ign = variables['ign']
    mount = variables['mount']
    animated = variables['animated']
    hair_color_change = variables['hair_color_change']
    detect_emotion_val = variables['detect_emotion']
    kittified = variables['kittify']
    # Create the URL string with the variables
    url = f'https://maplelegends.com/api/getavatar?name={ign}&mount={mount}&animated={animated}&face=f2'
    print(url)
    if detect_emotion_val != 2:
        url = url[:-1] + str(detect_emotion_val)
    # Get the image from the URL
    url = requests.get(url)
    url_str=url.url
    if kittified:
        url_str = kittifying(url_str, ign)
    if hair_color_change != 2 :
        url_str = hair_color_changing(url_str,hair_color_change)
    return url_str






def parse_input_string(input_str):
    variables = {'ign': None, 'mount': 0, 'animated': 0, 'hair_color_change': None, 'detect_emotion': 0, 'kittify': False}
    split_input = input_str.split(' ')
    variables['ign'] = split_input[0]

    for var in split_input[1:]:
        if var in ('mount', 'Mount'):
            variables['mount'] = 1
        elif var in ('animated', 'Animated'):
            variables['animated'] = 1
        elif var in ('kittify', 'Kittify'):
            variables['kittify'] = True
        elif hair_color_detect(var):
            variables['hair_color_change'] = hair_color_detect(var)
        elif detect_emotion(var):
            variables['detect_emotion'] = detect_emotion(var)

    return variables












#{'ign': None, 'mount': 0, 'animated': False, 'hair_color_change': None, 'detect_emotion': 0, 'kittify': False}
print(get_avatar_image('baeaf animated kittify f10'))

