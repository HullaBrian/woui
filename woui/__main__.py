import argparse
import os
import re

from urllib.request import urlretrieve


def get_data():
    path = "/".join(os.path.realpath(__file__).split(os.sep)[:-1])
    url = "https://www.wireshark.org/download/automated/data/manuf"
    filename = os.path.join(path, "wireshark_oui.txt")
    urlretrieve(url, filename)


parser = argparse.ArgumentParser()
parser.add_argument(  # Refresh data
    "-r",
    "--refresh",
    action="store_true",
    help="Pulls an updated MAC database"
)
parser.add_argument(  # Param for MAC addresses
    "MAC",
    help="Specify the MAC address that you want to search for"
)
args = parser.parse_args()

if args.refresh:  # Refresh data if desired
    print("Refreshing MAC database from wireshark...", end="")
    get_data()
    print("Done!")

path = "/".join(os.path.realpath(__file__).split(os.sep)[:-1])
search = re.compile(r"([^\s]+)")
with open(os.path.join(path, "wireshark_oui.txt"), "r") as file:
    for line in file.readlines():
        if line.startswith("#"):  # Exclude commented lines
            continue
        data = search.findall(line)  # Find data fields
        mac_block = data[0]
        if mac_block.startswith(args.MAC):  # Check MAC block
            # vendor_short = data[1]
            vendor_long = " ".join(data[2:])
            print(f"[{mac_block}]: {vendor_long}")
        