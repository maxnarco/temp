 
from pexels_api import API
import os
import requests



def pexel_search_image(search_query):

    # Type your Pexels API
    PEXELS_API_KEY = 'kv3T8dLUUk9TNXDgVVSQKiZqLWpmVu05QcAhAIxSHpzxdSvTJYx6uozS '
    
    api = API(PEXELS_API_KEY)
    
    api.search(search_query, page=1, results_per_page=1)
    
    photos = api.get_entries()
    
    photo_url=' '
    for photo in photos:
    # Print photographer
    #   print('Photographer: ', photo.photographer)
    #   # Print url
    #   print('Photo url: ', photo.url)
    #   # Print original size url
        photo_url=photo.original
    return photo_url
  
  
def download_image_file(photo_url):
    
    url=photo_url
    directory_path = "stock_image"
    file_name = "image.jpeg"

    # Create the directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    file_path = os.path.join(directory_path, file_name)

    response = requests.get(url)

    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        print("File downloaded and saved successfully.")
    else:
        print("Failed to download the file. Status code:", response.status_code)
  
  
download_image_file(pexel_search_image('An elephant'))