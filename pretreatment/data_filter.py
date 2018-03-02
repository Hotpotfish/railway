import os
import text_ddb_reader
import text_tax_reader
import tax_data
import ddb_data
import need_data

import datetime



class filter(object):
    
    temp_1_path = None
    
    temp_2_path = None

    def __init__(self, temp_1_path, temp_2_path):
        
        self.temp_1_path = temp_1_path
        
        self.temp_2_path = temp_2_path
        
    def scan_and_write(self):
        
        temp_names = os.listdir(self.temp_1_path)
        
        count = len(temp_names) / 3
        
        for i in range(0, count):
            
            tn = temp_names[i * 3][0:9]
            '''
            if tn == "hxd21281b":
                
                print "!"
            '''
            ddbs = text_ddb_reader.reader(self.temp_1_path + tn + "_ddb.csv").read()
            
            taxs = text_tax_reader.reader(self.temp_1_path + tn + "_tax.csv").read()
            
            #(ddbs,taxs) = self.update_two_Arr(ddbs,taxs)
            
            #needs = self.combination(ddbs, taxs)
            
            T = self.combination_1(ddbs,taxs)
            
            needs = self.get_needs(T)
            
            
            self.write(tn,needs)
            
     
    def  combination_1(self, ddbs, taxs):  
        
        T = []
        
        i = j = 0
        
        dc = len(ddbs)
        
        tc = len(taxs)
        
        while True:
            
            
            
            
            
            
            ddb1 = ddbs[i]
            
            tax1 = taxs[j]
            
            
            str1 = ddb1.tRunTime.split()
        
            Date1 = str1[0].split('-')
            
            Y1 = int(Date1[0])
            
            MO1 = int(Date1[1])
            
            D1 = int(Date1[2])
            
            T1 = str1[1].split(':')
            
            H1 = int(T1[0])
            
            M1 = int(T1[1])
            
            S1 = int(T1[2])
            
            d1 = datetime.datetime(Y1, MO1, D1, H1, M1 ,S1)
            
            str2 = tax1.tRunTime.split()
            
            Date2 = str2[0].split('-')
            
            Y2 = int(Date2[0])
            
            MO2 = int(Date2[1])
            
            D2 = int(Date2[2])
            
            T2 = str2[1].split(':')
            
            H2 = int(T2[0])
            
            M2 = int(T2[1])
            
            S2 = int(T2[2])
            
            d2 = datetime.datetime(Y2, MO2, D2, H2, M2 ,S2)
            
            re = int((d1 - d2).total_seconds())
            
            if re <= 0:
                
                T.append(ddb1)
                
                i = i + 1
                
            else :
                
                T.append(tax1)
                
                j = j + 1
                
                
            if (i == dc) or (j == tc):
                
                return T
            
    def get_needs(self, T):
        
        needs = []
        
        count = len(T)
        
        ex_ddb = ddb_data.ddb()
        
        ex_tax = tax_data.tax()
        
        '''
        for i in range(0, count):
            
            if i != 0 and type (T[i]) == type(ex_tax) :
                
                if type (T[i - 1]) == type(ex_ddb):       
                    
                    ddb1 = T[i - 1]
            
                    tax1 = T[i]
                    
                    k = -1
                    
                    k = self.f1(ddb1, tax1)
                    
                    if k == 0:
                        
                        
                        temp_need = need_data.need()
                    
                        temp_need.tRunTime = tax1.tRunTime
                        
                        print   temp_need.tRunTime
        
                        temp_need.nRunSpeed = tax1.nRunSpeed
                        
                        temp_need.nRunStone = tax1.nRunStone
                        
                        temp_need.sTrainNo = tax1.sTrainNo
                        
                        temp_need.sCarNo = tax1.sCarNo
                        
                        temp_need.nErr = tax1.nErr
                        
                        temp_need.nSiteNo = tax1.nSiteNo
                        
                        temp_need.nDriverNo = tax1.nDriverNo 
                        
                        temp_need.nDriverNo2 = tax1.nDriverNo2
                        
                        temp_need.nJiaoLuHao = tax1.nJiaoLuHao
                        
                        temp_need.nWeight = tax1.nWeight
                        
                        temp_need.nLength = tax1.nLength
                        
                        temp_need.nCarCount = tax1.nCarCount
                        
                        temp_need.nZyPower = ddb1.nZyPower
                        
                        temp_need.nFyPower = ddb1.nFyPower
                        
                        needs.append(temp_need)
                        
                        print "count = " + str(len(needs))
                        '''
        for i in range(0, count):
            
            if i != 0 and type (T[i]) == type(ex_ddb) :
                
                if type (T[i - 1]) == type(ex_tax):       
                    
                    ddb1 = T[i]
            
                    tax1 = T[i - 1]
                    
                    k = -1
                    
                    k = self.f1(ddb1, tax1)
                    
                    if k == 0:
                        
                        
                        temp_need = need_data.need()
                    
                        temp_need.tRunTime = ddb1.tRunTime
                        
                        print   temp_need.tRunTime
        
                        temp_need.nRunSpeed = tax1.nRunSpeed
                        
                        temp_need.nRunStone = tax1.nRunStone
                        
                        temp_need.sTrainNo = tax1.sTrainNo
                        
                        temp_need.sCarNo = tax1.sCarNo
                        
                        temp_need.nErr = tax1.nErr
                        
                        temp_need.nSiteNo = tax1.nSiteNo
                        
                        temp_need.nDriverNo = tax1.nDriverNo 
                        
                        temp_need.nDriverNo2 = tax1.nDriverNo2
                        
                        temp_need.nJiaoLuHao = tax1.nJiaoLuHao
                        
                        temp_need.nWeight = tax1.nWeight
                        
                        temp_need.nLength = tax1.nLength
                        
                        temp_need.nCarCount = tax1.nCarCount
                        
                        temp_need.nZyPower = ddb1.nZyPower
                        
                        temp_need.nFyPower = ddb1.nFyPower
                        
                        needs.append(temp_need)
                        
                        print "count = " + str(len(needs))
                        
        return needs                
                    
                    
                    
                    
                
                
                
                
            
            
                   
    
    def update_two_Arr(self, ddbs, taxs):
        
        ddbs1 = []
        
        taxs1 = []
        
        temp_time = ""
         
        for i in range(0, len(ddbs)):
            
            standard_time = self.date_rounding(ddbs[i].tRunTime)
            
            if standard_time != temp_time:
                
                ddbs[i].tRunTime = standard_time
                
                temp_time = standard_time
                
                ddbs1.append(ddbs[i])
        
        temp_time = ""
        
                
        for i in range(0, len(taxs)):
            
            standard_time = self.date_rounding(taxs[i].tRunTime)
            
            if standard_time != temp_time:
                
                taxs[i].tRunTime = standard_time
                
                temp_time = standard_time
                
                taxs1.append(taxs[i])
        
        return ddbs1,taxs1    
        '''
        for i in range(0, len(ddbs)):
            
            standard_time = self.date_rounding(ddbs[i].tRunTime)
            
            if not d1[standard_time]:
                
                ddbs[i].tRunTime = standard_time
                
                d1[standard_time] = ddbs[i]
        
        for i in range(0, len(taxs)):
            
            standard_time = self.date_rounding(taxs[i].tRunTime)
            
            if not d2[standard_time]:
                
                taxs[i].tRunTime = standard_time
                
                d2[standard_time] = taxs[i]
            
              
        return d1,d2
          '''  
                
                
        
    def date_rounding(self, date):
        
        string = date.split()
        
        T = string[1].split(':')
        
        H = int(T[0])
        
        M = int(T[1])
        
        S = int(T[2])
        
        t = (H * 3600 + M * 60 + S) /8 * 8
        
        H = t /3600
        
        M = (t - H * 3600) / 60
        
        S = t - H * 3600 - M * 60
        
        new_date = string[0] + " " + str(H) + ":" + str(M) + ":" + str(S)
        
        return new_date
        
        
        
        
        
    
    def combination(self, ddbs, taxs):
        
        
        
        needs = []
        
        c1 = len(ddbs)
        
        c2 = len(taxs)
        
        mark = 0
        
        for i in range(0, c2):
            
            tempi = taxs[i]
         
            for j in range(mark, c1):
                
                print "i = " + str(i + 1)
                
                print "j = " + str(j + 1)
              
                if i + 1 == 11 :#and j == 2 :
                    
                    print "!"
                
                if j == (mark + 5000):
                    
                    break
                
                tempj = ddbs[j]
                 
                k = -1
                 
                k = self.f1(tempj, tempi)
                 
                if k == 0 :
                    
                    print "mark = " + str(mark)
                    
                    mark = j + 1
                    
                    temp_need = need_data.need()
                    
                    temp_need.tRunTime = tempi.tRunTime
                    
                    print   temp_need.tRunTime
    
                    temp_need.nRunSpeed = tempi.nRunSpeed
                    
                    temp_need.nRunStone = tempi.nRunStone
                    
                    temp_need.sTrainNo = tempi.sTrainNo
                    
                    temp_need.sCarNo = tempi.sCarNo
                    
                    temp_need.nErr = tempi.nErr
                    
                    temp_need.nSiteNo = tempi.nSiteNo
                    
                    temp_need.nDriverNo = tempi.nDriverNo 
                    
                    temp_need.nDriverNo2 = tempi.nDriverNo2
                    
                    temp_need.nJiaoLuHao = tempi.nJiaoLuHao
                    
                    temp_need.nWeight = tempi.nWeight
                    
                    temp_need.nLength = tempi.nLength
                    
                    temp_need.nCarCount = tempi.nCarCount
                    
                    temp_need.nZyPower = tempj.nZyPower
                    
                    temp_need.nFyPower = tempj.nFyPower
                    
                    needs.append(temp_need)
                    
                    print "count = " + str(len(needs))
                    
                    break
        
        return needs
        
     
    def f1(self, ddb1, tax1):
        
       
        
        str1 = ddb1.tRunTime.split()
        
        Date1 = str1[0].split('-')
        
        Y1 = int(Date1[0])
        
        MO1 = int(Date1[1])
        
        D1 = int(Date1[2])
        
        T1 = str1[1].split(':')
        
        H1 = int(T1[0])
        
        M1 = int(T1[1])
        
        S1 = int(T1[2])
        
        d1 = datetime.datetime(Y1, MO1, D1, H1, M1 ,S1)
        
        str2 = tax1.tRunTime.split()
        
        Date2 = str2[0].split('-')
        
        Y2 = int(Date2[0])
        
        MO2 = int(Date2[1])
        
        D2 = int(Date2[2])
        
        T2 = str2[1].split(':')
        
        H2 = int(T2[0])
        
        M2 = int(T2[1])
        
        S2 = int(T2[2])
        
        d2 = datetime.datetime(Y2, MO2, D2, H2, M2 ,S2)
        '''
        if  str1[0] != str2[0]:
            
            return -1
    
        re = (H2 - H1) * 3600 + (M2 - M1) * 60 + (S2 - S1)
        
        '''
        
        re = int((d1 - d2).total_seconds())
        
        if re <= 10 and re >= -10:
            
            return 0
        
        return -1
    
    def write(self, tn, needs):
        
        fw = open(self.temp_2_path + tn + ".csv","a+")
            
        for i in range(0, len(needs)):
            
            fw.write(needs[i].tRunTime + " " +
                     
                     needs[i].nRunSpeed + " " +
                     
                     needs[i].nRunStone + " " +
                     
                     needs[i].sTrainNo + " " +
                     
                     needs[i].sCarNo + " " +
                     
                     needs[i].nErr + " " +
                     
                     needs[i].nSiteNo + " " +
                     
                     needs[i].nDriverNo + " " +
                     
                     needs[i].nDriverNo2 + " " +
                     
                     needs[i].nJiaoLuHao + " " +
                     
                     needs[i].nWeight + " " +
                     
                     needs[i].nLength + " " +
                     
                     needs[i].nCarCount + " " +
                     
                     needs[i].nZyPower + " " +
                     
                     needs[i].nFyPower + " " +
                     
                     "\n"
                     )
        fw.close()
        
        
    
