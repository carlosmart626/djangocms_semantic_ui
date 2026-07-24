#!/usr/bin/env python
"""Entry point: `python -m tests.runtests <manage.py command> [args...]`."""
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from django.core.management import execute_from_command_line

    argv = sys.argv[:1] + (sys.argv[1:] or ["test", "tests"])
    execute_from_command_line(argv)


if __name__ == "__main__":
    main()
