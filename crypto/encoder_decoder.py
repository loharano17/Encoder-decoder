#!/usr/bin/env python3
"""
Encoder_decoder.py
----------------------------

Command-line tool for encoding and decoding messages using Base64, Hexadecimal, and ASCII formats.
GitHub  : https://github.com/loharano17/Encoder-decoder

"""

import base64

def encode_base64(message: str) -> str:
    return base64.b64encode(message.encode()).decode()

def decode_base64(encoded: str) -> str:
    return base64.b64decode(encoded).decode()

def encode_hex(message: str) -> str:
    return message.encode().hex()

def decode_hex(encoded: str) -> str:
    return bytes.fromhex(encoded).decode()

def encode_ascii(message: str) -> str:
    return ' '.join(str(ord(c)) for c in message)

def decode_ascii(encoded: str) -> str:
    return ''.join(chr(int(c)) for c in encoded.split())

def menu():
    print("=== Encoder/Decoder CLI Tool ===")
    print("1. Encode to Base64")
    print("2. Decode from Base64")
    print("3. Encode to Hex")
    print("4. Decode from Hex")
    print("5. Encode to ASCII")
    print("6. Decode from ASCII")

def main():
    menu()
    choice = input("Choose an option (1-6): ").strip()

    if choice in ['1', '3', '5']:
        msg = input("Enter the message to encode: ")
    elif choice in ['2', '4', '6']:
        msg = input("Enter the message to decode: ")
    else:
        print("Invalid Option.")
        return

    try:
        actions = {
            '1': encode_base64,
            '2': decode_base64,
            '3': encode_hex,
            '4': decode_hex,
            '5': encode_ascii,
            '6': decode_ascii
        }
        result = actions[choice](msg)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
