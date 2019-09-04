import requests
import sys 
import keyboard

def get_chars(num):
    try:
        while True:
            yield requests.get("https://swapi.co/api/people/{}".format(num)).content
            num += 1
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


def main():
    was_pressed = False
    num = get_chars(1)

    while True:
        if keyboard.is_pressed('s'):
            if not was_pressed:
                print(next(num))
            
        else:
            was_pressed = False


if __name__ == '__main__':
     main()