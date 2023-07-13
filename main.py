import requests
import aws
import send_mail

# Get the API key
secrets = aws.get_secret()
api_key = secrets['news_api_key']

url = f"https://newsapi.org/v2/everything" \
      f"?q=splunk" \
      f"&apiKey={api_key}" \
      f"&sortBy=popularity" \
      # f"&from=2023-07-01" \
      #  f"&to=2023-07-11" \

request = requests.get(url)
content = request.json()

email_content = "<html><body>"

for article in content['articles']:
    email_content += "<p><b>" + article['title'] + "</b><br>" + article['url'] + "</p><br>"

email_content += "</body></html>"

# send the message via the server set up earlier.
send_mail.s.send_message(send_mail.msg)
send_mail.s.quit()
