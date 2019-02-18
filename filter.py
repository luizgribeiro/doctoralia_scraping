from more_itertools import unique_everseen

with open('info.csv', 'r') as in_file, open('docs_info.csv', 'w') as out_file:
     out_file.writelines(unique_everseen(in_file))


