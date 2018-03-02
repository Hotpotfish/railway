import tcm_data
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
        
        tcm_file = open(self.text_path)   
        
        line = tcm_file.readline()
        
        self.records = []
        
        gc.collect()
        
        
        while line:
            
            temp_record = tcm_data.tcm()
            
            #print line
             
            str = line.split()
            
            temp_record.tRunTime = str[0] + " " + str[1]
            
            temp_record.nRunSpeed = str[2]
            
            temp_record.nRunStone = str[3]
            
            temp_record.sTrainNo = str[4]
            
            temp_record.sCarNo = str[5]
            
            temp_record.nErr = str[6]
            
            temp_record.nGear = str[7]
            
            temp_record.nLargeGear = str[8]
            
            temp_record.nSmallGear = str[9]
            
            self.records.append(temp_record)
             
            self.number = self.number + 1
             
            line = tcm_file.readline()
            
        tcm_file.close()
        
        return self.records
        
        
