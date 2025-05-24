import argparse
import sys

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from .. import models


def setup_models(dbsession):
    """
    Add initial model objects.
    """
    # Tambahkan data awal untuk Matakuliah
    matakuliah1 = models.Matakuliah(
        kode_mk='MK001',
        nama_mk='Pemrograman Web',
        sks=3,
        semester=5
    )
    matakuliah2 = models.Matakuliah(
        kode_mk='MK002',
        nama_mk='Struktur Data',
        sks=4,
        semester=3
    )
    matakuliah3 = models.Matakuliah(
        kode_mk='MK003',
        nama_mk='Basis Data',
        sks=3,
        semester=4
    )
    dbsession.add(matakuliah1)
    dbsession.add(matakuliah2)
    dbsession.add(matakuliah3)


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config_uri',
        help='Configuration file, e.g., development.ini',
    )
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env['request'].tm:
            dbsession = env['request'].dbsession
            setup_models(dbsession)
    except OperationalError:
        print('''
Pyramid is having a problem using your SQL database.

Your database should be up and running before you
initialize your project. Make sure your database server
is running and your connection string in development.ini
is correctly configured.
''')


if __name__ == '__main__':
    main()