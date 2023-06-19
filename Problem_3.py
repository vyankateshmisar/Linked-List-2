"""
Problem : 3

Time Complexity : O(1)
Space Complexity : O(1)

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

Changing the value in the current node to the value in next node
then changing deleting the link between the current and next node and
linking the current node to the next of next node. Resulting in deletion of one node

"""

# delete without head pointer

'''
    Your task is to delete the given node from
	the linked list, without using head pointer.
	
	Function Arguments: node (given node to be deleted) 
	Return Type: None, just delete the given node from the linked list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        #code here
        curr_node.data=curr_node.next.data
        curr_node.next=curr_node.next.next
        