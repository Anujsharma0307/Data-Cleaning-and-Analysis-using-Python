from aflutil import helper

''' 
A function to compute a final scored based on the traditional
per quarter score format used by the AFL. Columns 7 and 5 will
contain something like '1.0 1.4 4.5 5.8'. These map to the 
four quarters and are cumulative. So '5.8' means the team
scored 5 goals worth 6 points each and had 8 behinds for 
1 point each, which should sum up to 38. So the function
should simply take a scoring row and return the final
score for that field. This is not as easy as it looks.
You need to split on spaces and then again on '.'. Once
You have the goals and behinds from the string, you need
to cast them to an integer to do any computations with
them.
'''
def compute_score(S):
    result=0
    
 # Inputs the string of the scores and splits the numbers by "."  
    i,j = map(int , S.split()[-1].split("."))
    result = (i*6)+j
    
    return result
'''
Once you can compute a score using a scoring field,
you can validate every score, win/loss/tie, and score
difference in the raw data. The function should take
the data array, and validate columns 6,8,10,11 of every
row, which are For Final Score, Against Final Score, Result,
and Margin respectively. If a row is incorrect, you should
correct it. So the function accepts the data_array and
returns a modified data array that should have 100% of the
statistics correct.
'''
def validate_all_scores(data_array):
    global endResult
    for n, i in enumerate(data_array):

        self = i[5]
        selfTotal = i[6]
        opponent = i[7]
        opponentTotal = i[8]
        matchOutcome = i[9]
        winningMargin = i[10]

        scoreSelf = compute_score(self)
        scoreOpponent = compute_score(opponent)
        
#This validates final scores of the match 

        if scoreSelf != selfTotal:
            data_array[n][6] = str(scoreSelf)

        elif scoreOpponent != opponentTotal:
            data_array[n][8] = str(scoreOpponent)

        elif winningMargin != (scoreSelf - scoreOpponent):
            data_array[n][10] = str(scoreSelf - scoreOpponent)
            
#This validates the final outcome of the match 

            if scoreSelf == scoreOpponent:
                endResult = "D"
            elif (scoreSelf - scoreOpponent) > 0:
                endResult = "W"

            elif (scoreSelf - scoreOpponent) < 0:
                endResult = "L"

        elif matchOutcome != endResult:
            data_array[n][9] = str(endResult)

    return data_array
'''
The main fuction calls. These should not be modified in
your final version so be careful if you change anything
here.
'''

if __name__ == "__main__":
  output_dir = 'results/'
  error_log = 'results/error.log'
  teams_file = 'data/teams.in'
  input_array_file = 'results/array-initial.tsv'
  output_array_file = 'results/array-updated.tsv'

  helper.create_results_dir(output_dir)
  helper.zero_error_log(error_log)
  data_array = helper.load_tsv_file(input_array_file)
  data_array = validate_all_scores(data_array)
  helper.print_array(data_array,output_array_file)

