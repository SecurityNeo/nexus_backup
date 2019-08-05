import os
import requests
from gevent import monkey
from gevent.pool import Pool

from common.readingconfig import backup_dir
from common.utils import md5sum
from tasks.grab_data import grab_components
monkey.patch_all()


def download(download_url, path, md5):
    target_file = os.path.join(backup_dir, path)
    if os.path.exists(target_file):
        actually_md5 = md5sum(target_file)
        if actually_md5 == md5:
            print("The file {file} is exists,do not to need to "
                  "download").format(file=target_file)
            return
        else:
            print("The md5 of the  file {file} is {ac_md5}, but the md5 "
                  "in the nexus is {expect_md5}, delete the old file")\
                .format(file=target_file, ac_md5=actually_md5, expect_md5=md5)
            os.remove(target_file)
    if os.path.exists(path):
        os.mkdir(path)
    rep = requests.get(download_url, stream=True)
    with open(target_file, 'wb') as f:
        for data in rep.iter_content(chunk_size=512):
            if data:
                f.write(data)


def run():
    assets = grab_components()
    pool = Pool(size=5)
    for asset in assets:
        pool.add(download, asset["download_url"], asset["path"], asset["md5"])
    pool.join()
