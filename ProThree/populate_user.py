import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProThree.settings')

import django
django.setup()

from AppThree.models import VisitorList
from faker import Faker

fakegen = Faker()
def populate(N=5):
    for entry in range(N):
        # fake_name = fakegen.name().split()
        # fake_first_name = fake_name[0]
        # fake_last_name = fake_name[1]
        ff_name = fakegen.first_name()
        fl_name = fakegen.last_name()
        f_email = fakegen.email()

        visitors = VisitorList.objects.get_or_create(first_name=ff_name,
                                            last_name=fl_name,
                                            email=f_email)[0]
        visitors.save()

if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Populating complete!")
