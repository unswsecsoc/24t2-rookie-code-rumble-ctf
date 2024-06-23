import pickle
import base64
import sys

def main():
    while True:
        try:
            encoded = input("I'm pickle riiiiiick: ").split()[0]
            decoded = base64.b64decode(encoded)
            pickle.loads(decoded)
        except Exception as e:
            print("Still a pickle..")
            continue
        except KeyboardInterrupt:
            sys.exit(1)


if __name__ == "__main__":
    main()