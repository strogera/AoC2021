import strutils
import sequtils

var nums = map(readFile("input.txt").strip().splitLines(), parseInt)

var count1 = 0
var count2 = 0
for x in 0..len(nums):
  if x + 1 < len(nums) and nums[x] < nums[x+1]:
    count1 += 1
  if x + 3 < len(nums) and nums[x] < nums[x+3]:
    count2 += 1
echo(count1)
echo(count2)
