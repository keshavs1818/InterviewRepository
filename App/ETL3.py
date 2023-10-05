IN_FILE_NAME  = "C:\\SampleProjects\\ETL1\\Input\\CLASS3.txt"
OUT_FILE_NAME = "C:\\SampleProjects\\ETL1\\Output\\CLASS_OUT.txt"

out_file = open(OUT_FILE_NAME, "a")
ptr = 0
with open(IN_FILE_NAME, "r") as in_file:
    lines = in_file.readlines()
    for line in lines:
        lst = line.split("|")
        out_string = "|".join([lst[-1][:-1], lst[1], lst[2]])
        # print(out_string)
        if ptr > 0:
           out_file.write(out_string + "\n")
        ptr += 1
 
out_file.close()