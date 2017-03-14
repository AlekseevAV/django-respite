from setuptools import setup

exec(compile(open('respite/version.py', "rb").read(), 'respite/version.py', 'exec'))

setup(
    name = 'django-respite',
    version = __version__,
    description = "Respite conforms Django to Representational State Transfer (REST)",
    long_description = open('README.rst').read(),
    author = "Johannes Gorset",
    author_email = "jgorset@gmail.com",
    url = "http://github.com/jgorset/django-respite",
    packages = ['respite', 'respite.lib', 'respite.serializers', 'respite.urls', 'respite.views', 'respite.utils']
)
