# LeetCode-Practice-from-Scratch
This repo is created to record my process of practicing LeetCode coding problems.

# Acknowledgement
Thanks to [代码随想录](https://www.programmercarl.com) for giving a detailed instruction on **how to choose the problems** and in what **order** to solve them. I am following this guide to practice LeetCode problems.

# Catalogue
> **Array**: </br>
    1. [Binary Search](#binary-search) and [related problems](#applications) </br>
    2. [Remove Element](#remove-element) and [related problems](#applications-1) </br>
    3. [squares-of-a-sorted-array](#squares-of-a-sorted-array) </br>
    4. [minimum-size-subarray-sum](#miminum-size-subarray-sum) and [related problems](#applications-2) </br>
    5. [Spiral Matrix](#spiral-matrix) </br>
> **List**: </br>
    1. [remove-linked-list-elements](#remove-linked-list-elements) </br>
    2. [design-linked-list](#design-linked-list) </br>
    3. [reverse-linked-list](#reverse-linked-list) </br>
    4. [swap-nodes-in-pairs](#swap-nodes-in-pairs) </br>
    5. [remove-nth-node-from-end-of-list](#remove-nth-node-from-end-of-list) </br>
    6. [intersection-of-two-linked-lists-lcci](#intersection-of-two-linked-lists) </br>
    7. [Linked List Cycle-ii](#linked-list-cycle-ii) </br>
> **Hash Table**: </br>
    1. [valid-anagram](#valid-anagram) </br>
    2. [intersection-of-two-arrays](#intersection-of-two-arrays) </br>
    3. [happy-number](#happy-number) </br>
    4. [two-sum](#two-sum) </br>
    5. [four-sum-ii](#four-sum-ii) </br>
    6. [3sum](#3sum) </br>
    7. [4sum](#4sum) </br>
> **String**: </br>
    1. [reverse-string](#reverse-string) </br>
    2. [reverse-string-ii](#reverse-string-ii) </br>
    3. [replace-whitespace](#replace-whitespace) </br>
    4. [reverse-words-in-a-string](#reverse-words-in-a-string) </br>
    5. [zuo-xuan-zhuan-zi-fu-chuan-lcof](#zuo-xuan-zhuan-zi-fu-chuan-lcof) </br>
    6. [KMP / find-the-index-of-the-first-occurrence-in-a-string](#kmp-algo--find-the-index-of-the-first-occurrence-in-a-string) </br>
    7. [repeated-substring-pattern](#repeated-substring-pattern) </br>
> **Stack and Queue**: </br>
    1. [implement-queue-using-stacks](#implement-queue-using-stacks) </br>
    2. [implement-stack-using-queues](#implement-stack-using-queues) </br>
    3. [remove-all-adjacent-duplicates-in-string](#remove-all-adjacent-duplicates-in-string) </br>
    4. [valid-parentheses](#valid-parentheses) </br>
    5. [evaluate-reverse-polish-notation](#evaluate-reverse-polish-notation) </br>
    6. [sliding-window-maximum](#sliding-window-maximum) </br>
    7. [top-k-frequent-elements](#top-k-frequent-elements) </br>
> **Binary Tree**: </br>
    1. [binary-tree-preorder-traversal](#binary-tree-preorder-traversal) </br>
    2. [binary-tree-inorder-traversal](#binary-tree-inorder-traversal) </br>
    3. [binary-tree-postorder-traversal](#binary-tree-postorder-traversal) </br>
    4. [binary-tree-level-order-traversal](#binary-tree-level-order-traversal) </br>
    5. [invert-binary-tree](#invert-binary-tree) </br>
    6. [symmetric-tree](#symmetric-tree) </br>
    7. [maximum-depth-of-binary-tree](#maximum-depth-of-binary-tree) </br>
    8. [minimum-depth-of-binary-tree](#minimum-depth-of-binary-tree) </br>
    9. [count-complete-tree-nodes](#count-complete-tree-nodes) </br>
    10. [balanced-binary-tree](#balanced-binary-tree) </br>
    11. [binary-tree-paths](#binary-tree-paths) </br>
    12. [sum-of-left-leaves](#sum-of-left-leaves) </br>
    13. [find-bottom-left-tree-value](#find-bottom-left-tree-value) </br>
    14. [Path Sum](#path-sum) </br>
    15. [Path Sum ii](#path-sum-ii) </br>
    16. [construct-binary-tree-from-inorder-and-postorder-traversal](#construct-binary-tree-from-inorder-and-postorder-traversal) </br>
    17. [construct-binary-tree-from-preorder-and-postorder-traversal](#construct-binary-tree-from-preorder-and-postorder-traversal) </br>
    18. [maximum-binary-tree](#maximum-binary-tree) </br>
    19. [merge-two-binary-trees](#merge-two-binary-trees) </br>
    20. [search-in-a-binary-search-tree](#search-in-a-binary-search-tree) </br>
    21. [validate-binary-search-tree](#validate-binary-search-tree) </br>
    22. [minimum-absolute-difference-in-bst](#minimum-absolute-difference-in-bst) </br>
    23. [find-mode-in-binary-search-tree](#find-mode-in-binary-search-tree) </br>
    24. [lowest-common-ancestor-of-a-binary-tree](#lowest-common-ancestor-of-a-binary-tree) </br>
    25. [lowest-common-ancestor-of-a-binary-search-tree](#lowest-common-ancestor-of-a-binary-search-tree) </br>
    26. [insert-into-a-binary-search-tree](#insert-into-a-binary-search-tree) </br>
    27. [delete-node-in-a-bst](#delete-node-in-a-bst) </br>
    28. [trim-a-binary-search-tree](#trim-a-binary-search-tree) </br>

# Array
## Binary Search
> My first version: [Binary Search](Array/binary_search/binary_search.py) </br>
> Problem Link: [Chinese Version](https://leetcode.cn/problems/binary-search/), [English Version](https://leetcode.com/problems/binary-search/)
#### Missing Keys:
1. when calculating the 'middle', I did not consider **overflowing of the integer type**, using 
```python
middle = (left + right) // 2
```
instead of
```python
middle = left + (right - left) // 2
```
1. referring to [solution](https://www.programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html#%E6%80%9D%E8%B7%AF), remember to define whether the target is in the range of [left, right] or [left, right). Though in my version I consider the middle as a decision boundary.

#### Others to Note:
The conditions using **binary search** are usually **sorted** and **non-repetitive elements**.

#### Applications: 
1. **Search Insert Position:**
    > My first version: [Search Insert Position](Array/binary_search/search-insert-position.cpp) </br>
    > Problem Link: [Chinese Version](https://leetcode-cn.com/problems/search-insert-position/), [English Version](https://leetcode.com/problems/search-insert-position/)

    **Why Using Binary Search:**
    1. The array is sorted.
    2. The array is non-repetitive.

    **Key**: Classify the different situations of the target number and consider the corner cases.

## Remove Element
> My first version: [Remove Elements](Array/remove_element/remove-element.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/remove-element/), [English Version](https://leetcode.com/problems/remove-element/)

#### Keys:
1. Use two pointers, one for the current element and the other for the position to be replaced. (**Two Pointers Method or 双指针法**)
2. Only using the original array and the length of the array, **no extra array is needed**.
3. The block:
    ```cpp
    temp[result] = nums[i];
    result++;
    ```
    can be replaced by:
    ```cpp
    nums[result++] = nums[i];
    ```
    Try to be familiar with it.

#### Applications:
1. **Remove Duplicates from Sorted Array**
    > My first version: [Remove Duplicates from Sorted Array](Array/remove_element/remove-duplicates-from-sorted-array.cpp) </br>
    > Problem Link: [Chinese Version](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/), [English Version](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
    
    **Why Using Two Pointers Method:**: the array is sorted in **non-descending order**. So the duplicated elements are adjacent to each other. </br>
    **Think about when the array is not sorted:** the array is not sorted in **non-descending order**. So the duplicated elements are not adjacent to each other. In this case, we can use **Hash Table** to solve the problem. But the time complexity is O(n) and the space complexity is O(n).

## Squares of a Sorted Array
> My first version: [Squares of a Sorted Array](Array/squares_of_a_sorted_array/squares_of_a_sorted_array.cpp) </br>
> Second version: [Squares of a Sorted Array2](Array/squares_of_a_sorted_array/squares_of_a_sorted_array2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/squares-of-a-sorted-array/), [English Version](https://leetcode.com/problems/squares-of-a-sorted-array/)

#### Keys: (Two Pointers Method)
1. In my **first version**, I stuck to the thinking that **I have to sort the result array from left to right in an ascending order**. So, I first use binary search to find the decision boundary of positive and negative numbers, and then use two pointers to merge the two sorted arrays. However, this method is not efficient enough.
2. In my **second version**, not implementing the sorting, I just use two pointers to merge the two sorted arrays in descending order and return the result array from the end of the array to the start. </br>

## Miminum Size Subarray Sum
> My first version: [Minimum Size Subarray Sum](Array/minimum_size_subarray_sum/minimum_size_subarray_sum.cpp) *This first version cannot pass the unit tests provided by LeetCode.* </br>
> Second version: [Minimum Size Subarray Sum2](Array/minimum_size_subarray_sum/minimum_size_subarray_sum2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/minimum-size-subarray-sum/), [English Version](https://leetcode.com/problems/minimum-size-subarray-sum/)

#### Keys: Sliding Window (Still Two Pointers Method)
1. In my **first version**, I used two pointers, one from the start and the other from the end of the array, to move towards the middle, and find a subarray that cannot be reduced anymore. Nevertheless, this method has an obvious fallacy that it **only considers the partial optimized solution, without a general optimized solution, which is quite like greedy algorithm**. There are many cases this method cannot handle.</br>
2. The second version is about **Sliding Window**, which is a kind of **two pointers method**. It includes all situations and heuristically prevents certain combinations that are not optimal. </br> Actually, there are two kinds of sliding window: **iterate the starting pointer** and **iterate the ending pointer**. In this version, we iterate the start pointer. </br>

#### Applications:
1. **fruit into baskets**:
   > My first version: [fruit into baskets](Array/fruit-into-baskets/fruit-into-baskets.cpp) *This version cannot pass all the tests due to the time limit exceediing.* </br>
   > Second version: [fruit into baskets2](Array/fruit-into-baskets/fruit-into-baskets2.cpp) </br>
   > Problem Link: [Chinese Version](https://leetcode-cn.com/problems/fruit-into-baskets/), [English Version](https://leetcode.com/problems/fruit-into-baskets/)

   **Keys**:
   1. In my **first version**, the thought is simple: for every start point, there is only one situation for the number of fruits, so I just need to **iterate all the start points**, i.e. from start to the end, to find the most fruits I can get. But obviously, this can lead to O($n^2$) time complexity.
   2. Applying the thought of **sliding window**, I modify my first version into the second version. The essence is very similar to the previous problem. But this question chooses **iterating the end pointer rather than the start pointer**. Actually, I find that it is more convenient to iterate the end pointer in **sliding window**.</br>

## Spiral Matrix
> My first version: [Spiral Matrix](Array/spiral-matrix-ii/spiral-matrix-ii.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/spiral-matrix-ii/), [English Version](https://leetcode.com/problems/spiral-matrix-ii/)

#### Keys:
   1. **Iterate the matrix layer by layer**. </br>
   2. Pay attention to how to **iterate the matrix layer by layer**. Find the things that ***don't change in every loop and keep consistent*** when judging the loop conditions (***whether the interval is close, open, left-close-right-open or left-open-right-close?***)</br>
   3. This is a very good example to show the manipulation of the loop and the index. </br>



# List
## Remove Linked List Elements
> My first version: [Remove Linked List Elements](List/remove-linked-list-elements/remove-linked-list-elements.cpp) *This version cannot pass the test.* (太菜了┭┮﹏┭┮)</br>
> My second version: [Remove Linked List Elements2](List/remove-linked-list-elements/remove-linked-list-elements2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/remove-linked-list-elements/), [English Version](https://leetcode.com/problems/remove-linked-list-elements/)

#### Keys
1. In my **first version**, I used a **dummy node** to solve the problem. But my implementation has an error, which is during each while loop, the **current pointer** updation is not correct. There are 2 problems: 
   ```cpp
        while (current->next != NULL){
            if (current->next->val == val){
                if (current->next == head){
                    head = head->next;
                }
                current->next = current->next->next;
            }
            current = current->next;
        }
    ```
   1. My logic is: whether the next node should be deleted or not, **I always move the current pointer to the next in one while loop** (so the current updation is outside of the ```if```). The problem is that, if I remove the last element of the list, the current will become NULL pointer. A test case showing this bug is [1, 2, 3, 5, 6] and remove target is 6. When removing the last element, the current will be a ```NULL``` pointer, leading to a bug.</br>
   2. The second problem is about the updation of ```head```. This is a sub-problem caused by previous problem. An example showing the ```head``` updation bug is [7, 7, 7, 7]. When removing the first element, the ```head``` will be updated to the second ```7```, but the current pointer also points to the second ```7```, missing the removal of the second ```7```. </br>
   3. The core of the above problem is that, **when removing the current's next node, the current pointer should not move to the next in this while loop. Because I don't have the information of the current's next' next**. </br>
   4. After modifying the code, the **[second version](List/remove-linked-list-elements/remove-linked-list-elements2.cpp)** can pass all the tests. </br>

## Design Linked List
> My first version: [Design Linked List](List/design-linked-list/design-linked-list.cpp) </br>
> Second version: [Design Linked List2](List/design-linked-list/design-linked-list2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/design-linked-list/), [English Version](https://leetcode.com/problems/design-linked-list/)

#### Keys
1. My first version can pass all the tests. But it is obvious that the code is **not well organized**. There are **too many corner cases judgement**. The core problem is that **A dummy head node and an attribute to record the internal size are missing.**</br>
2. [Second version](List/design-linked-list/design-linked-list2.cpp) is the **optimized version**. </br>

## Reverse Linked List
> My first version: [Reverse Linked List](List/reverse-linked-list/reverse-linked-list.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/reverse-linked-list/), [English Version](https://leetcode.com/problems/reverse-linked-list/)

#### Keys
1. The key is to **use three pointers' updation to iterate the whole linked list**. Pay attention to the **loop condition, that is when the loop is over, which pointer is the division boundary, is there any NULL pointer reference?** Drawing a graph and simulating the process can solve the problem.</br>

## Swap Nodes in Pairs
> My first version: [Swap Nodes in Pairs](List/swap-nodes-in-pairs/swap-nodes-in-pairs.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/swap-nodes-in-pairs/), [English Version](https://leetcode.com/problems/swap-nodes-in-pairs/)

#### Keys
1. Just simulate the process of swapping nodes. </br>
2. Pay attention to the **null pointer reference**. (今天终于一直有注意这个情况了！)</br>


## Remove Nth Node From End of List
> My first version: [Remove Nth Node From End of List](List/remove-nth-node-from-end-of-list/remove-nth-node-from-end-of-list.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/), [English Version](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

#### Keys
1. **"Two Pointers Method" 双指针法**. </br>
2. Corner case judgement. </br>

## Intersection of Two Linked Lists
> My first version: except for the brutal force method or the hashmap method, no idea </br>
> Answer: [Intersection of Two Linked Lists](List/intersection-of-two-linked-lists-lcci/intersection-of-two-linked-lists-lcci.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/), [English Version](https://leetcode.com/problems/intersection-of-two-linked-lists-lcci/)

#### Keys:
1. The reason why I cannot figure out the **$O(n)$** time method is that I do not utilize the condition that **all nodes after the intersection pointer will be the same**. So, two pointers method can dominate.

## Linked List Cycle-ii
> My first version: [Linked List Cycle-ii](List/linked-list-cycle-ii/linked-list-cycle-ii.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/linked-list-cycle-ii/), [English Version](https://leetcode.com/problems/linked-list-cycle-ii/)

#### Keys
1. **"Two Pointers Method" 双指针法. Once you meet with this problem, this method will pop up when encountering it again（xuasong:典型的套路题）**. </br>
2. Simulate the process of two pointers and find the internal mathmatical relationship between the two pointers. </br>

## Summary of Linked List
1. Most of the time, using a **dummy head node** can simplify the problem since it can avoid the **head node corner case**. </br>
2. Two pointers method is a **very common method** to solve the linked list problem. </br>
3. Pay attention to the **null pointer reference**. </br>

# Hash Table
## Valid Anagram
> My first version: [Valid Anagram](Hash-Table/valid-anagram/valid-anagram.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/valid-anagram/), [English Version](https://leetcode.com/problems/valid-anagram/)

#### Keys:
1. Array is a kind of hash table. The index is the key, and the value is the value. </br>

## intersection-of-two-arrays
> No idea other than brutal force method </br>
> Answer: [intersection-of-two-arrays](Hash-Table/intersection-of-two-arrays/intersection-of-two-arrays.cpp) </br>
> Since the answer uses the ```unordered_set``` container, I have to learn it. Answer link: https://www.programmercarl.com/0349.%E4%B8%A4%E4%B8%AA%E6%95%B0%E7%BB%84%E7%9A%84%E4%BA%A4%E9%9B%86.html#%E6%80%9D%E8%B7%AF</br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/intersection-of-two-arrays/), [English Version](https://leetcode.com/problems/intersection-of-two-arrays/)

## Happy Number
> My first version: [Happy Number](Hash-Table/happy-number/happy-number.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/happy-number/), [English Version](https://leetcode.com/problems/happy-number/)

#### Keys:
1. About the **loop or cycle** detection, if you have to search for the value in the loop, you can use the **set**. Since the set can guarantee the non-repetitiveness.</br>

## Two-sum
> My first version: [Two-sum](Hash-Table/two-sum/two-sum.cpp) </br>
> Porblem Link: [Chinese Version](https://leetcode-cn.com/problems/two-sum/), [English Version](https://leetcode.com/problems/two-sum/)

#### Keys:
1. why using hash map? I have to store the already searched **element and its corresponding index**, which is easy to connect to the "key-value pairs" concept in hash map.

## Four-sum-ii
> My first version: [Four-sum-ii](Hash-Table/four-sum-ii/four-sum-ii.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/four-sum-ii/), [English Version](https://leetcode.com/problems/four-sum-ii/)

#### Keys:
1. The brutal force method takes $O(n^4)$ time, which is not acceptable. </br>
2. Similar to the two-sum problem, we can use the hash map to store the sum of two elements and the corresponding number of pairs. </br>

## 3sum
> No idea except hash map. But the de repetition process is trivious and easily bring bugs. It cannot pass. [3sum](Hash-Table/3sum/3sum.cpp) </br>
> answer: [3sum](Hash-Table/3sum/3sum2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/3sum/), [English Version](https://leetcode.com/problems/3sum/)

#### Keys:
1. 首先看懂题目意思。。。说的是元组包含nums中的哪三个数的和为0，而不是这三个数索引的元组。
2. The hardest part is how to avoid repetition. If using **hash method** like [four sum](#four-sum-ii), it is very difficult because of a large number of corner cases.
3. Using **two pointers method**. Firstly sorting the array in order can give the pointers movement a hint. Then the repetition avoidance is easy to accomplish.

## 4sum
> My first version: [4sum](Hash-Table/4sum/4sum.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/4sum/), [English Version](https://leetcode.com/problems/4sum/)

#### Keys:
1. Very similar to the 3sum problem. Both problems utilize the **two pointers method**.
2. Remember the **overflow problem** and **cutting the branch problem**. Overflow can be caused by the **sum of two numbers**. Cutting the branch can reduce the time.

# String
## Reverse String
> My first version: [Reverse String](String/reverse-string/reverse-string.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/reverse-string/), [English Version](https://leetcode.com/problems/reverse-string/)

#### Keys:
1. Very basic problem, use the **two pointers method** to solve it. </br>

## Reverse String-ii
> My first version: [Reverse String-ii](String/reverse-string-ii/reverse-string-ii.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/reverse-string-ii/), [English Version](https://leetcode.com/problems/reverse-string-ii/)

#### Keys:
1. Actually, my **first version** is much more complex. The logic is tedious since the **for loop** of the string reversal repeats a lot. Define an additional function to handle this.</br>

## Replace whitespace
> My first version: [Replace white space](String/replace-whitespace/replace-whitespace.cpp) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/), [English Version](https://leetcode.com/problems/ti-huan-kong-ge-lcof/)

#### Keys:
1. understand that the string is actually the same as **character array**. So pay attention to the space allocation.
2. Think of **moving pointer from the backward** about the reallocation problem.
3. **Allocate the needed space in advance.**

## Reverse words in a string
> My first version: At first, I have no clear idea. </br>
> After exposure to the answer's thought, the second version: [Reverse words in a string](String/reverse-words-in-a-string/reverse-words-in-a-string.cpp) </br>
> Problem link: [Chinese Version](https://leetcode.cn/problems/reverse-words-in-a-string/submissions/), [English Version](https://leetcode.com/problems/reverse-words-in-a-string/)

#### Keys:
1. Two key points:
2. **How to eliminate the unwanted whitespaces?**: two pointers method. 
3. **How to reverse the order of words, but remain the order of characters in each word?**: reverse all the characters, then reverse each word sparated by white space.

## zuo-xuan-zhuan-zi-fu-chuan-lcof
> My first version: [zuo-xuan-zhuan-zi-fu-chuan-lcof](String/zuo-xuan-zhuan-zi-fu-chuan-lcof/zuo-xuan-zhuan-zi-fu-chuan-lcof.cpp) </br>
> Second version: [zuo-xuan-zhuan-zi-fu-chuan-lcof](String/zuo-xuan-zhuan-zi-fu-chuan-lcof/zuo-xuan-zhuan-zi-fu-chuan-lcof2.cpp) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/), [English Version](https://leetcode.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)

#### Keys:
1. In my first version, I consider that no extra space cannot be achieved. But concerning the reverse string operation, it is actually a **in-place operation**. So the extra space is not needed. </br>

## KMP algo / find-the-index-of-the-first-occurrence-in-a-string
> My first version: [find-the-index-of-the-first-occurrence-in-a-string, brutal force](String/find-the-index-of-the-first-occurrence-in-a-string/find-the-index-of-the-first-occurrence-in-a-string.cpp) </br>
> Second version:[KMP](String/find-the-index-of-the-first-occurrence-in-a-string/kmp.cpp) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/find-the-index-of-the-first-occurrence-in-a-string/), [English Version](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

#### Keys:
1. **Brutal force method** can solve the problem with $O(n*m)$ time complexity. </br>
2. **KMP algorithm** can solve the problem with $O(n+m)$ time complexity. </br>
3. Understand the **KMP algorithm**: 
   1. how to optimize the **brutal force method**?: use some already known information to avoid some useless comparisons. -> partial match table
   2. how to get partial match table?:
   ```python
   def getNxt(x):
        for i in range(x, 0, -1):
            if p[0:i] == p[x-i+1:x+1]:
                return i
        return 0
    ```
    This will cause $O(m^2)$ time complexity. So we can further optimize it. </br>
    3. how to further optimize the **KMP algorithm**?:
    如何更好地理解和掌握 KMP 算法? - 阮行止的回答 - 知乎
    https://www.zhihu.com/question/21923021/answer/1032665486
    核心的一点是：j一直是当前最长前缀的下一个位置；如果nxt[j] != nxt[i],说明当前后缀不能再用j匹配了，j必须缩小，而如何缩小呢？

## repeated-substring-pattern
> My first version: brutal force, incurs $O(n^2)$ time complexity. </br>
> second version: [repeated-substring-pattern](String/repeated-substring-pattern/repeated-substring-pattern.cpp) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/repeated-substring-pattern/), [English Version](https://leetcode.com/problems/repeated-substring-pattern/)

#### Keys:
1. The method is very delicate: concatenate the string with itself, then delete the first and the last character. If the string is in the concatenated string, then the string is a repeated substring pattern. </br>
2. It is apparent that this condition is sufficient. But how to prove that it is necessary? [answer](https://leetcode.cn/problems/repeated-substring-pattern/solution/zhong-fu-de-zi-zi-fu-chuan-by-leetcode-solution/)


# Stack and Queue
## implement-queue-using-stacks
> My first version: [implement-queue-using-stacks](Stack-and-Queue/implement-queue-using-stacks/implement-queue-using-stacks.cpp) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/implement-queue-using-stacks/), [English Version](https://leetcode.com/problems/implement-queue-using-stacks/)

#### Keys:
Very fundamental problem. Just pay attention to **when to update the out queue**. </br>

## implement-stack-using-queues
> My first version: [implement-stack-using-queues](Stack-and-Queue/implement-stack-using-queues/implement-stack-using-queues.cpp) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/implement-stack-using-queues/), [English Version](https://leetcode.com/problems/implement-stack-using-queues/)
> Basic problem so no more explanation.

## remove-all-adjacent-duplicates-in-string
> My first version: [remove-all-adjacent-duplicates-in-string](Stack-and-Queue/remove-all-adjacent-duplicates-in-string/remove-all-adjacent-duplicates-in-string.cpp) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/), [English Version](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)
> Basic problem so no more explanation.

## Valid Parentheses
> My first version: [Valid Parentheses](Stack-and-Queue/Valid-Parentheses/Valid-Parentheses.cpp) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/valid-parentheses/), [English Version](https://leetcode.com/problems/valid-parentheses/)
> Basic problem so no more explanation.

## evaluate-reverse-polish-notation
> My first version: [evaluate-reverse-polish-notation](Stack-and-Queue/evaluate-reverse-polish-notation/evaluate-reverse-polish-notation.cpp) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/), [English Version](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
> Basic problem so no more explanation.

## sliding-window-maximum
> My first version: [sliding-window-maximum](Stack-and-Queue/sliding-window-maximum/sliding-window-maximum.cpp) *This version exceeds the time constraint*</br>
> Second version: [sliding-window-maximum](Stack-and-Queue/sliding-window-maximum/sliding-window-maximum2.cpp) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/sliding-window-maximum/), [English Version](https://leetcode.com/problems/sliding-window-maximum/)

#### Keys:
1. The first version is a **brutal force method wtih $O(n^2)$ time complexity** . It is easy to understand but it exceeds the time constraint. </br>
2. The second version is implementing a descending queue using **double-ended queue with $O(n)$ time complexity**. Another name of this special data structure is **monotonic queue**. The ***essence*** is that:
   1.  when iterating from the **small index to large index**, if a number with low index is smaller than the number with higehr index, it will be **impossible** to occur in the result. To understand this, we should consider that the sliding window is a range from a small index to a large index, the lower index number will quit the window first, so if it is large, it is possible to occur in the result, but if it is small, it will never occur in the result since the latter number will always be over it.</br>
   2. However, how do we know that the large number, the front of the queue, is still in the sliding window? :
      1. We can use the index to record the position of the number. </br>
      2. Or we can use the **pop_front()** function to delete the number that is out of the sliding window. But how do we know that the front of the queue is the number quiting the sliding window? Actually, **we only need to delete those quiting numbers equal to the front of queue.** That is :
      ```cpp
      if (!q.empty() && q.front() == nums[i-1]) q.pop_front();
      ```
        </br>
3. An interesting point when implementing the algorithm: when pushing new numbers, the numbers in the queue should be **descending**. So we need to delete the numbers that are smaller than the new number. But what about the numbers that are equal to the new number? Actually, we **should** keep them in the queue.
    ```cpp
        while (!q.empty() && q.back() < nums[i]){
            q.pop_back();
        }
    ```
    In this line of code, the **<** sign can not be **<=**. If it is **<=**, the numbers that are equal to the new number will be deleted, but when the input case is like: [-7,-8,7,5,7,1,6,0] and k = 4, the problem rises. Since we delete the repeated **7**, when it quits the queue, all the **7** quits and this is not we want. 
    </br>

## top-k-frequent-elements
> I have no idea how to implement $O(nlogn)$ time complexity algo in this problem. </br>
> Answer link: [top-k-frequent-elements](Stack-and-Queue/top-k-frequent-elements/top-k-frequent-elements.cpp) </br>
> The analysis is here (**much more deailed and clear than me and I need to reimplement this problem later**): https://leetcode.cn/problems/top-k-frequent-elements/solution/qian-k-ge-gao-pin-yuan-su-by-leetcode-solution/

# Binary Tree
## binary-tree-preorder-traversal
> **Recursive** version: [binary-tree-preorder-traversal](Binary-Tree/binary-tree-preorder-traversal/binary-tree-preorder-traversal.cpp) </br>
> **Iteration Version1**: [binary-tree-preorder-traversal2](Binary-Tree/binary-tree-preorder-traversal/binary-tree-preorder-traversal2.cpp)
> **Iteration Version2**: [binary-tree-preorder-traversal3](Binary-Tree/binary-tree-preorder-traversal/binary-tree-preorder-traversal3.cpp)
> Problem Link: [Chinese Version](https://leetcode.cn/problems/binary-tree-preorder-traversal/), [English Version](https://leetcode.com/problems/binary-tree-preorder-traversal/)

## binary-tree-inorder-traversal
> **Recursive** version: [binary-tree-inorder-traversal](Binary-Tree/binary-tree-inorder-traversal/binary-tree-inorder-traversal.cpp) </br>
> **Iteration Version1**: [binary-tree-inorder-traversal2](Binary-Tree/binary-tree-inorder-traversal/binary-tree-inorder-traversal2.cpp)
> **Iteration Version2**: [binary-tree-inorder-traversal3](Binary-Tree/binary-tree-inorder-traversal/binary-tree-inorder-traversal3.cpp)
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/), [English Version](https://leetcode.com/problems/binary-tree-inorder-traversal/)

## binary-tree-postorder-traversal
> **Recursive** version: [binary-tree-postorder-traversal](Binary-Tree/binary-tree-postorder-traversal/binary-tree-postorder-traversal.cpp) </br>
> **Iteration Version1**: [binary-tree-postorder-traversal2](Binary-Tree/binary-tree-postorder-traversal/binary-tree-postorder-traversal2.cpp)
> **Iteration Version2**: [binary-tree-postorder-traversal3](Binary-Tree/binary-tree-postorder-traversal/binary-tree-postorder-traversal3.cpp)
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/), [English Version](https://leetcode.com/problems/binary-tree-postorder-traversal/)

### Keys:
1. The recursive version is easy to understand. The difference between three kinds of orders is jsut the order of recursion. </br>
2. The **gist is iteration method 1:**
   1. We use a **stack** to store the **already-traversed** nodes since this is **DFS** rather than **BFS**. But whether **pushing the nodes to the result** depends on the order of travsersal.</br>
   2. The **preorder** is **root-left-right**, so we should push the **right** node first and then the **left** node. And the root node can be directly pushed to the result since it is already handled.</br>
   3. The **inorder** is quite different. Since the order is **left-root-right**, we traverse to root but it cannot be added to the result, rather, the left should be added to result before root. So, we first traverse to the left-most node, then begin to add the node to the result. </br>
   4. The **postorder** is similar to preorder. </br>
   5. From above, we can see that the three different traversal orders bring different styles of code. </br>
   6. However, in ***Iteration Version2***, all three traversal orders have similar and consistent styles. Here, we use the **null pointer markinig** method. We add a null pointer before the already-traversed nodes so that they should be added to the result.</br>
> 迭代法的核心难点就在于，如何判断这个节点是否已经遍历过了。用空指针标记法就可以很好的统一代码结构。

## binary-tree-level-order-traversal
> **Recursive** version: [binary-tree-level-order-traversal](Binary-Tree/binary-tree-level-order-traversal/binary-tree-level-order-traversal.cpp) </br>
> **Iteration Version**: [binary-tree-level-order-traversal2](Binary-Tree/binary-tree-level-order-traversal/binary-tree-level-order-traversal2.cpp)
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/), [English Version](https://leetcode.com/problems/binary-tree-level-order-traversal/)
> Related Problems: 
> 1.  [binary-tree-right-side-view](https://leetcode.cn/problems/binary-tree-right-side-view/) and [my version](Binary-Tree/binary-tree-level-order-Traversal/binary-tree-right-side-view.cpp)
> 2. [n-ary-tree-level-order-traversal](https://leetcode.cn/problems/n-ary-tree-level-order-traversal/) and [my version(using ***Null pointer mark method***)](Binary-Tree/binary-tree-level-order-Traversal/n-ary-tree-level-order-traversal.cpp)))

#### Keys:
1. Since levelorder traversal is **BFS**, we use **queue** to store the nodes traversed. </br>
2. In **recursive method**, we use an additional parameter **depth** to indicate the level of the node. </br>

## Invert Binary Tree
> My version: [invert-binary-tree](Binary-Tree/invert-binary-tree/invert-binary-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/invert-binary-tree/), [English Version](https://leetcode.com/problems/invert-binary-tree/)

#### Keys:
1. Use **recursion** or **iteration** to solve this problem. </br>
2. When using **recursion**, we should use *preorder* or *postorder* traversal to invert the tree. **Inorder** is not applicable since after inverting left and right child (traverse the mid point), the right child will be the original left child. </br>

## Symmetric Tree
> My version: [symmetric-tree](Binary-Tree/symmetric-tree/symmetric-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/symmetric-tree/), [English Version](https://leetcode.com/problems/symmetric-tree/)

#### Keys:
1. I use the **level order traversal** method to solve this problem. </br>
2. Every level, the nodes should be symmetric. So we use a stack to check the symmetry.</br>


## Maximum Depth of Binary Tree
> My version: [maximum-depth-of-binary-tree](Binary-Tree/maximum-depth-of-binary-tree/maximum-depth-of-binary-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/), [English Version](https://leetcode.com/problems/maximum-depth-of-binary-tree/)


## Minimum Depth of Binary Tree
> My version: [minimum-depth-of-binary-tree](Binary-Tree/minimum-depth-of-binary-tree/minimum-depth-of-binary-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/), [English Version](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

#### Keys:
1. The difference between **maximum depth** and **minimum depth** is illustrated in this graph. ![](Binary-Tree/minimum-depth-of-binary-tree/111.二叉树的最小深度.png) </br>

## Count Complete Tree Nodes
> My version: [count-complete-tree-nodes](Binary-Tree/count-complete-tree-nodes/count-complete-tree-nodes.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/count-complete-tree-nodes/), [English Version](https://leetcode.com/problems/count-complete-tree-nodes/)

#### Keys:
1. If using normal **recursion or iteration** method, the time complexity is $O(n)$ and these methods also apply to any normal binary tree. </br>
2. Utilizing the condition that this is a **complete binary tree**, we can use its property that once we know the depth of the complete binary tree, we get its node number. And if not, just deepening the recursion is ok to get $O(log^2_n)$ time complexity. </br>

## Balanced Binary Tree
> My first version: [balanced-binary-tree](Binary-Tree/balanced-binary-tree/balanced-binary-tree.cpp) </br>
> My second version: [balanced-binary-tree2](Binary-Tree/balanced-binary-tree/balanced-binary-tree2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/balanced-binary-tree/), [English Version](https://leetcode.com/problems/balanced-binary-tree/)

#### Keys:
1. In my **first version**, the time complexity is $O(n^2)$ since I use **recursion** from the **top to down** to solve this problem. That is, for every node traversed, I will **first** calculate whether **this node** is balanced, then consider its **left and right children**. So all the height below this node are calculated, leading to computability waste. </br>
2. In my **second** version, the time complexity is only $O(n)$ since I use **recursion** from the **bottom to top** to solve this problem. </br>

## binary-tree-paths
> My version: [binary-tree-paths](Binary-Tree/binary-tree-paths/binary-tree-paths.cpp) </br>
> Second version: [binary-tree-paths2](Binary-Tree/binary-tree-paths/binary-tree-paths2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/binary-tree-paths/), [English Version](https://leetcode.com/problems/binary-tree-paths/)

#### Keys:
1. How to manipulate and maintain the **already traversed path**? Use **pass by reference** or not? </br>
2. My version uses **pass a string vector by reference** and second version uses **pass a string by value**. But the essence is the same: leave the track with marks.</br>

## sum of left leaves
> My version: [sum-of-left-leaves](Binary-Tree/sum-of-left-leaves/sum-of-left-leaves.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/sum-of-left-leaves/), [English Version](https://leetcode.com/problems/sum-of-left-leaves/)

#### Keys:
1. The challenge lies on the definition of **left leaves**, which means this node is both a leaf and a left node of the parent.
2. Pay attention to the conditions of stopping the recursion: we know **this node's left child is a leaf**. So it is not the common case that the **null pointer** is stopping condition.

## Find Bottom Left Tree Value
> My version: [find-bottom-left-tree-value](Binary-Tree/find-bottom-left-tree-value/find-bottom-left-tree-value.cpp) </br>
> Version2: [find-bottom-left-tree-value2](Binary-Tree/find-bottom-left-tree-value/find-bottom-left-tree-value2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/find-bottom-left-tree-value/), [English Version](https://leetcode.com/problems/find-bottom-left-tree-value/)

#### Keys:
1. The most intuitive way is to use **level order traversal** to find the leftmost node of the last level. And this is the version 1.</br>
2. The second version is to use **recursion**. The key point is to **record the depth** of the current node. If the depth is larger than the maximum depth, then update the maximum depth and the leftmost node value. </br>

## path-sum
> My version: [path-sum](Binary-Tree/path-sum/path-sum.cpp) </br>
> problem Link: [Chinese Version](https://leetcode-cn.com/problems/path-sum/), [English Version](https://leetcode.com/problems/path-sum/)

#### Keys:
1. typical recursion problem. </br>

## path-sum-ii
> My version: [path-sum-ii](Binary-Tree/path-sum-ii/path-sum-ii.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/path-sum-ii/), [English Version](https://leetcode.com/problems/path-sum-ii/)

#### Keys:
1. The difference between this problem and the previous one is that this problem requires to return all the paths that sum to a given value. So we have to search for the **whole tree**, which means the recursion function should have no return.</br>
2. Use **backtracking** to remove the last element in the path vector after the recursion. And **use pass by reference**.</br>

## construct-binary-tree-from-inorder-and-postorder-traversal
> My version: [construct-binary-tree-from-inorder-and-postorder-traversal](Binary-Tree/construct-binary-tree-from-inorder-and-postorder-traversal/construct-binary-tree-from-inorder-and-postorder-traversal.cpp) </br>
> Second version: [construct-binary-tree-from-inorder-and-postorder-traversal2](Binary-Tree/construct-binary-tree-from-inorder-and-postorder-traversal/construct-binary-tree-from-inorder-and-postorder-traversal2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/), [English Version](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

#### Keys:
1. The key point is to find the **pivot node** in the **postorder traversal**. The pivot node in the **inorder** array can divide the array into left child tree and right child tree. </br>
2. My version does not use the **unordered_map** to store the index of the inorder array. So the searching process has time complexity $O(n)$. What's more, I define two new vectors every recursion which is costly. The optimized one is the second version. </br>
3. The second version defines a **map** to store the index of the inorder array. So the searching process has time complexity $O(1)$. And the recursion function uses the **range of the inorder and postorder reference** to avoid defining new vectors. </br>

## construct-binary-tree-from-preorder-and-postorder-traversal
> My version: [construct-binary-tree-from-preorder-and-postorder-traversal](Binary-Tree/construct-binary-tree-from-preorder-and-postorder-traversal/construct-binary-tree-from-preorder-and-postorder-traversal.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/), [English Version](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)

#### Keys:
1. From these two problems above, we can get the key to these constructing problems: **find the pivot node**, which means finding the decision boundary of left and right child tree. </br>

## maximum-binary-tree
> My version: [maximum-binary-tree](Binary-Tree/maximum-binary-tree/maximum-binary-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/maximum-binary-tree/), [English Version](https://leetcode.com/problems/maximum-binary-tree/)

#### Keys:
1. Similar to the construction of binary tree above, we can find the **pivot node** by finding the **maximum value** in the array. </br>

## merge-two-binary-trees
> My version: [merge-two-binary-trees](Binary-Tree/merge-two-binary-trees/merge-two-binary-trees.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/merge-two-binary-trees/), [English Version](https://leetcode.com/problems/merge-two-binary-trees/)

#### Keys:
1. How to handle two trees at the same time? No difference. Just need to process two roots in one recursion. </br>

## search-in-a-binary-search-tree
> My version: [search-in-a-binary-search-tree](Binary-Tree/search-in-a-binary-search-tree/search-in-a-binary-search-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/search-in-a-binary-search-tree/), [English Version](https://leetcode.com/problems/search-in-a-binary-search-tree/)

#### Keys:
1. This is the most basic problem to get familiar with the characteristics of binary search tree. </br> 

## validate-binary-search-tree
> My version: [validate-binary-search-tree](Binary-Tree/validate-binary-search-tree/validate-binary-search-tree.cpp) </br>
> second version: [validate-binary-search-tree2](Binary-Tree/validate-binary-search-tree/validate-binary-search-tree2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/validate-binary-search-tree/), [English Version](https://leetcode.com/problems/validate-binary-search-tree/)

#### Keys:
1. In my first version, I use **from bottom to top** to check the validity of the tree. If the **left and right children are both valid**, then I use the **BST property** to check whether the **left child's max node is smaller than the current**, and so as the right child. So, this is **postorder** traversal. But this induces **some repetition** when finding the max and min node. </br>
2. Version two handles the reprtition problem. It checks whether the current node's value is in the boundary, and then goes to the left and right child by narrowing the boundary. This is **preorder** traversal.</br>

## minimum-absolute-difference-in-bst
> My version: [minimum-absolute-difference-in-bst](Binary-Tree/minimum-absolute-difference-in-bst/minimum-absolute-difference-in-bst.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/), [English Version](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

#### Keys:
1. The naive and my first version is to use **inorder traversal** to get the sorted array, and then calculate the minimum difference. </br>
2. The second version maintains a **previous node value** to calculate the minimum difference. So there is no need to allocate another $O(n)$ vector to record all the nodes. </br>

## find-mode-in-binary-search-tree
> My version: [find-mode-in-binary-search-tree](Binary-Tree/find-mode-in-binary-search-tree/find-mode-in-binary-search-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/), [English Version](https://leetcode.com/problems/find-mode-in-binary-search-tree/)

#### Keys:
1. Use **inorder traversal** to get the sorted array, and then store a global maximum frequency to help get the mode during the traversal process. </br>

## lowest-common-ancestor-of-a-binary-tree
> My version: [lowest-common-ancestor-of-a-binary-tree](Binary-Tree/lowest-common-ancestor-of-a-binary-tree/lowest-common-ancestor-of-a-binary-tree.cpp) </br>
> Second version: [lowest-common-ancestor-of-a-binary-tree2](Binary-Tree/lowest-common-ancestor-of-a-binary-tree/lowest-common-ancestor-of-a-binary-tree2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/), [English Version](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

#### Keys:
1. The two versions are actually the same, but the second version is more concise. </br>
2. Both use the thought of **from the bottom to the top**. If the current node is the **lowest common ancestor**, then it must satisfy that **the left and right child are both marked by the program**. </br>

## lowest-common-ancestor-of-a-binary-search-tree
> My version: [lowest-common-ancestor-of-a-binary-search-tree](Binary-Tree/lowest-common-ancestor-of-a-binary-search-tree/lowest-common-ancestor-of-a-binary-search-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/), [English Version](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

#### Keys:
1. The thought is the same as the previous problem. But this time, we can use the **BST property** to help us find the lowest common ancestor. </br>

## insert-into-a-binary-search-tree
> My version: [insert-into-a-binary-search-tree](Binary-Tree/insert-into-a-binary-search-tree/insert-into-a-binary-search-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/), [English Version](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

#### Keys:
1. This problem is just simulating the process of searching the node in the BST. If the node is not found, then we can insert the node at the leaf. </br>

## delete-node-in-a-bst
> My version: [delete-node-in-a-bst](Binary-Tree/delete-node-in-a-bst/delete-node-in-a-bst.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/delete-node-in-a-bst/), [English Version](https://leetcode.com/problems/delete-node-in-a-bst/)

#### Keys:
1. This problem requires us to consider different cases. But the thought is naive. So, taking every case into consideration is ok. </br>

## trim-a-binary-search-tree
> My version: [trim-a-binary-search-tree](Binary-Tree/trim-a-binary-search-tree/trim-a-binary-search-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/trim-a-binary-search-tree/), [English Version](https://leetcode.com/problems/trim-a-binary-search-tree/)

#### Keys:
1. To solve this problem, you have to understand the **recursion function with TreeNode as the return value**. This thought also applies to the [delete BST](#delete-node-in-a-bst) and [insert BST](#insert-into-a-binary-search-tree), where I use the iteration method instead.</br>

## convert-sorted-array-to-binary-search-tree
> My version: [convert-sorted-array-to-binary-search-tree](Binary-Tree/convert-sorted-array-to-binary-search-tree/convert-sorted-array-to-binary-search-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/), [English Version](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

#### Keys:
1. With the keys in [trim BST](#trim-a-binary-search-tree), we can solve this problem. </br>

## convert-bst-to-greater-tree
> My version: [convert-bst-to-greater-tree](Binary-Tree/convert-bst-to-greater-tree/convert-bst-to-greater-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/convert-bst-to-greater-tree/), [English Version](https://leetcode.com/problems/convert-bst-to-greater-tree/)

#### Keys:
1. Use **reverse inorder traversal** to solve this problem. </br>