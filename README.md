cbr2cbz
=======

CBR to CBZ conversion tool for GNU/Linux


Requirements
------------

* A GNU/Linux distro (sorry, no Windows support)
* The non-free package ``unrar-nonfree`` (check [unrar-nonfree](https://packages.debian.org/source/sid/unrar-nonfree/ "Debian non-free"))
* The free package ``zip``. Install it with ``sudo apt-get install zip``.
* Python (checked with Python 2.7 and Python 3.3)

Usage
-----

To convert a single CBR file use this:

``./cbr2cbz.py <cbr_filename>``

To convert an entire directory with CBR files in it use:

``cbrfolder2cbz.py <directory>``

The script will put CBZ files in the same directory. In case you need to rename many files check [pyrenamer] (https://packages.debian.org/wheezy/pyrenamer)

Introduction
-------------
CBR files use RAR format, a non-free format. If you use a GPL comics reader in your tablet it's likely it will have problems when reading CBR files. Convert them to CBZ with this script.
