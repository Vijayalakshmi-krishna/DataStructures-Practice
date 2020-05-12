"""
Copyright (C) 2020 vijayalakshmisuresh

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
"""
PROBLEM 2
Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
Example 1:
SAMPLE Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
SAMPLE Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]


"""
def set_mat_zero():
    inp_list = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    # inp_list= [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    n=len(inp_list)
    # flag = 0
    n_row=len(inp_list)
    n_col=len(inp_list[0])
    print (n_col , n_row)
    index_list=[]
    for i in range(0,n_row):
        for j in range(0,n_col):
            # Check for the element zero
            # If match occurs
            if inp_list [i][j] == 0:
                row = i
                col = 0
                #Collect the row indexes
                while col < n_col:
                    index_list.append([row,col])
                    col += 1
                col = j
                row = 0
                #Collect the column indexes
                while row < n_row:
                    index_list.append([row,col])
                    row += 1
    print(index_list)
    #set element to 0 for the collected indexes
    for i in range(0,len(index_list)):
        k= index_list[i]
        ind1=k[0]
        ind2=k[1]
        inp_list[ind1][ind2] = 0
    print(inp_list)

if __name__ == "__main__":
    set_mat_zero()