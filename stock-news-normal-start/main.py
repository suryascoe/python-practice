from twilio.rest import Client
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_parameters = {
    "apikey": "3QPIYMMYP23T6F99",
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME
}
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_parameters = {
    "apiKey": "93aa1d488b13447ea8e875895204bea8",
    "q": COMPANY_NAME,
    "language": "en",
    "searchIn": "title"
}
account_sid = 'ACd0086696efce5ec5ae71e1e67602a517'
auth_token = 'Your Auth Token'


# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# Get yesterday's closing stock price.
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing = yesterday_data["4. close"]

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing = day_before_yesterday_data["4. close"]

# Find the positive difference between 1 and 2.
difference = float(yesterday_closing) - float(day_before_yesterday_closing)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price the day before
# yesterday.
diff_percentage = round((difference / float(yesterday_closing)) * 100)

# If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percentage) > 1:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_data = news_response.json()

    # Use Python slice operator to create a list that contains the first 3 articles.
    three_articles = news_data["articles"][:3]

    # Create a new list of the first 3 articles headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percentage}%.\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)

    client = Client(account_sid, auth_token)
    # Send each article as a separate message via Twilio.
    for article in formatted_articles:
        message = client.messages.create(
            from_='+15736854664',
            body=article,
            to='Your Number'
        )
