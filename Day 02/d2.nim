import strutils, sequtils, sugar

var
  directions = readFile("input.txt")
    .strip()
    .splitLines()
    .map(line => (var lineSplit = line.split();
                 (lineSplit[0], parseInt(lineSplit[1]))))
  posx = 0
  depth = 0
  depth2 = 0
  aim = 0

for (d, x) in directions:
  case d:
    of "up":
      depth -= x
      aim -= x
    of "down":
      depth += x
      aim += x
    of "forward":
      posx += x
      depth2 += aim * x

echo abs(posx*depth)
echo abs(posx*depth2)
