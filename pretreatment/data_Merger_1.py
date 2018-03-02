import os
import train_data
import text_ddb_reader
import text_tax_reader
import text_tcm_reader

import sys

class Merger(object):
    '''
    classdocs
    '''
    catalog_path = None
    
    temp_1_path = None

    def __init__(self, catalog_path,temp_1_path):
        '''
        Constructor
        '''
        self.catalog_path = catalog_path
        
        self.temp_1_path = temp_1_path
        
    
    def Merge(self):
        
        # train_dict = {}
        
        train_name_1 = os.listdir(self.catalog_path)
        
        for i in range(0, len(train_name_1)):
            
            print train_name_1[i]
            
            train_name_2 = train_name_1[i][0: 9]
            
            temp_train_data = train_data.train()
            
            if train_name_1[i][26: 29] == "ddb":
                
                temp_train_data.ddbs = text_ddb_reader.reader(self.catalog_path + train_name_1[i]).read()
                
                ddb_file_path = self.temp_1_path + train_name_2 + "_" + "ddb" + ".csv"
                
                f1 = open(ddb_file_path,'a+')
            
                for j in range(0, len(temp_train_data.ddbs)):
                    
                    
                    f1.write(temp_train_data.ddbs[j].tRunTime + " " +
                            
                            temp_train_data.ddbs[j].nRunSpeed + " " +
                            
                            temp_train_data.ddbs[j].nRunStone + " " +
                            
                            temp_train_data.ddbs[j].sTrainNo + " " +
                            
                            temp_train_data.ddbs[j].sCarNo + " " +
                            
                            temp_train_data.ddbs[j].nZyPower + " " +
                            
                            temp_train_data.ddbs[j].nFyPower + "\n"
                             
                            )
                f1.close()
                
                
            if train_name_1[i][26: 29] == "tax":
                    
                temp_train_data.taxs = text_tax_reader.reader(self.catalog_path + train_name_1[i]).read()
                
                tax_file_path = self.temp_1_path + train_name_2 + "_" + "tax" + ".csv"
                
                f2 = open(tax_file_path,'a+')
            
                for k in range(0, len(temp_train_data.taxs)):
                    
                    if temp_train_data.taxs[k].nErr == '1':
                        
                        continue
                    
                    f2.write(temp_train_data.taxs[k].tRunTime + " " +
                            
                            temp_train_data.taxs[k].nRunSpeed + " " +
                            
                            temp_train_data.taxs[k].nRunStone + " " +
                            
                            temp_train_data.taxs[k].sTrainNo + " " +
                            
                            temp_train_data.taxs[k].sCarNo + " " +
                            
                            temp_train_data.taxs[k].nErr + " " +
                            
                            temp_train_data.taxs[k].nSiteNo + " " +
                            
                            temp_train_data.taxs[k].nDriverNo + " " +
                            
                            temp_train_data.taxs[k].nDriverNo2 + " " +
                            
                            temp_train_data.taxs[k].nJiaoLuHao + " " +
                            
                            temp_train_data.taxs[k].nWeight + " " +
                            
                            temp_train_data.taxs[k].nLength + " " +
                            
                            temp_train_data.taxs[k].nCarCount + "\n"
                            )
                f2.close()
            if train_name_1[i][26: 29] == "tcm":
                   
                temp_train_data.tcms = text_tcm_reader.reader(self.catalog_path + train_name_1[i]).read()
                
                tcm_file_path = self.temp_1_path + train_name_2 + "_" + "tcm" + ".csv"
                
                f3 = open(tcm_file_path,'a+')
            
            
                for z in range(0, len(temp_train_data.tcms)):
                    
                    if temp_train_data.tcms[z]. nErr == '1':
                        
                        continue
                    
                    f3.write(temp_train_data.tcms[z].tRunTime + " " +
                            
                            temp_train_data.tcms[z].nRunSpeed + " " +
                            
                            temp_train_data.tcms[z].nRunStone + " " +
                            
                            temp_train_data.tcms[z].sTrainNo + " " +
                            
                            temp_train_data.tcms[z].sCarNo + " " +
                            
                            temp_train_data.tcms[z]. nErr + " " +
                            
                            temp_train_data.tcms[z].nGear + " " +
                            
                            temp_train_data.tcms[z].nLargeGear + " " +
                             
                            temp_train_data.tcms[z].nSmallGear + "\n"
                             
                            )
                f3.close()
            
              
            print sys.getsizeof(temp_train_data.ddbs)
            
            print sys.getsizeof(temp_train_data.taxs)
            
            print sys.getsizeof(temp_train_data.tcms)
            
        
            
            
                
        
