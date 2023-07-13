import requests
import aws

# Get the API key
api_key = aws.get_secret()

url = f"https://newsapi.org/v2/everything" \
      f"?q=splunk" \
      f"&apiKey={api_key}" \
      f"&sortBy=popularity" \
      # f"&from=2023-07-01" \
      #  f"&to=2023-07-11" \

request = requests.get(url)
content = request.json()

for article in content['articles']:
    print(article['title'])
    print(article['url'])
