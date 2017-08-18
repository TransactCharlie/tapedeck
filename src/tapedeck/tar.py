import tarfile
from io import BytesIO


TAR_COMPRESSIONS = {"gzip": "w|gz", "bzip2": "w|bz2", "lzma": "w|xz"}


def inject_data_as_file(tar, filename, data):
    """
    stores <data> into tar with a filename of filename
    :param tar: an !open! tarfile object
    :param filename: the filename we write to tar
    :param data: data to be crammed in
    :return: tar (for possible fluid chaining)
    """
    file_info = tarfile.TarInfo(filename)
    file_info.size = len(data)
    tar.addfile(file_info, BytesIO(data.encode()))


def write_tar(data, stream, compression="gzip"):
    """
    Writes a tarfile to a stream
    :param data: dataset to write (a sequence of 2 tuples (name, data))
    :param stream: stream to write tar to
    :param compression: Use Gzip compression or not
    :return: none
    """
    mode = TAR_COMPRESSIONS.get(compression, "w|")
    with tarfile.open(fileobj=stream, mode=mode) as tf:
        for d in data:
            inject_data_as_file(tf, d[0], d[1])
        tf.close()
