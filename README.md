

![alt text](https://bitg.org/wp-content/uploads/2020/04/bitgreen-logo-full.png)


Minimum environment:
- **Ubuntu 18.04+**  
- 1 vCore  
- 1024MB RAM  

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
pip3 install python-crontab  
pip3 install discord.py  
pip3 install python-dateutil  
```
```bash
git clone https://github.com/Nadro-J/tweepy.git
cd tweepy
python3 setup.py install
```
```bash
git clone https://github.com/jgarzik/python-bitcoinrpc.git
cd python-bitcoinrpc
python3 setup.py install
```
## Setting up PM2
```bash
apt install npm
npm install pm2 -g
pm2 start main.py --name airdrop --interpreter=python3
```
> All PM2 logs held in *`.pm2\logs`*
