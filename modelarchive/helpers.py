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
