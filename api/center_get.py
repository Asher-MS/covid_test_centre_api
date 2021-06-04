from .models import Center
import csv  
import os


def get():
    with open(os.getcwd()+'\\api\CovidLabs.csv','r') as file:
        reader=csv.reader(file)
        # print(reader)
        reader=list(reader)
        for i in range(1,len(reader)):
            ide=reader[i][0]
            
            name=reader[i][1]
            address=reader[i][2]
            district=reader[i][3]
            test_type=reader[i][4]
            lab_type=reader[i][6]
            # print(reader[7])
            latitude=float(reader[i][7])
            
            longitude=float(reader[i][8])
            temp=Centre(ide=ide,name=name,address=address,district=district,test_type=test_type,lab_type=lab_type,latitude=latitude,longitude=longitude)
            temp.save()

