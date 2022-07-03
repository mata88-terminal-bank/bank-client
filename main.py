from requests import send_request

# Self explanatory, keep sending the commands as prompted
def main():
    print("WELCOME TO THE TERMINAL BANK!")
    print("Type 'exit' at any point to exit")
    print("REQ:")
    request = input()

    while request != "exit":
        send_request(request)

        print("REQ:")
        request = input()

if __name__ == "__main__":
    main()

