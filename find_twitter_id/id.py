# Import Tweepy
import tweepy

# Twitter API credentials
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJM6yAEAAAAAUKARBnLa2kET%2BeTX3kzUs34Nx%2Bc%3D7QwNGBBL6WjcDHaavjg8VgOseA0JrYINQVfH2GjZRx0uBTybhF'

# Initialize Tweepy client
client = tweepy.Client(bearer_token=bearer_token)

# Function to get user ID
def get_twitter_user_id(username):
    try:
        user = client.get_user(username=username)
        return f"User ID for @{username} is {user.data.id}"
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    username = 'Flame__live'  # Replace with the actual Twitter username
    result = get_twitter_user_id(username)
    print(result)
