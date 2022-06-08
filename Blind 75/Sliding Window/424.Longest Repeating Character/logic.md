**TC: O(26n) SC: O(n)**
- Initialize left = 0
- now for right go through the loop and check if window length - maxFreq count is <=k or not
- if not then increment l and decrement the maxfreq count
**TC:O(n) SC:O(n)**
- We maintain a maxFrequency variable which keeps track of the max frequency
- Then instead of checking max in count hashmap everytime we just have to use max frequency