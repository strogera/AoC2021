import System.IO
import Data.List

main = do
  (x:xs) <- lines <$> readFile "./input.txt"
  let scores = getAllWinningScores ( parseBoards xs []) (read $ "[" ++ x ++ "]")
  print $  head scores
  print $  last scores

parseBoards :: [String] -> [[Int]] -> [[[Int]]]
parseBoards [] p = [p]
parseBoards ("":xs) [] = parseBoards xs []
parseBoards ("":xs) curBoards = curBoards : parseBoards xs []
parseBoards (x:xs) curBoards = parseBoards xs (curBoards ++ [map ( read::String -> Int) (words x)])

getAllWinningScores :: [[[Int]]] -> [Int] -> [Int]
getAllWinningScores [] _ = []
getAllWinningScores _ [] = []
getAllWinningScores b (n:ns) = map score winning ++ getAllWinningScores rest ns
  where
    marked = mark n b
    winning = filter isWinning marked
    rest = filter (not . isWinning) marked
    score board = n * sum(filter (/= -1) (concat board)) 

mark :: Int -> [[[Int]]] -> [[[Int]]]
mark _ [] = []
mark n (x:xs) = map (map (\x -> if x == n then -1 else x)) x : mark n xs

isWinning :: [[Int]] -> Bool
isWinning [] = False
isWinning b = any ((==True) . winningRow) b || any ((==True) . winningRow) (transpose b)
  where winningRow  = all (==(-1))

