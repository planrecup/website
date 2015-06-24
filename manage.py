# !python
# coding=UTF-8

if __name__ == "__main__":
    
    import os
    import sys
    
    sys.path.append(os.path.realpath(os.path.dirname(os.path.realpath(__file__)
                                                     )))
    
    path = os.path.dirname(os.path.realpath(__file__))
    os.environ.setdefault("DJANGO_ENV", 'dev')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "planrecup.settings")
    
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
