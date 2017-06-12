# ccie-lab-tools
Some tools for management of ccie lab environment

#### deploy-config.py
Download and put all INE initial configs on file/web server and push them with this script. The script asks for url to directory, choose the lab and provide url, example http://10.0.0.50/INE/advanced.technology.labs/basic.bgp.routing/

Note the configs from INE needs a bit of work before they can be used. Remove no login from vty lines, remove ip address from Gi2, remove commands including serial number etc.

#### reset-routers_fast.py  
Reset all routers without reboot. You need a locally stored base config for this on all routers, see base-config.txt.

#### reset-routers_slow.py
Reset all routers with reboot. You need a locally stored base config for this on all routers, see base-config.txt.

#### wr-all.yml
The name says it.

#### send-commands.yml
Send arbitrary commands to all routers.

#### auto-connect.sh
Used with screen.
