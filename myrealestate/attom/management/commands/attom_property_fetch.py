from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from attom.models import *
from attom.utils import *


class Command(BaseCommand):
    help = 'This command once run helps populate property data from attom.'

    def add_arguments(self, parser):
        parser.add_argument('--zipcode', nargs='?', type=int, action='store')

    def handle(self, *args, **options):
        zipcode = options['zipcode']
        try:
            property_lst_res = attom_property_get(url=settings.PROPERTY_LIST_URL.format(zipcode))
            for property_json in property_lst_res:
                attom_id = property_json.get('identifier').get('attomId')
                detail_json = attom_property_get(url=settings.PROPERTY_DETAIL_URL.format(attom_id))[0]
                property = Property()
                for key in detail_json:
                    if key == 'identifier':
                        property.identifier = detail_json.get(key, None)
                    elif key == 'lot':
                        property.lot = detail_json.get(key, None)
                    elif key == 'area':
                        property.area = detail_json.get(key, None)
                    elif key == 'address':
                        property.address = detail_json.get(key, None)
                    elif key == 'location':
                        property.location = detail_json.get(key, None)
                    elif key == 'summary':
                        property.summary = detail_json.get(key, None)
                    elif key == 'utilities':
                        property.utilities = detail_json.get(key, None)
                    elif key == 'building':
                        property.building = detail_json.get(key, None)
                    elif key == 'vintage':
                        property.vintage = detail_json.get(key, None)
                property.save()
                print('We have saved a property with attom_id to be {}'.format(property.identifier['attomId']))
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
