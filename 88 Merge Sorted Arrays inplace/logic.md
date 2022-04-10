- nums1 = [1, 2, 3, 0, 0, 0], m= 3 nums2 = [2, 5, 6] n= 3
- Start filling from the last index of the nums1
- Now compare if the nums1 last element > nums2 last element and whichever is greater put it inside nums1 last_index
- last_index = m + n - 1
- It may happen that the nums2 does not become iterate fully and nums1 does in that case copy all the elements from nums2 to nums1
 