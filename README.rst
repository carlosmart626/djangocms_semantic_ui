=====================
DjangoCMS Semantic UI
=====================

.. image:: https://badge.fury.io/py/djangocms-semantic-ui.svg
    :target: https://badge.fury.io/py/djangocms-semantic-ui

.. image:: https://github.com/CarlosMart626/djangocms_semantic_ui/actions/workflows/test.yml/badge.svg
    :target: https://github.com/CarlosMart626/djangocms_semantic_ui/actions/workflows/test.yml

Semantic UI reusable components for DjangoCMS.

Requires Python 3.10+, Django 5.2 and django-cms 5.1.

Available Components
====================

- Container
- Grid
- Column
- Segments
- Group Segments
- Dividers
- Tabs

Usage
=====

Install using ``pip install djangocms-semantic-ui`` and add it to the installed apps of your
django CMS project.

.. note::

    django-cms 5.1 imports the ``packaging`` library at runtime without declaring it as a
    dependency of its own, so this package declares ``packaging`` explicitly and pip will
    pull it in for you.

Settings
========

.. code:: python

    INSTALLED_APPS = (
        # ...
        'djangocms_semantic_ui',
    )
