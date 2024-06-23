import random
import base64
import gzip
import zlib
import bz2
import lzma
import lz4.frame
import urllib.parse
import base64
import time

# List of mutators
mutators = [
    lambda flag: flag[::-1],  # Reverse the flag
    lambda flag: ''.join(chr((ord(c) - 33 + 47) % 94 + 33) for c in flag),  # ROT47
    lambda flag: ''.join(chr(ord(c) + 1) for c in flag),  # Caesar Cipher with shift 1
    lambda flag: ''.join(chr(ord(c) - 1) for c in flag),  # Caesar Cipher with shift -1
    lambda flag: ''.join(chr(ord(c) ^ 0xFF) for c in flag),  # Bitwise XOR with 0xFF
    lambda flag: base64.b32encode(flag.encode()).decode(),  # Base32 Encoding
    lambda flag: urllib.parse.quote(flag),  # URL Encoding
    # Add more :)
]

# List of compression techniques
compression_techniques = [
    lambda data: gzip.compress(data.encode()),  # Gzip compression
    lambda data: zlib.compress(data.encode()),  # Zlib compression
    lambda data: bz2.compress(data.encode()),  # Bzip2 compression
    lambda data: lzma.compress(data.encode()),  # LZMA compression
    lambda data: lz4.frame.compress(data.encode()),  # LZ4 compression
    # Add more :)
]

def generate_ctf_flag(flag):
    mutator = random.choice(mutators)
    flag = mutator(flag)

    compression_technique = random.choice(compression_techniques)
    flag = compression_technique(flag)

    encoded_flag = base64.b64encode(flag).decode()

    return encoded_flag

def segment_flag(flag):
    segment_len = len(flag) // 4
    segments = [flag[i:i + segment_len] for i in range(0, len(flag), segment_len)]
    return segments

if __name__ == "__main__":
    flag = "BEGINNER{p0w3r_0f_fr13nd5h1p}"

    intro = '''
       _________                                                                        _________                                                                         
      (_,.....,_)                                                                      (_,.....,_)
        |||||||                                                                          |||||||
        |||||||                                                                          |||||||
        |||||||                 I am Larethor, Archmage of the arcane.                   |||||||
        |||||||                    Venture forth into the unknown!                       |||||||
        |||||||        Decrypt the Rune Fragments, each a shard of ancient magic.        |||||||    
        |||||||                 They guard the key to the prized Flag!                   |||||||
        |||||||                    Will you rise to the challenge?                       |||||||
        |||||||                      The realm's destiny awaits.                         |||||||
        |_____|               Begin your quest under Larethor's guidance!                |_____|
        )     (                                                                          )     (
       /       \                                                                        /       \\
     _/_________\_                                                                    _/_________\_
    |_____________|                                                                  |_____________|
    '''

    print(intro)
    input("\t\t\t\t\tAccept the quest?")
    print()
    for segment in segment_flag(flag):

        print(f"You have been given the rune: {generate_ctf_flag(segment)}")

    print("Good luck!")
