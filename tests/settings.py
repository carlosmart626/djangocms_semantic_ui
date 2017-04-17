#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    sites = models.ManyToManyField('sites.Site')

    def get_sites(self):
        return self.sites


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
}


def run():
    from djangocms_helper import runner
    runner.cms('djangocms_semantic_ui')


if __name__ == '__main__':
    run()
