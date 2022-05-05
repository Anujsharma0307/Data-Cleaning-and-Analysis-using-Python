from aflutil import helper

'''
Main function to implement. To get it working,
you need open in input file in input_files and
walk each line by line. The text files are
cleanly formatted markdown with all data using
the '|' separator. So, each line if not empty
can be split into fields using the split function.
You can keep the data clean by using the strip
operator to remove trailing and leading spaces
in lines and fields.
Your goal is simple -- build a two dimensional
array (list of lists) where every line adheres
to the teams_header, which is 14 columns of data.
You can then convert this to a pandas dataframe
or easily compute and validate simple statistical
data by walking each rown in the list as you will
know what information it should contain.
'''
def process_teams (input_files):
    data_array = []
# Read from the input    
    for x in range(len(input_files)):
        f = open(input_files[x], "r")
        counter = 0
        
# Separates the line by '|' and and the lists of strings with the name fields  

        for line in f:
            line = line.strip()
            fields = line.split('|')
            if len(fields) == 3:
                if fields[1] != " --- ":
                    
# Appends the two columns Teams and Year          

                    if counter == 0:
                        Team = fields[1].strip()
                        
                    else:
                        Year = fields[1].strip()
                        
                    counter = counter + 1
                    
# Stores the rest of data from the file    

            elif len(fields) == 15:
        
# Removes the header lines from the file           

                if fields[4] != fields[6]:
                    del fields[0]
                    del fields[13]
                    
                    for i in range(len(fields)):
                        fields[i] = fields[i].strip()
                        
# Inserts Team and Year Columns into final data array                   
                    fields.insert(0, Team)
                    fields.insert(1, Year)
                    data_array.append(fields)
                    
    return data_array
'''
This is the main function.
You should not modify this unless you
want to print the header in testing.
Make sure to comment it out in your
submission or you'll fail the
test harness.
'''
if __name__ == "__main__":
  output_dir = 'results/'
  error_log = 'results/error.log'
  teams_file = 'data/teams.in'
  array_file = 'results/array-initial.tsv'

  helper.create_results_dir(output_dir)
  helper.zero_error_log(error_log)
  teams_files = helper.read_input_file_names(teams_file)
  data_array = process_teams(teams_files)
  #helper.print_header()
  helper.print_array(data_array,array_file)

