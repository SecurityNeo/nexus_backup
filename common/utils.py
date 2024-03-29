import os
import hashlib


def md5sum(file_name):
    def read_chunks(fh):
        fh.seek(0)
        chunk = fh.read(8096)
        while chunk:
            yield chunk
            chunk = fh.read(8096)
        else:
            fh.seek(0)
    m = hashlib.md5()
    if isinstance(file_name, basestring) and os.path.exists(file_name):
        with open(file_name, "rb") as fh:
            for chunk in read_chunks(fh):
                m.update(chunk)
    elif file_name.__class__.__name__ in ["StringIO", "StringO"] or isinstance(file_name, file):
        for chunk in read_chunks(file_name):
            m.update(chunk)
    else:
        return ""
    return m.hexdigest()
