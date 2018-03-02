import data_Merger_1
import data_Merger_2
import data_Merger_3
import data_filter

def main():
    
    
    
    #data_Merger.Merger("input\\").Merge()
    data_Merger_1.Merger("input\\","temp_1\\").Merge()
    
    data_filter.filter("temp_1\\","temp_2\\").scan_and_write()
    
    data_Merger_2.Merger("temp_2\\","output\\").Merge()
    
    data_Merger_3.Merger("output\\","output1\\").Merge()
    
    print "success"
    

if __name__ == '__main__':
    
    main()
    
    
