IN_FILE_NAME  = "C:\\SampleProjects\\ETL1\\Input\\CLASS1.txt"
OUT_FILE_NAME = "C:\\SampleProjects\\ETL1\\Output\\CLASS_OUT.txt"

out_file = open(OUT_FILE_NAME, "w")
with open(IN_FILE_NAME, "r") as in_file:
    lines = in_file.readlines()
    for line in lines:
        lst = line.split("|")
        out_string = "|".join([lst[3][:-1], lst[1], lst[0]])
        # print(out_string)
        out_file.write(out_string + "\n")
 
out_file.close()