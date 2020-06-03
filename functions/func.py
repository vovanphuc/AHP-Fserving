import pandas as pd
import numpy as np


def preprocessing(data, price_from,price_to, area_from, area_to, provinceName=None, districtName = None ):
    # loc

    data = data.loc[:, ['index','bedRoom', 'fPrice', 'tPriceM2', 'fArea', 'provinceName','districtName', 'khoang_cach', 'range_tt', 'range_school']]
    data = data.where((data['fPrice'] > price_from) & (data['fPrice'] < price_to) &
                      (data['fArea'] < area_to) & (data['fArea'] > area_from) &
                      (data['tPriceM2'] > 20))
    if (districtName != None):
        data = data.where(data['districtName'] == districtName)
    data = data.dropna()
    data['tPrice_BedRoom'] = data['fPrice'] / data['bedRoom']
    data = data.reset_index()
    #
    data = data.loc[:, ['index', 'tPriceM2', 'tPrice_BedRoom', 'khoang_cach', 'range_school', 'range_tt']]
    #
    return data
def score(data):
    mean_tPriceM2 = np.round(data['tPriceM2'].mean())
    mean_tPrice_BedRoom = np.round(data['tPrice_BedRoom'].mean())
    mean_range_school = np.round(data['range_school'].mean())
    mean_range_tt = np.round(data['range_tt'].mean())
    mean_khoang_cach = np.round(data['khoang_cach'].mean())

    max_tPriceM2 = np.round(data['tPriceM2'].max())
    max_tPrice_BedRoom = np.round(data['tPrice_BedRoom'].max())
    max_range_school = np.round(data['range_school'].max())
    max_range_tt = np.round(data['range_tt'].max())
    max_khoang_cach = np.round(data['khoang_cach'].max())

    min_tPriceM2 = np.round(data['tPriceM2'].min())
    min_tPrice_BedRoom = np.round(data['tPrice_BedRoom'].min())
    min_range_school = np.round(data['range_school'].min())
    min_range_tt = np.round(data['range_tt'].min())
    min_khoang_cach = np.round(data['khoang_cach'].min())

    def tbc(x,y):
        return (x+y)/2
    ref = {'1': [ max_tPriceM2, max_tPrice_BedRoom, max_khoang_cach, max_range_school, max_range_tt],
       '2': [tbc(tbc(max_tPriceM2,mean_tPriceM2 ), max_tPriceM2), tbc(tbc(max_tPrice_BedRoom,mean_tPrice_BedRoom ), max_tPrice_BedRoom),
             tbc(tbc(max_khoang_cach,mean_khoang_cach ), max_khoang_cach), tbc(tbc(max_range_school,mean_range_school ), max_range_school),
             tbc(tbc(max_range_tt,mean_range_tt ), max_range_tt)],
       '3' : [ tbc(max_tPriceM2,mean_tPriceM2 ), tbc(max_tPrice_BedRoom,mean_tPrice_BedRoom ),
               tbc(max_khoang_cach,mean_khoang_cach ), tbc(max_range_school,mean_range_school ), tbc(max_range_tt,mean_range_tt )],
      '4': [tbc(tbc(max_tPriceM2,mean_tPriceM2 ), mean_tPriceM2), tbc(tbc(max_tPrice_BedRoom,mean_tPrice_BedRoom ), mean_tPrice_BedRoom),
            tbc(tbc(max_khoang_cach,mean_khoang_cach ), mean_khoang_cach), tbc(tbc(max_range_school,mean_range_school ), mean_range_school),
            tbc(tbc(max_range_tt,mean_range_tt ), mean_range_tt)],
       '5': [mean_tPriceM2, mean_tPrice_BedRoom, mean_khoang_cach, mean_range_school, mean_range_tt],
       '6' : [ tbc(tbc(min_tPriceM2,mean_tPriceM2 ), mean_tPriceM2), tbc(tbc(min_tPrice_BedRoom,mean_tPrice_BedRoom ), mean_tPrice_BedRoom),
               tbc(tbc(min_khoang_cach,mean_khoang_cach ), mean_khoang_cach), tbc(tbc(min_range_school,mean_range_school ), mean_range_school),
               tbc(tbc(min_range_tt,mean_range_tt ), mean_range_tt)],
      '7': [tbc(min_tPriceM2, mean_tPriceM2), tbc(min_tPrice_BedRoom, mean_tPrice_BedRoom), tbc(min_khoang_cach,mean_khoang_cach ),
            tbc(min_range_school, mean_range_school), tbc(min_range_tt,mean_range_tt )],
       '8': [tbc(tbc(min_tPriceM2,mean_tPriceM2 ), min_tPriceM2), tbc(tbc(min_tPrice_BedRoom,mean_tPrice_BedRoom ), min_tPrice_BedRoom),
             tbc(tbc(min_khoang_cach,mean_khoang_cach ), min_khoang_cach), tbc(tbc(min_range_school,mean_range_school ), min_range_school),
             tbc(tbc(min_range_tt,mean_range_tt ), min_range_tt)],
       '9' : [ min_tPriceM2, min_tPrice_BedRoom, min_khoang_cach, min_range_school, min_range_tt]}
    ref = pd.DataFrame(data=ref, index = ['tPriceM2', 'tPrice_BedRoom', 'khoang_cach', 'range_school', 'range_tt'])
    def thamchieu(x, l ):
        for i in range(0,9):
            if x >= l[i] :
                return int(i+1)
    h,w = data.shape
    data2 = data.copy()
    for i in range(0, h):
        for j in ['tPriceM2','tPrice_BedRoom','khoang_cach', 'range_school', 'range_tt']:
            data2.loc[i,j] = thamchieu(data.loc[i,j], ref.loc[j])
    return data2
def AHP(weight_vector_col1):
    matrix = np.eye(len(weight_vector_col1))
    matrix[0] = weight_vector_col1
    for i in range(0, matrix.shape[1]):
        for j in range(i+1, matrix.shape[0]):
            matrix[j, i] = 1/matrix[i, j]
        for j in range(i + 2, matrix.shape[0]):
            matrix[i + 1, j] = matrix[i + 1,0]*matrix[0,j]
    A = matrix.copy()
    num_rows, num_cols = A.shape
    sum_col = A.sum(axis=0)
    B = np.zeros(shape=(num_rows, num_cols))
    for row in range(0, num_rows):
        for col in range(0, num_cols):
            B[row][col] = A[row][col] / sum_col[col]
    sum_row = B.sum(axis=1)
    sum_all_row = sum_row.sum(axis=0)
    W = np.zeros(num_rows)
    for row in range(0, num_rows):
        W[row] = sum_row[row] / sum_all_row
    return W
def Rank(data, weight_vector):
    data['Diem_tong'] = weight_vector[0]*data.iloc[:,1] + \
                        weight_vector[1]*data.iloc[:,2] + \
                        weight_vector[2]*data.iloc[:,3] + \
                        weight_vector[3]*data.iloc[:,4] + \
                        weight_vector[4]*data.iloc[:,5]
    data =data.sort_values(by=['Diem_tong'], ascending=False)
    return data[:10]


def main(data, price_from, price_to, area_from, area_to, provinceName, districtName, weight_vector_col1):
    data1 = preprocessing(data, price_from, price_to, area_from, area_to, provinceName, districtName)
    data2 = score(data1)
    weight_vector = AHP(weight_vector_col1)

    return Rank(data2, weight_vector)['index'].values
