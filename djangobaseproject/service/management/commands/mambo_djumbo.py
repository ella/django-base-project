from django.core.management.base import BaseCommand, CommandError
from django.core.management.base import NoArgsCommand

from optparse import make_option


class Command(NoArgsCommand):
    help = 'djangobaseproject initial command'
    option_list = NoArgsCommand.option_list + (
        make_option('--noinput', action='store_false', dest='interactive', default=True,
            help='Tells Django to NOT prompt the user for input of any kind.'),
    )

    def handle(self, *args, **options):
        from django.core.management import call_command
        from django.conf import settings

        nofetch = options.get('nofetch')
        interactive = options.get('interactive')

        if interactive:
            confirm = raw_input('\n'.join((
                'You have requested a database reset.',
                'This will IRREVERSIBLY DESTROY',
                'ALL data in the database "%s".' % settings.DATABASE_NAME,
                'Are you sure you want to do this?',
                '',
                "Type 'yes' to continue, or 'no' to cancel: ")))
        else:
            confirm = 'yes'

        if confirm != 'yes':
            print "Reset cancelled."
            return

        print 'reseting db'
        call_command('reset_db', verbosity=False)

        print 'syncing db'
        call_command('syncdb', verbosity=False)

        print 'loading fixtures'
        call_command('loaddata', 'user_admin', verbosity=False)


