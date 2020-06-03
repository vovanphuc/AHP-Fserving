import pandas as pd
import numpy as np
df = pd.read_csv('data_hcm.csv')
#df = df.rename(columns={'1': 'BB'})
#df = df.rename(columns={'0':'index', '1':'title','2': 'description',
#                                         '3':'address', '4':'fPrice', '5':'fArea', '6':'fArea', '7':'districtName',
#                                         '8':'provinceName', '9':'area', '10':'lon', '11':'lat', '12':'bedRoom', '13':'tPriceM2'})
#df = df.query("provinceName == 'Hồ Chí Minh'")
#df.to_csv('data_hcm.csv', index = False)
# df['khoang_cach'] = np.random.randint(1, 20, df.shape[0])
# # toa do cac khu vuc dc goi la trung tam
# X =[[10.990677, 106.520779],[10.826163, 106.794064],[10.544122, 106.820157],
#     [10.465807, 106.884015],[10.716931, 106.629006]]
# import math
# def rad(x):
#     return x * math.pi / 180
# def getDistance(lat1, lng1, lat2, lng2):
#     R = 6378137
#     dLat = rad(lat2 - lat1)
#     dLong = rad(lng2 - lng1)
#     a = math.sin(dLat/2)*math.sin(dLat/2) + math.cos(rad(lat1))*math.cos(rad(lat2))*math.sin(dLong/2)*math.sin(dLong/2)
#     c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
#     return R*c
# # for i in range (len(df)):
# #     kc = getDistance(X[0][0], X[0][1], df.iloc[i]['lat'], df.iloc[i]['lon'])
# #     for j in range(1,len(X)):
# #         if (kc > getDistance(X[j][0], X[j][1], df.iloc[i]['lat'], df.iloc[i]['lon'])):
# #             kc = getDistance(X[j][0], X[j][1], df.iloc[i]['lat'], df.iloc[i]['lon'])
# #     df.loc[i,'khoang_cach'] = kc
# Trung_tam = [10.771677, 106.696817]
# df['range_tt'] = np.random.randint(1, 20, df.shape[0])
# for i in range (len(df)):
#     df.loc[i,'range_tt'] = getDistance(Trung_tam[0], Trung_tam[1], df.iloc[i]['lat'], df.iloc[i]['lon'])
#df['range_school'] = np.random.randint(1, 20, df.shape[0])
#df.to_csv('data_hcm.csv', index = False)

print(df.query("index == 10")['title'])