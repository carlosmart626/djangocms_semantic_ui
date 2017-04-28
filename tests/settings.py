#!/usr/bin/env python
# -*- coding: utf-8 -*-

HELPER_SETTINGS = {
    'INSTALLED_APPS': [],
    'ALLOWED_HOSTS': ['localhost'],
    'CMS_LANGUAGES': {
        1: [{
            'code': 'en',
            'name': 'English',
        }]
    },
    'LANGUAGE_CODE': 'en',
    'SECRET_KEY': 1,

    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'django_test.sqlite',
        }
    }
}


def run():
    from djangocms_helper import runner
    runner.cms('djangocms_semantic_ui')


if __name__ == '__main__':
    run()
