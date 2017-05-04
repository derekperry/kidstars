from distutils.core import setup

setup(
    name='kidstars',
    version='',
    packages=['env.lib.python3.6.distutils', 'env.lib.python3.6.encodings', 'env.lib.python3.6.importlib',
              'env.lib.python3.6.collections', 'env.lib.python3.6.site-packages.pip',
              'env.lib.python3.6.site-packages.pip.req', 'env.lib.python3.6.site-packages.pip.vcs',
              'env.lib.python3.6.site-packages.pip.utils', 'env.lib.python3.6.site-packages.pip.compat',
              'env.lib.python3.6.site-packages.pip.models', 'env.lib.python3.6.site-packages.pip._vendor',
              'env.lib.python3.6.site-packages.pip._vendor.distlib',
              'env.lib.python3.6.site-packages.pip._vendor.distlib._backport',
              'env.lib.python3.6.site-packages.pip._vendor.colorama',
              'env.lib.python3.6.site-packages.pip._vendor.html5lib',
              'env.lib.python3.6.site-packages.pip._vendor.html5lib._trie',
              'env.lib.python3.6.site-packages.pip._vendor.html5lib.filters',
              'env.lib.python3.6.site-packages.pip._vendor.html5lib.treewalkers',
              'env.lib.python3.6.site-packages.pip._vendor.html5lib.treeadapters',
              'env.lib.python3.6.site-packages.pip._vendor.html5lib.treebuilders',
              'env.lib.python3.6.site-packages.pip._vendor.lockfile',
              'env.lib.python3.6.site-packages.pip._vendor.progress',
              'env.lib.python3.6.site-packages.pip._vendor.requests',
              'env.lib.python3.6.site-packages.pip._vendor.requests.packages',
              'env.lib.python3.6.site-packages.pip._vendor.requests.packages.chardet',
              'env.lib.python3.6.site-packages.pip._vendor.requests.packages.urllib3',
              'env.lib.python3.6.site-packages.pip._vendor.requests.packages.urllib3.util',
              'env.lib.python3.6.site-packages.pip._vendor.requests.packages.urllib3.contrib',
              'env.lib.python3.6.site-packages.pip._vendor.requests.packages.urllib3.packages',
              'env.lib.python3.6.site-packages.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
              'env.lib.python3.6.site-packages.pip._vendor.packaging',
              'env.lib.python3.6.site-packages.pip._vendor.cachecontrol',
              'env.lib.python3.6.site-packages.pip._vendor.cachecontrol.caches',
              'env.lib.python3.6.site-packages.pip._vendor.webencodings',
              'env.lib.python3.6.site-packages.pip._vendor.pkg_resources',
              'env.lib.python3.6.site-packages.pip.commands', 'env.lib.python3.6.site-packages.pip.operations',
              'env.lib.python3.6.site-packages.cffi', 'env.lib.python3.6.site-packages.mako',
              'env.lib.python3.6.site-packages.mako.ext', 'env.lib.python3.6.site-packages.click',
              'env.lib.python3.6.site-packages.flask', 'env.lib.python3.6.site-packages.flask.ext',
              'env.lib.python3.6.site-packages.tests', 'env.lib.python3.6.site-packages.wheel',
              'env.lib.python3.6.site-packages.wheel.test',
              'env.lib.python3.6.site-packages.wheel.test.simple.dist.simpledist',
              'env.lib.python3.6.site-packages.wheel.test.complex-dist.complexdist',
              'env.lib.python3.6.site-packages.wheel.tool', 'env.lib.python3.6.site-packages.wheel.signatures',
              'env.lib.python3.6.site-packages.bcrypt', 'env.lib.python3.6.site-packages.jinja2',
              'env.lib.python3.6.site-packages.oauth2', 'env.lib.python3.6.site-packages.oauth2.clients',
              'env.lib.python3.6.site-packages.alembic', 'env.lib.python3.6.site-packages.alembic.ddl',
              'env.lib.python3.6.site-packages.alembic.util', 'env.lib.python3.6.site-packages.alembic.script',
              'env.lib.python3.6.site-packages.alembic.runtime', 'env.lib.python3.6.site-packages.alembic.testing',
              'env.lib.python3.6.site-packages.alembic.testing.plugin',
              'env.lib.python3.6.site-packages.alembic.operations',
              'env.lib.python3.6.site-packages.alembic.autogenerate', 'env.lib.python3.6.site-packages.blinker',
              'env.lib.python3.6.site-packages.passlib', 'env.lib.python3.6.site-packages.passlib.ext',
              'env.lib.python3.6.site-packages.passlib.ext.django', 'env.lib.python3.6.site-packages.passlib.tests',
              'env.lib.python3.6.site-packages.passlib.utils', 'env.lib.python3.6.site-packages.passlib.utils.compat',
              'env.lib.python3.6.site-packages.passlib.crypto', 'env.lib.python3.6.site-packages.passlib.crypto.scrypt',
              'env.lib.python3.6.site-packages.passlib.crypto._blowfish',
              'env.lib.python3.6.site-packages.passlib.handlers', 'env.lib.python3.6.site-packages.wtforms',
              'env.lib.python3.6.site-packages.wtforms.ext', 'env.lib.python3.6.site-packages.wtforms.ext.csrf',
              'env.lib.python3.6.site-packages.wtforms.ext.i18n', 'env.lib.python3.6.site-packages.wtforms.ext.django',
              'env.lib.python3.6.site-packages.wtforms.ext.django.templatetags',
              'env.lib.python3.6.site-packages.wtforms.ext.dateutil',
              'env.lib.python3.6.site-packages.wtforms.ext.appengine',
              'env.lib.python3.6.site-packages.wtforms.ext.sqlalchemy', 'env.lib.python3.6.site-packages.wtforms.csrf',
              'env.lib.python3.6.site-packages.wtforms.fields', 'env.lib.python3.6.site-packages.wtforms.widgets',
              'env.lib.python3.6.site-packages.facebook', 'env.lib.python3.6.site-packages.httplib2',
              'env.lib.python3.6.site-packages.oauthlib', 'env.lib.python3.6.site-packages.oauthlib.oauth1',
              'env.lib.python3.6.site-packages.oauthlib.oauth1.rfc5849',
              'env.lib.python3.6.site-packages.oauthlib.oauth1.rfc5849.endpoints',
              'env.lib.python3.6.site-packages.oauthlib.oauth2',
              'env.lib.python3.6.site-packages.oauthlib.oauth2.rfc6749',
              'env.lib.python3.6.site-packages.oauthlib.oauth2.rfc6749.clients',
              'env.lib.python3.6.site-packages.oauthlib.oauth2.rfc6749.endpoints',
              'env.lib.python3.6.site-packages.oauthlib.oauth2.rfc6749.grant_types',
              'env.lib.python3.6.site-packages.requests', 'env.lib.python3.6.site-packages.requests.packages',
              'env.lib.python3.6.site-packages.requests.packages.idna',
              'env.lib.python3.6.site-packages.requests.packages.chardet',
              'env.lib.python3.6.site-packages.requests.packages.urllib3',
              'env.lib.python3.6.site-packages.requests.packages.urllib3.util',
              'env.lib.python3.6.site-packages.requests.packages.urllib3.contrib',
              'env.lib.python3.6.site-packages.requests.packages.urllib3.packages',
              'env.lib.python3.6.site-packages.requests.packages.urllib3.packages.backports',
              'env.lib.python3.6.site-packages.requests.packages.urllib3.packages.ssl_match_hostname',
              'env.lib.python3.6.site-packages.werkzeug', 'env.lib.python3.6.site-packages.werkzeug.debug',
              'env.lib.python3.6.site-packages.werkzeug.contrib', 'env.lib.python3.6.site-packages.flask_wtf',
              'env.lib.python3.6.site-packages.flask_wtf.recaptcha', 'env.lib.python3.6.site-packages.packaging',
              'env.lib.python3.6.site-packages.pycparser', 'env.lib.python3.6.site-packages.pycparser.ply',
              'env.lib.python3.6.site-packages.markupsafe', 'env.lib.python3.6.site-packages.setuptools',
              'env.lib.python3.6.site-packages.setuptools.command', 'env.lib.python3.6.site-packages.sqlalchemy',
              'env.lib.python3.6.site-packages.sqlalchemy.ext',
              'env.lib.python3.6.site-packages.sqlalchemy.ext.declarative',
              'env.lib.python3.6.site-packages.sqlalchemy.orm', 'env.lib.python3.6.site-packages.sqlalchemy.sql',
              'env.lib.python3.6.site-packages.sqlalchemy.util', 'env.lib.python3.6.site-packages.sqlalchemy.event',
              'env.lib.python3.6.site-packages.sqlalchemy.engine', 'env.lib.python3.6.site-packages.sqlalchemy.testing',
              'env.lib.python3.6.site-packages.sqlalchemy.testing.suite',
              'env.lib.python3.6.site-packages.sqlalchemy.testing.plugin',
              'env.lib.python3.6.site-packages.sqlalchemy.dialects',
              'env.lib.python3.6.site-packages.sqlalchemy.dialects.mssql',
              'env.lib.python3.6.site-packages.sqlalchemy.dialects.mysql',
              'env.lib.python3.6.site-packages.sqlalchemy.dialects.oracle',
              'env.lib.python3.6.site-packages.sqlalchemy.dialects.sqlite',
              'env.lib.python3.6.site-packages.sqlalchemy.dialects.sybase',
              'env.lib.python3.6.site-packages.sqlalchemy.dialects.firebird',
              'env.lib.python3.6.site-packages.sqlalchemy.dialects.postgresql',
              'env.lib.python3.6.site-packages.sqlalchemy.databases',
              'env.lib.python3.6.site-packages.sqlalchemy.connectors', 'env.lib.python3.6.site-packages.flask_script',
              'env.lib.python3.6.site-packages.flask_social', 'env.lib.python3.6.site-packages.flask_social.providers',
              'env.lib.python3.6.site-packages.flask_migrate', 'env.lib.python3.6.site-packages.pkg_resources',
              'env.lib.python3.6.site-packages.pkg_resources.extern',
              'env.lib.python3.6.site-packages.pkg_resources._vendor',
              'env.lib.python3.6.site-packages.pkg_resources._vendor.packaging',
              'env.lib.python3.6.site-packages.flask_oauthlib',
              'env.lib.python3.6.site-packages.flask_oauthlib.contrib',
              'env.lib.python3.6.site-packages.flask_oauthlib.provider',
              'env.lib.python3.6.site-packages.flask_security', 'env.lib.python3.6.site-packages.flask_sqlalchemy',
              'kidstars'],
    url='',
    license='',
    author='derek.perry',
    author_email='',
    description=''
)
