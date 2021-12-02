import System.IO

fromStringToTuple :: String -> (Char, Int)
fromStringToTuple str = (head str , getValue str)

getValue :: String -> Int
getValue str = read $ cutDirection str

cutDirection :: String -> String
cutDirection (h:t)
        | h == ' ' = t
        | otherwise = cutDirection t

compute :: [(Char, Int)] -> (Int, Int, Int, Int) -- (posx, depth, depth2, aim)
compute [] = (0, 0, 0, 0)
compute ((d, v):t)
  | d == 'f' = (posx + v, depth, depth2 + (aim*v), aim)
  | d == 'u' = (posx, depth - v, depth2, aim - v)
  | d == 'd' = (posx, depth + v, depth2, aim + v)
  where (posx, depth, depth2, aim) = compute t

solvePart1 :: [String] -> Int
solvePart1 l = posx * depth
        where (posx, depth, _, _) = compute $ fromStringToTuple <$> l

solvePart2 :: [String] -> Int
solvePart2 l = posx * depth
        where (posx, _, depth, _) = compute $ reverse $ fromStringToTuple <$> l

main = do
        input <- lines <$> readFile "input.txt"
        print $ solvePart1 input
        print $ solvePart2 input
