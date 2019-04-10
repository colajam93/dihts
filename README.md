# DEPRECATED

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

This repository is no longer maintained because I do not use the iTunes to manage music library.

# Do I have this song?

Simple iTunes library search tool using Django.
Build database from `iTunes Music Library.xml` and search songs or albums from DB.

## Install

- Install dependencies

```
# pacman -S --needed python python-pip python-virtualenv bower git
```

- Prepare files

```
$ git clone https://github.com/colajam93/dihts
$ cd dihts
$ virtualenv env
$ source env/bin/activate
$ ./install_dependencies.sh
$ ./manage.py migrate
$ ./manage.py collectstatic --no-input
```

- Initialize database

```
$ ./manage.py songupdate --init '/path/to/itunes music library.xml'
```

- Run server

Run development server or deploy to WSGI environment.

```
$ uwsgi --ini /home/user/dihts/dihts.ini
```

## Add song

```
$ ./manage.py songupdate '/path/to/itunes music library.xml'
```

This command will skip songs which have already existed.
To update or delete songs, you have to construct database from scratch (use `--init` option).

## License

MIT
