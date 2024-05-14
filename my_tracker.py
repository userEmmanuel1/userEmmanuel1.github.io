import requests
import time
import smtplib
import ssl
from multiprocessing import Process
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 

global weekly
global timer
global selected_option
weekly =604800 
global daily 
daily = 86400

def run_stock_tracker(stocks, alert, timer, selected_option):
        # Email sender configuration
        smtp_port = 587 
        smtp_server = "smtp.gmail.com"
        email_from = "investiwatchers@gmail.com"
        email_to = alert
        pw = "kjru uvwz idmd cnjt"
        simple_email_context = ssl.create_default_context()
        global ticker
        # Stock tracker configuration
        ticker = stocks
        api_key = "71959a3173904d4cb215fe33857b2665"
        
        timer= timer
        selected_option = selected_option


        # Function to get stock price

        


        def get_stock_price(ticker_symbol, api):
            url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
            url2 = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
            response = requests.get(url).json()
            global initial_price
            initial_price = response['price'][:-2]
            print("$" + initial_price + " per share for " + ticker_symbol)
            print("Selected option :" + selected_option)
            return initial_price


        # Function to send notification
        def send_notification(message):
            try:
                TIE_server = smtplib.SMTP(smtp_server, smtp_port)
                TIE_server.starttls(context=simple_email_context)
                TIE_server.login(email_from, pw)

                print(f"Sending email to {email_to}")
                TIE_server.sendmail(email_from, email_to, message)
                print(f"Sent email to {email_to}")  
                #######REPLACE NUMBER WITH ALERT######
                resp = requests.post('https://textbelt.com/text', {
                    'phone': '',
                    'heading': 'STFU',
                    'message': message,
                    'key': 'cd2595248c0ac46913b132b3ff6f335fa996cd95BAfjSt35FbB3Nnp0X7oxtIJlE',
                })
                print(resp.json())

            except Exception as e:
                print(f"An error occurred: {e}")

            finally:
                TIE_server.quit()

        # Basic information about the stock
        price = get_stock_price(ticker, api_key)
        

        sell_price1 = price


        
        

        # Stock tracker loop
#       while sell_price1 :  # Change the loop condition
#           current_price = float(get_stock_price(ticker, api_key))

#    if price == price :
#        msg1 = f"""Check the stock {ticker}, probably SELL at {current_price}
#        You also selected: {selected_option} ,you can count on us to keep you updated! 
#        """
#        send_notification(msg1)
#        print("Notification sent.")

#    # Use pointers instead
#    sell_price1 = current_price * 0.95
#    sell_price2 = current_price * 0.90

#    ## Timer set in days
#    if timer.strip():  # strip() removes leading and trailing whitespaces
#        timer = int(timer) * 86400
#        time.sleep(timer)
#    else:
#        print('Stock tracker finished.')

# global target_percentage_gain  # Declare target_percentage_gain as a global variable

# def bullish_market(initial_price, target_percentage_gain):
   
#     if selected_option == 'Bullish Market':
#         selling_price = initial_price * (1 + target_percentage_gain / 100)
#         print ("IT WORKED ")
#         return selling_price
  
# def bearish_market(initial_price, target_percentage_loss):
#     if selected_option == 'Bearish Market':
#         selling_bear= initial_price * (1 + target_percentage_loss /100)
#         print("IT WORKED AGAIN!!!!!")
