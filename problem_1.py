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
PROBLEM 1
3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
SAMPLE INPUT:
a = [-1, 0, 1, 2, -1, -4],

SAMPLE OUTPUT:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
def unique_trip():

    op_list=[]
    arr=[-1, 0, 1, 2, -1, -4]
    for i in range(0,len(arr) - 2):
        # num1=arr[i]
        for j in range(i + 1,len(arr) - 1):
            # num2=arr[j]
            for k in range(j + 1,len(arr)):
                # num3 = arr[k]
                if arr[i] + arr[j] + arr[k] == 0:
                    op_list.append([arr[i],arr[j],arr[k]])
    print(op_list)

#PROBLEM 1 ALTER METHOD

def uniq_trip_new():
    arr = [0, -1, 2, -3, 1]
    op_list=[]
    n=len(arr)
    arr.sort()
    for i in range(0,n-1):
        l = i + 1
        r= n - 1
        x = arr[i]
        while l < r:
            if(x + arr[l] + arr[r] == 0):
                op_list.append([x , arr[l] , arr[r]])
                l = l + 1
                r = r - 1
            elif(x + arr[l] + arr[r] < 0):
                l = l + 1
            else:
                r = r - 1
    print(op_list)


if __name__ == "__main__":
    unique_trip()
    uniq_trip_new()


