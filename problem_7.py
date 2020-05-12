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
'''
PROBLEM 7
Merge Intervals
Given a collection of intervals, merge all overlapping intervals.
Example 1:
SAMPLE Input: [[1,3],[2,6],[8,10],[15,18]]
SAMPLE Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

'''

def mergeIntervals(arr,op_list):
    """Merge intervals in the given list
        Args:
            arr: input list
            op_list: output list after merge done
        Returns:
            op_list
        """
    #Exit condition for recursion
    if len(arr) < 2:
        return (op_list + arr)

    rn = arr[:2] #take only first two items
    rstart = rn[0][0] #start position
    rend = rn[0][1] #end position
    ck = rn[1][0]
    # if merge found :append the rest of the list with the merge item
    if rstart < ck < rend:# Check the range of the two items
        rend = rn[1][1]
        return mergeIntervals([[rstart,rend]] + arr[2:],op_list)
    # if merge not found : append the second value with the rest of the list
    else:
        return mergeIntervals([rn[1]] + arr[2:], op_list + [rn[0]])

if __name__ == "__main__":
    arr =  [[1,3],[2,5],[6,7]]
    res = mergeIntervals(arr,[])
    print (res)
