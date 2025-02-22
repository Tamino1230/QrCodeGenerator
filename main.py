import qrcode
import os
import time

def safe_input(msg: str, datatype = str, min_length = 0, max_length = 1000):
    while True:
        try:
            text = input(msg)
            value = datatype(text)
            if value == "":
                print("Input cannot be empty")
                continue
            if datatype == str:
                if len(text) < min_length:
                    print(f"Input must be at least {min_length} characters long")
                    continue
                elif len(text) > max_length:
                    print(f"Input must be at most {max_length} characters long")
                    continue
            elif datatype in [int, float]:
                if value < min_length:
                    print(f"Input must be at least {min_length}")
                    continue
                elif value > max_length:
                    print(f"Input must be at most {max_length}")
                    continue
            return value
        except ValueError:
            print(f"Invalid input. Please only {datatype.__name__} is allowed")

def generate_qr_code():
    paths = []
    amount = safe_input("Enter the number of QR codes to generate: ", int, 1)
    for i in range(amount):
        url = safe_input(f"{i+1}. Enter the URL: ", str).lstrip().rstrip()
        url.replace(" ", "_")
        try:
            if not os.path.exists("saved_qrcodes"):
                os.mkdir("saved_qrcodes")
            img = qrcode.make(url)
            path = f"saved_qrcodes/{i+1}_qrcode_{url}.png"
            img.save(f"saved_qrcodes/{i+1}_qrcode_{url}.png")
            paths.append(path)
        except Exception as e:
            print("An error occurred while generating the QR code. Please try again.", e)
    return paths

if __name__ == "__main__":
    while True:
        paths = generate_qr_code()
        print("QR code generated successfully")
        print("QR code saved at: ", end="")
        for path in paths:
            path.replace(" ", "_")
            print(f" {path}", end="")
        time.sleep(1)
        response = safe_input("Do you want to generate another QR code [y/n]: ", str)
        if response.lower() != "y":
            time.sleep(1)
            print("By Tamino1230...")
            time.sleep(1)
            print("Exiting..")
            time.sleep(1)
            break
        else:
            continue