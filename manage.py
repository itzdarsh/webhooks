import datetime,requests,sys


Today = datetime.date.today().strftime('%d-%m-%Y')
dateList = [Today]
findFor = int(sys.argv[2])
for i in range(1,findFor):
    dateList.append((datetime.date.today() + datetime.timedelta(days=i)).strftime('%d-%m-%Y'))

pinCode = sys.argv[1]
print(pinCode)
for i in dateList:
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=" + str(pinCode) + "&date=" + str(i)
    res = requests.get(url).json()
    for i in range(0,len(res['sessions'])):
        if res['sessions'][i]['min_age_limit'] == 45:
            print(res['sessions'][i])

