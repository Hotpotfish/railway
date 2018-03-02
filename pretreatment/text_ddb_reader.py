import ddb_data
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
        
        self.records = []
        
        gc.collect()
        
        ddb_file = open(self.text_path)   
        
        line = ddb_file.readline()
        
        while line:
            
            temp_record = ddb_data.ddb()
            
            #print line
             
            str = line.split()
            
            temp_record.tRunTime = str[0] + " " +  str[1]
            
            temp_record.nRunSpeed = str[2]
            
            temp_record.nRunStone = str[3]
            
            temp_record.sTrainNo = str[4]
            
            temp_record.sCarNo = str[5]
            
            temp_record.nZyPower = str[6]
            
            temp_record.nFyPower = str[7]
            
            self.records.append(temp_record)
             
            self.number = self.number + 1
             
            line = ddb_file.readline()
            
        ddb_file.close()
        
        return self.records
        
        
