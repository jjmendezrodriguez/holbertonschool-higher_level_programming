#!/usr/bin/python3
import requests
import csv

# Function to fetch and print posts
def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Print the status code of the response
    print('Status Code:', response.status_code)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the fetched data into a JSON object
        posts = response.json()
        
        # Iterate through the parsed JSON data and print out the titles of all the posts
        for post in posts:
            print(post['title'])

# Function to fetch and save posts to a CSV file
def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the fetched data into a JSON object
        posts = response.json()
        
        # Structure the data into a list of dictionaries
        structured_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        # Write the data into a CSV file
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(structured_data)

# Main function to call the defined functions
if __name__ == '__main__':
    fetch_and_print_posts()
    fetch_and_save_posts()
