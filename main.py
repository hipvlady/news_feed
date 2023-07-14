import requests
from datetime import datetime, timedelta
import aws
import statics
from send_mail import send_msg


# Get the API key
secrets = aws.get_secret()
api_key = secrets['news_api_key']
current_topic = statics.topics[0]  # Get the topic splunk vs grammarly
base_url = statics.url

# Get the current date and date 14 days ago
current_date = datetime.now()
date_minus_14 = current_date - timedelta(days=14)

# Format the dates
current_date_formatted = current_date.strftime('%Y-%m-%d')
result_date_string = date_minus_14.strftime('%Y-%m-%d')

# Form the request URL
request_url = f"{base_url}?q={current_topic}&apiKey={api_key}" \
              f"&sortBy={statics.sortBy}" \
              f"&from={result_date_string}" \
              f"&to={current_date_formatted}" \
              f"&language={statics.language}" \

# Make the request
response = requests.get(request_url)
content = response.json()

# Build the email content
email_content = "<html><body>"

for article in content['articles'][:30]:
    email_content += f"<p><b>{article['title']}</b><br>{article['url']}</p><br>"

email_content += "</body></html>"

# Send the email
send_msg(email_content)
