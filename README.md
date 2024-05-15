# woui
woui (short for Wireshark OUI) is a command line application written in Python
 meant to allow you to search the wireshark OUI while being offline!

**Until woui is updated more, it is quite limited in functionality!** Most 
searching **should work**, however please be aware that the logic used to match
the MAC address(s) is basically checking if either the MAC you passed to woui
or the MAC it found starts with the other. As far as I know, woui works,
however I have not written accuracy tests *yet* for the software. Therefore,
inaccuracies may occur.

I am not liable for any damanges that may be occured by this software - it is
provided AS IS and WITHOUT warranty.

# Updating the Data
To update the data that woui uses for searching, simply add the `-r` (or `
--refresh`) flag when calling the application:
```command
python -m woui -r
```

# Searching
To search for a vendor using a MAC address, use the following command:
```command
python -m woui <MAC>
```
If you'd like to also update the data used for the search before executing
then you can add the `-r` flag before passing the MAC address!
```command
python -m woui -r <MAC>
```