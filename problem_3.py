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
PROBLEM 3
Group Anagrams
Given an array of strings, group anagrams together.
Example:
SAMPLE Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
SAMPLE Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter.

"""
def find_anagrams():
    inp_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    temp_list=[]
    op_list=[]
    i=0
    while inp_list:
        curr_str=inp_list[i]
        temp_list=check_list(curr_str,inp_list)
        for j in temp_list:
            inp_list.remove(j)
        op_list.append(temp_list)
    print(op_list)

'''
check_list()
For anagrams program
return anagram strings of the current string
'''

def check_list(curr_str,inp_list):
    temp_list=[]
    for i in inp_list:
        count = 0
        for char in curr_str:
            if char in i:
                count += 1
        if count == len(curr_str):
            temp_list.append(i)
    return temp_list


if __name__ == "__main__":
    find_anagrams()