# printer_over_wifi

In this project we can host a printer in local area network so that any device can access the printer (actually i had a usb printer which due to some issues i was not able to share so i did this). It works fine on windows the printer function only supports windows more linux stuff to come.




## Installation


```bash
cd printer_over_wifi
```
```bash
virtualenv virtual_env
```
```bash
cd virtual_env/Scripts/
```
```bash
activate
```
```bash
pip install -r requirement.txt
```

Then edit the bat file with path where the project is present.
As the website is limited to windows now i have created
a bat file which fires the server and the website is availabe at the ip address specified to all the pcs in LAN.

Done!
