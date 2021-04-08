    
import argparse
import glob, os
import os.path
import main

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str,  
                             help="inputfiles")
    #output requires value so used type=str
    parser.add_argument("--output", type=str,  
                             help="outputfile")
    #names doesn't require value so used store_true
    parser.add_argument("--names", action='store_true',
                             help="firstoperand")
    parser.add_argument("--genders", action='store_true', 
                             help="secondoperand")
    parser.add_argument("--dates", action='store_true',  
                             help="thirdoperand")
    parser.add_argument("--phones", action='store_true',  
                             help="fourthoperand")
    parser.add_argument("--stats", type=str,  
                             help="fifthoperand")
    parser.add_argument("--concept", type=str,  
                             help="concepts")
    
    
    args = parser.parse_args()
    
    result_dict={}
    file_summary=""
    if args.input:
        ip_files=args.input
        ip_files_list= glob.glob("*.txt")
    for file in ip_files_list:
        f=open(file, "r")
        document=f.read()
        
        if args.names:
            print("this is names redaction")
            names_result=main.names(document)
            result_dict["names"]=names_result[1]
#             print("this is names pattern ++++++++++++++++++++++++++++++++++++{}\n".format(result_dict["names"]))
        
        if args.genders:
            genders_result=main.genders(document)
            result_dict["genders"]=genders_result[1]
#             print("this is genders pattern ++++++++++++++++++++++++++++++++++++{}\n".format(result_dict["genders"]))

        if args.dates:
            dates_result=main.dates(document)
            result_dict["dates"]=dates_result[1]
#             print("this is dates pattern ++++++++++++++++++++++++++++++++++++{}\n".format(result_dict["dates"]))

        if args.phones:
            phones_result=main.phones(document)
            result_dict["phones"]=phones_result[1]
#             print("this is phones pattern ++++++++++++++++++++++++++++++++++++{}\n".format(result_dict["phones"]))

        if args.concept:
            concept_name = args.concept
            concept_result=main.concept(document,concept_name)
            result_dict["concepts"]=concept_result[1]
#             print("this is concept pattern ++++++++++++++++++++++++++++++++++++{}\n".format(result_dict["concepts"]))

        if args.stats:
            print(result_dict)
            file_summary += main.stats(result_dict)
            stats_file = args.stats
            
            if stats_file=="stderr":
                stats_file_obj = open(stats_file, "w")
                stats_file_obj.write(file_summary)
                stats_file_obj.close()
            else:
                stats_file_obj = open(stats_file, "w")
                stats_file_obj.write(file_summary)
                stats_file_obj.close()
            
            if args.output:            
            save_path = args.output
            output_file = os.path.join(save_path,str(file)[:len(file)-4]+".redacted")         
#             print(output_file)
            file_obj = open(output_file, "w",encoding = "utf-8")
            file_obj.write(main.redacted_doc(result_dict,document))
            file_obj.close()
    if stats_file=="stdout":
        print(file_summary)

