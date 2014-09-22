from distutils.core import setup

setup(
    name='postgresqlbackup',
    url='https://github.com/Version2beta/postgresqlbackup',
    version='1.0.5',
    author='Rob Martin',
    author_email='rob@version2beta.com',
    description=('Back up all PostgreSQL databases to a local '
                 'directory plus rotating hourly and seven day on Amazon S3.'),
    packages=['postgresqlbackup'],
    install_requires=[],
    data_files=[('/etc/postgresql', ['backups.conf'])],
    entry_points={
        'console_scripts': [
            'postgresql_backup=postgresqlbackup.postgresqlbackup:main'
        ]
    }
)
