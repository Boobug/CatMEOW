
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


def get_gender(name):
    url = f"https://maplelegends.com/api/character?name={name}"
    response = requests.get(url)
    data = response.json()
    gender = data["gender"]
    return gender


def get_avatar_image(ign, gender):
    url = f'https://maplelegends.com/api/getavatar?name={ign}&mount=0&animated=0&face=f2'
    
    # Set the headers with randomized User-Agent and Referrer Policy
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8'
    ]
    headers = {
        'User-Agent': random.choice(user_agents),
        'Referer': 'https://maplelegends.com',
        'Referrer Policy': 'strict-origin-when-cross-origin'
    }

    # Send a GET request to the URL with the headers
    response = requests.get(url, headers=headers)
    return response.url


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



def kittify(ign_now):
    #let's combine everything nicely above
    if get_gender(ign_now) == 'female':
        hair_digit_4 = '3445'
    else:
        hair_digit_4 = '3343'
    avatar_url = get_avatar_image(ign_now, get_gender(ign_now))
    if check_valid_url(avatar_url):
        return replace_item_id(avatar_url, hair_digit_4)
    else:
        raise ValueError("Invalid URL or image format")


def detect_color(text):
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
    matches = regex.findall(text)
    if matches:
        return color_dict[matches[0].upper()]
    return None

def hair_color_change(url, color):
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
    matches = regex.findall(color)
    if not matches:
        raise ValueError(f'Invalid color: {color}')
    color_code = color_dict[matches[0].upper()]
    new_url = replace_last_digit(url, color_code)
    try:
        response = requests.get(new_url)
        response.raise_for_status()
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException) as e:
        raise ValueError(f'Invalid URL or image not found: {new_url}') from e
    return new_url



print(hair_color_change(kittify('kaza'), 'BlAcK'))
