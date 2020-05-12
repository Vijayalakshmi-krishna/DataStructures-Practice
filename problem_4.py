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
PROBLEM 4
Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

SAMPLE Input: nums = [1,2,3,1]
SAMPLE Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

'''

def find_peak(a):
    op_list = [];
    if a[0] > a[1]:
        op_list.append(0);
        #Comparing the previous and next elements
    if a[n-1] > a[n-2]:
        op_list.append(n-1);
    for i in range(1, n-1):
        key = a[i];
        if key > a[i - 1] and key > a[i + 1]:
            op_list.append(i)
    return op_list

if __name__ == "__main__":
    a = [1, 2, 1, 3, 5, 6, 4];
    n = len(a);
    print(find_peak(a))