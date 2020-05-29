
# discord_airdrop
Distribute coins within Discord

Minimum environment:
- **Ubuntu 18.04+**  
- 1 vCore  
- 1024mb RAM  

## Setup swap file  
```bash
dd if=/dev/zero of=/swapfile count=2048 bs=1M
```

#### Activate the swap file
```bash
chmod 600 /swapfile
ls -lh /swapfile
mkswap /swapfile
```
#### Turn swap on
```bash
swapon /swapfile
```
## Python libraries
```bash
apt install python3-pip  
pip3 install discord.py  
pip3 install python-dateutil  
```
```bash
git clone https://github.com/jgarzik/python-bitcoinrpc.git
cd python-bitcoinrpc
python3 setup.py install
```
