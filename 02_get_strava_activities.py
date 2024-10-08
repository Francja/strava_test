import requests
import pandas as pd

# Replace with your actual access token
access_token = 'dc140e91c376b4b1a599381d541a3c9f447d737b'

# Initialize variables
activities = []
page = 1
per_page = 50  # Number of activities per page (up to 200)
count = 1

while True:
    # Fetch the activities
    response = requests.get(
        'https://www.strava.com/api/v3/athlete/activities',
        headers={'Authorization': f'Bearer {access_token}'},
        params={'page': page, 'per_page': per_page}  # Pagination parameters
    )

    # Check the response status
    if response.status_code == 200:
        print(f"page:{count}")
        count+=1
        page_activities = response.json()

        if not page_activities:  # Stop if there are no more activities
            break

        activities.extend(page_activities)  # Add activities from this page to the list
        page += 1  # Move to the next page
    else:
        print(f"Failed to fetch activities: {response.status_code}, {response.text}")
        break

# Convert the JSON response to a pandas DataFrame
df = pd.DataFrame(activities)

# Check the columns of the DataFrame
print("DataFrame Columns:", df.columns)

# Display the first few rows of the DataFrame
print(df.head())

# Optionally, save the data to a CSV file
df.to_csv('strava_activities.csv', index=False)
