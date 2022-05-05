from aflutil import helper
from aflutil import AFLGame 
import heapq

'''
The final challenge is to walk the corrected data and return the five
biggest home wins and losses in the dataset. Use the AFLGames class 
for this one. Create a list of games with their scores. Once you have
the list, you can apply the function heapq.nlargest as discussed in the
lectorial to find final results. There are other ways, but this one
should be straightforward if you understand the example we show.
'''

def find_biggest_wins (data_array,where):

  ''' TODO by you. heapq.nlargest is the best solution hint I can
      give you.
  '''

  return topfive

if __name__ == "__main__":
  input_array = 'results/array-updated.tsv'
  output_file = 'results/bigwins.txt'

  data_array = helper.load_tsv_file(input_array) 
  home_wins = find_biggest_wins (data_array,'H')
  away_wins = find_biggest_wins (data_array,'A')
  helper.write_top_five (home_wins, away_wins,output_file)

