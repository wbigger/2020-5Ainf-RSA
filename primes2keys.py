from primes import primes
from rsa import generate_keypair

keys = [generate_keypair(p,q) for (p,q) in primes.values()]

for prv,pub in keys:
    print prv
    print pub
    print pub
    print pub
    
