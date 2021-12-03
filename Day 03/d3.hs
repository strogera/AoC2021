import System.IO

main = do
        input <- lines <$> readFile "input.txt"
        print $ solvePart1 input
        print $ solvePart2 input

solvePart1 :: [String] -> Int
solvePart1 x = gamma x * epsilon x
  where 
    mcommon = mostCommon
    gamma = toInt . mcommon 
    epsilon = toInt .flipBits . mcommon 


toInt :: [Char] -> Int
toInt [] = 0
toInt ('0':xs) = toInt xs
toInt ('1':xs) = (2 ^ length xs) + toInt xs

flipBits :: [Char] -> [Char]
flipBits [] = ""
flipBits ('0':xs) = ('1':flipBits xs)
flipBits ('1':xs) = ('0':flipBits xs)


mostCommon :: [String] -> String
mostCommon [] = ""
mostCommon l = map (\x -> if x > (length l - x) then '1' else '0') (countOnes l)


countOnes :: [String] -> [Int]
countOnes [] = []
countOnes ([]:xs) = countOnes xs
countOnes l = length ( filter (=='1') $ head <$> l) : countOnes (tail <$>  l)

solvePart2 :: [String] -> Int
solvePart2 l = toInt generatorRating * toInt grubberRating
  where 
    (generatorRating, grubberRating) = rating l

rating:: [String] -> (String, String)
rating x 
  | length x == 1 = (head x , head x)
  | otherwise =
    if onecount >= (length x - onecount) then
       ('1':fst (rating (tail <$> filter (\x -> head x == '1') x)), 
       '0':snd (rating (tail <$> filter (\x -> head x == '0') x)))
    else
       ('0':fst (rating (tail <$> filter (\x -> head x == '0') x)),
       '1':snd (rating (tail <$> filter (\x -> head x == '1') x)))
    where
      onecount = head $ countOnes x 
