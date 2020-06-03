# -*- coding: utf-8 -*-

import datetime
import pandas as pd
from mongoengine import *

connect('bds', host='ec2-3-1-194-244.ap-southeast-1.compute.amazonaws.com', port=27017)


# connect('bds5')

class ItemObject(Document):
    meta = {'collection': 'item'}
    index = StringField(required=True, max_length=200)
    source = StringField(required=True, max_length=200)
    linkUrl = StringField(required=True, max_length=10000)

    title = StringField(required=True, max_length=10000)
    description = StringField(required=True, max_length=100000)
    address = StringField(required=True, max_length=10000)

    fPrice = FloatField(default=0)
    fArea = FloatField(default=0)

    isFrontispiece = BooleanField(default=False)
    isInAlley = BooleanField(default=False)
    streetName = StringField(default=None)
    widthLine = StringField(default='')
    addressContact = StringField(default='')
    direction = StringField(default='')
    imgs = StringField(default='')
    districtName = StringField(default='')
    provinceName = StringField(default='')
    area = StringField(default='')
    nameContact = StringField(default='')
    createDate = StringField(default='')
    lon = StringField(default='')
    product = StringField(default='')
    price = StringField(default='')
    roadCondition = StringField(default='')
    lat = StringField(default='')
    keyContent = StringField(default='')
    furniture = StringField(default='')
    bathRoom = StringField(default='')
    floor = StringField(default='')
    phonesContact = StringField(default='')
    bedRoom = StringField(default='')
    sUnit = StringField(default='')
    nPrice = StringField(default='')
    id_server = StringField(default='')
    tPrice = StringField(default='')
    year = StringField(default='')
    tPriceM2 = StringField(default='')
    month = StringField(default='')
    tUnitPrice = StringField(default='')
    week = StringField(default='')
    tArea = StringField(default='')
    createdAt = DateTimeField(default=datetime.datetime.utcnow)
    modifiedAt = DateTimeField(default=datetime.datetime.utcnow)
    status = StringField(max_length=200)
df = pd.DataFrame.from_records(
    ItemObject.objects.all().values_list('index', 'title', 'description',
                                         'address', 'fPrice', 'fArea', 'fArea', 'districtName',
                                         'provinceName', 'area', 'lon', 'lat', 'bedRoom', 'tPriceM2')
)
df = df.rename(columns={'0':'index', '1':'title','2': 'description',
                                         '3':'address', '4':'fPrice', '5':'fArea', '6':'fArea', '7':'districtName',
                                         '8':'provinceName', '9':'area', '10':'lon', '11':'lat', '12':'bedRoom', '13':'tPriceM2'})
#df = df.query("provinceName == 'Hồ Chí Minh'")
df.to_csv('data_hcm.csv', index = False)
print(df)
