import requests

try:
    # Make API request to get a specific post
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    response.raise_for_status()  # Raise error if status is not 200
    
    data = response.json()
    
    # Extract and display post information
    post_id = data['id']
    title = data['title']
    body = data['body'][:100]  # First 100 characters
    user_id = data['userId']
    
    print(f"Post ID: {post_id}")
    print(f"Title: {title}")
    print(f"Body: {body}...")
    print(f"User ID: {user_id}")
    
except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")
except KeyError as e:
    print(f"Missing data field: {e}")
