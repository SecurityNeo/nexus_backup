import os
import requests

from common.readingconfig import backup_dir
from common.utils import md5sum


def download(asset):
    download_url = asset["download_url"]
    path = asset["path"]
    md5 = asset["md5"]
    target_file = os.path.join(backup_dir, path)
    if target_file.exists():
        actually_md5 = md5sum(target_file)
        if actually_md5 == md5:
            print("============The file {file} is exists,do not to need to "
                  "download==========").format(file=target_file)
            return 
        else:
            print("============The md5 of the  file {file} is {ac_md5}, but the md5 "
                  "in the nexus is {expect_md5}, delete the old file")\
                .format(file=target_file, ac_md5=actually_md5, expect_md5=md5)
            os.remove(target_file)
    rep = requests.get(download_url, stream=True)
    with open(target_file, 'wb') as f:
        for data in rep.iter_content():
            f.write(data)