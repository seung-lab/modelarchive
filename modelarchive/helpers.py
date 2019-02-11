import shutil
from pathlib import Path


def cp(src, dst):
    """
    A wrapper for the shutil copy function, but that accepts path objects.
    The shutil library will be updated to accept them directly in a later
    version of python, and so this will no longer be needed, but for now,
    this seemed cleaner than having explicit conversions everywere.
    """
    if isinstance(src, Path):
        src = str(src)
    if isinstance(dst, Path):
        dst = str(dst)
    shutil.copy(src, dst)


class dotdict(dict):
    """Allow accessing dict elements with dot notation"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.items():
            if isinstance(v, dict):
                self[k] = dotdict(v)
