from primes import primes
from rsa import generate_keypair
from blabel import LabelWriter

records_prv = []
records_pub = []

for prime in primes:
    p,q = primes[prime]
    (prv,pub) = generate_keypair(p,q)
    pdict = dict(name=f"{prime} prv",key=prv)
    records_prv.append(pdict)
    pdict = dict(name=f"{prime} pub",key=pub)
    records_pub.append(pdict)

label_writer = LabelWriter(
    "item_template.html", items_per_page=3, default_stylesheets=("style.css",)
)

# print(records)
label_writer.write_labels(records_prv, target='barcode_and_label_prv.pdf')
label_writer.write_labels(records_pub, target='barcode_and_label_pub.pdf')
