from ecdsa import SigningKey, SECP256k1
from multiprocessing import Pool, cpu_count

def recover_key_parallel(args):
    """Recover private key using parallel processing."""
    r, z_s_inv, r_s_inv, pub_key, n, k_range = args
    for k in k_range:
        try:
            # Calculate private key: priv = (r * k - z) * s_inv mod n
            priv = (r_s_inv * k - z_s_inv) % n
            
            # Verify key by regenerating public key
            key = SigningKey.from_secret_exponent(priv, curve=SECP256k1)
            if key.get_verifying_key().to_string().hex() == pub_key:
                return priv, k
        except:
            continue
    return None, None

def main():
    # Known values
    r = 0xf5c26eee36e47b5ac824254398e1b82e2baaf53c645366bdd0b359e2cd01c010
    s = 0x67d6e273e289285360d49961152d599581446bbda5286e912073ac5f27ef266e
    z = 0x8389f34c98c606322740c0be6a7125d9860bb8d5cb182c02f98461e5fa6cd15
    pub_key = "024b0faa9624763002e963816b2f6774df0dedd770896a9511cb5c9d90f674ecda"

    # Curve order (n) and modular inverse of s
    n = SECP256k1.order
    s_inv = pow(s, -1, n)

    # Precompute values to reduce redundant calculations
    r_s_inv = (r * s_inv) % n
    z_s_inv = (z * s_inv) % n

    # Divide the range of k into chunks for parallel processing
    num_cores = cpu_count()
    step = 65536 // num_cores  # Divide 65536 into equal chunks for each core
    ranges = [(r, z_s_inv, r_s_inv, pub_key, n, range(i * step, (i + 1) * step)) for i in range(num_cores)]

    print(f"Using {num_cores} CPU cores for parallel processing...")

    # Use multiprocessing to search for the private key in parallel
    with Pool(num_cores) as pool:
        results = pool.map(recover_key_parallel, ranges)

    # Check results from all processes
    for priv, k in results:
        if priv:
            print(f"Found private key: {hex(priv)}")
            print(f"Nonce k: {hex(k)}")
            return

    print("Private key not found in the search range.")

if __name__ == "__main__":
    main()