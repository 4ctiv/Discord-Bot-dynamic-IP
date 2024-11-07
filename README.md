# Discord-Bot-dynamic-IP
## General info
Python Discord Bot for providing his host PC's global (dynamic) IP adress (ipv4).

> Note: 
> - Hand out your public IP **ONLY** to people you trust as this may allow bad people to do bad things. (Tough running a minraft server is a security risk on its own :P) 
> - This bot is just ment to be a quick (and dirty) way to give other people acces to your private minecraft server and is only really usefull if you have a dynamic ipv4 given by your provider. 
> - I did not add ipv6 to this as ipv6 has it's own ipv6 problems with firewalls and if you use this project you are likely to not have those configured correctly. (e.g. [ufw](https://wiki.ubuntuusers.de/ufw/) does not block [docker ipv6](https://docs.docker.com/engine/network/packet-filtering-firewalls/#docker-and-ufw) by default) 

## Requirements
REQUIRES: Phyton3.7+

## Usage
> To use this bot on your Server create a Discord Bot at: https://discordapp.com/developers/applications/
> - Add the clientID of your Bot in the clientID Variable in `GLOBALS.py`
> - Recommendation: Ensure `GLOBALS.py` is only realdable for you by doing the following:
>   - Windows: In explorer: `[Rightclick] GLOBALS.py -> permissions -> Security` (Then set access accoringly)
>   - Linux (MacOS): `chmod 600 GLOBALS.py`
