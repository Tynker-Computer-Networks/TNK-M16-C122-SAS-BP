from helpers import get_random_url
import json
import socket


def ddos_attack(ip_address, port):
    try:
        # Create a socket and save it in ddos variable
        
        # Connect the socket using ip_address and port
        

        # Use get_random_url() function to generate random url and save it in random_url 
        

        # Use json.dumps() to convert random_url to json and then encode it and save it in message variable
        

        # Use send() and sendto() methods on ddos socket to send the message
        

        # Close the ddos socket
        
        pass

    except Exception as err:
        print(err)


def main():
    host = input("Site you want to DDoS:")
    port = int(input("Enter port number:"))

    # Use socket.gethostbyname(host) to get ip of the website's server and store it in ip_address variable

    print("|| DDoS Loaded ||")

    # Call ddos_attack function with ip and port
    


if __name__ == "__main__":
    main()
