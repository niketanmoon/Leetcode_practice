- First put the finish spot as 1 and then start calculating from reverse
- This way we know that the last row is all 1. We also know that last column is all 1
- Then we compute the paths to a particular box as right + down
- Once its done we can return row[0]
- Look at the video for better understanding