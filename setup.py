import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
import sys

setup(
    name = "django-followit",
    version = '0.0.4',
    description = 'A Django application that allows users to follow django model objects',
    packages = find_packages(),
    author = 'Evgeny.Fadeev',
    author_email = 'evgeny.fadeev@gmail.com',
    license = 'BSD License',
    keywords = 'follow, database, django',
    url = 'https://github.com/ASKBOT/django-followit',
    include_package_data = True,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: JavaScript',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    long_description = """The ``followit`` django app allows to easily set up a
capability for the site users to follow various things on the site,
represented by django model objects.

Setup
========

To the INSTALLED_APPS in your ``settings.py`` add entry ``'followit'``.
Then, in your apps' ``models.py``, probably at the end of the file, add::
    import followit
    followit.register(Thing)

Once that is done, in your shell run::
    python manage.py syncdb

Not it will be possible for the user to follow instances of ``SomeModel``.

If you decide to allow following another model, just add another
``followit.register(...)`` statement to the ``models.py`` and re-run the ``syncdb``.

Usage
============

Examples below show how to use ``followit`` (assuming that model ``Thing``
is registered with ``followit`` in your ``models.py``::
    bob.follow_thing(x)
    bob.unfollow_thing(x)
    things = bob.get_followed_things()
    x_followers = x.get_followers()

Note that ``followit`` does not yet provide view functions of url routing
relevant to following or unfollowing items, nor template tags.
"""
)
