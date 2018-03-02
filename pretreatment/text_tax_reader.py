import tax_data
import gc

class reader(object):
    '''
    classdocs
    '''
    
    text_path = None
    
    number = 0
    
    records = []

    def __init__(self, text_path):
        '''
        Constructor
        '''
        
        self.text_path = text_path
        
    def read(self):
            
        tax_file = open(self.text_path)   
    
        line = tax_file.readline()
    
        self.records = []
        
        gc.collect()
        
        while line:
            
            #print line
            
            temp_record = tax_data.tax()
             
            str = line.split()
            
            temp_record.tRunTime = str[0] + " " + str[1]
            
            temp_record.nRunSpeed = str[2]
            
            temp_record.nRunStone = str[3]
            
            temp_record.sTrainNo = str[4]
            
            temp_record.sCarNo = str[5]
            
            temp_record.nErr = str[6]
            
            temp_record.nSiteNo = str[7]
            
            temp_record.nDriverNo = str[8]
            
            temp_record.nDriverNo2 = str[9]
            
            temp_record.nJiaoLuHao = str[10]
            
            temp_record.nWeight = str[11]
            
            temp_record.nLength = str[12]
            
            temp_record.nCarCount = str[13]
            
            self.records.append(temp_record)
      
            self.number = self.number + 1
            
            line = tax_file.readline()
            
        tax_file.close()
    
        return self.records
                
        
