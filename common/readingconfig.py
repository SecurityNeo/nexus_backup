import os
import configparser

root_dir = os.path.dirname(os.path.abspath('.'))
cf = configparser.ConfigParser()

cf.read(root_dir + '/config.ini')

vip = cf.get("Platform", "vip")
port = cf.get("platform", "port")
repo = cf.get("Nexus", "repository")
admin_user = cf.get("Nexus", "username")
admin_password = cf.get("Nexus", "password")
backup_dir = cf.get("Backup", "backup_dir")
