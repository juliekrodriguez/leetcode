/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit.
 Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

var addTwoNumbers = function(l1, l2) {
    // Create a new ListNode object and assign it to the dummyNode variable
    let dummyNode = new ListNode(0);
    
    // Assign dummyNode to the newHead variable
    let newHead = dummyNode;
    
    // Initialize the carry variable to 0
    let carry = 0;
    
    // Use a while loop to iterate through both lists, l1 and l2
    while(l1 || l2){
        // If l1 is not null, assign its value to valueList1; otherwise, assign 0 to valueList1
        let valueList1 = l1 ? l1.val : 0;
        // If l2 is not null, assign its value to valueList2; otherwise, assign 0 to valueList2
        let valueList2 = l2 ? l2.val : 0;
        
        // Compute the sum of the values in valueList1, valueList2, and carry
        let sum = valueList1 + valueList2 + carry;
        
        // Compute the carry value for the next iteration
        carry = Math.floor(sum/10);
        
        // Compute the value of the new node to be added to the linked list
        sum = sum % 10;
        
        // Create a new ListNode object with value equal to sum, and assign it to the next property of newHead
        newHead.next  = new ListNode(sum);
        
        // Advance both pointers to the next nodes in l1 and l2, if they are not null
        l1 = l1 && l1.next;
        l2 = l2 && l2.next;
        
        // Move newHead to the next node in the linked list
        newHead = newHead.next;
    }
    
    // If there is a carry value remaining after iterating through both lists, add a new node with that value to the linked list
    if(carry > 0) newHead.next = new ListNode(carry);
    
    // Return the linked list starting from the second node of the dummyNode
    return dummyNode.next;
    
};
