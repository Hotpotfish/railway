import os
import need_data
import text_need_reader


class Merger(object):
    
    output_path = None
    
    output1_path = None

    def __init__(self, output_path, output1_path):
        
        self.output_path = output_path
        
        self.output1_path = output1_path
        
    def Merge(self):
        
        temp_names = os.listdir(self.output_path)
        
        count = len(temp_names) 
        
        for i in range(0, count):
            
            tn = temp_names[i][0:9]
            
            needs = text_need_reader.reader(self.output_path + tn + ".csv").read()
            
            self.write(tn, needs)
            
            print "!!"
     
    def write(self, tn, needs):
        
        fw1 = open(self.output1_path + tn + "_up" + ".csv", "a+")
        
        fw2 = open(self.output1_path + tn + "_down" + ".csv", "a+")
            
        for i in range(1, len(needs)):
            
            a = int(needs[i].nRunStone) - int(needs[i - 1].nRunStone)
            
            if a >= 0 :
                
                    fw1.write(needs[i].tRunTime + " " + 
                          
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
                          
                          "\n")
               
            else :
                
                    fw2.write(needs[i].tRunTime + " " + 
                       
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
                       
                       "\n")
                     
        fw1.close()
        fw2.close()
            
        
