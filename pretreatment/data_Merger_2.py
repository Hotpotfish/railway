import os
import need_data
import text_need_reader
import datetime

class Merger(object):
    
    
    temp_2_path = None
    
    output_path = None


    def __init__(self, temp_2_path, output_path):
        
        self.temp_2_path = temp_2_path
        
        self.output_path = output_path
        
    
        
    def Merge(self):
        
        temp_names = os.listdir(self.temp_2_path)
        
        count = len(temp_names) / 2
        
        for i in range(0, count):
            
            tn =  temp_names[i * 2][0 : 8]
            
            needs1 = text_need_reader.reader(self.temp_2_path + tn + "a.csv").read()
            
            needs2 = text_need_reader.reader(self.temp_2_path + tn + "b.csv").read()
            
            needs = self.combination(needs1, needs2)
            
            self.write(tn, needs)
            
            print "!"
     
    def write(self, tn, needs):
        
        fw = open(self.output_path + tn + ".csv","a+")
            
        for i in range(0, len(needs)):
            
            if needs[i].sTrainNo == "0" or needs[i].sCarNo == "0":
                
                continue
            
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
        
        
               
    def combination(self, needs1, needs2):
        
        c1 = len(needs1)
        
        c2 = len(needs2)
        
        i = j = 0
        
        needs = []
        
        while True:
            
            need1 = needs1[i]
            
            need2 = needs2[j]
            
            str1 = need1.tRunTime.split()
        
            Date1 = str1[0].split('-')
            
            Y1 = int(Date1[0])
            
            MO1 = int(Date1[1])
            
            D1 = int(Date1[2])
            
            T1 = str1[1].split(':')
            
            H1 = int(T1[0])
            
            M1 = int(T1[1])
            
            S1 = int(T1[2])
            
            d1 = datetime.datetime(Y1, MO1, D1, H1, M1 ,S1)
            
            str2 = need2.tRunTime.split()
            
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
                
                needs.append(need1)
                
                i = i + 1
                
            else :
                
                needs.append(need2)
                
                j = j + 1
                
                
            if i == c1 and j == c2 :
                
                return needs
            
            if i ==c1 and j != c2:
                
                t = j
                
                for j in range(t , c2):
                    
                    needs.append(needs2[j])
                    
                return needs
                    
            if i !=c1 and j == c2:
                
                t = i
                
                for i in range(t, c1):
                    
                    needs.append(needs1[i])
                    
                return needs
                
                
            
            
            
        