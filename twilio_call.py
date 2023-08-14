from twilio.rest import Client
def main():
    
    account_sid = '****'
    auth_token = '*****'


    client = Client(account_sid, auth_token)


    with open('callingNumber.txt', 'r') as txt_file:
        to_number = txt_file.read()
    
    
    from_number = '****'


    with open('response.txt', 'r', encoding='utf-8') as f:
        resp = f.read()


    message = client.messages \
                    .create(
                        body=resp,
                        from_=from_number,
                        to=to_number
                    )

    print(message.sid)
if __name__ == "__main__":
    main()