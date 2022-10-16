
# import the requests library
import requests

# Ask the user for a file name
file_name = input("Please enter the file name of the file that is gonna be created: ")

def get_cat_photo():
    # get the cat photo from the internet
    response = requests.get("https://cataas.com/cat")
    # save the cat photo to the current directory
    with open(str(f"{file_name}.jpg"), "wb") as file:
        file.write(response.content)
        file.close()
    print(f"Succesfuly Saved a Cat Photo with the file name: {file_name}.jpg!")

get_cat_photo()