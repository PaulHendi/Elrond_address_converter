# We need Erdpy
from erdpy.accounts import Address


def erd_to_hex(erd_address) : 
    return Address(erd_address).hex()

def hex_to_erd(hex_address) : 
    return Address(hex_address).bech32()

# Test
sc_address = "erd1qqqqqqqqqqqqqpgqajrn8x33yf56gf3h72juk63t2znza90rkewqvlgv44"

# Should not return any error and continue the program
assert(hex_to_erd(erd_to_hex(sc_address)) == sc_address) 