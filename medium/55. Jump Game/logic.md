- Initialize a goal post at last index
- Now iterate from behind and check if we can reach goal index by i + nums[i] >= goal
- if this is true we keep shifting goal by i
- Now return True is goal is at the first index else False