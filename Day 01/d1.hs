import System.IO

toInt :: String -> Int
toInt x = read x 

getNext :: [Int] -> Int -> Int
getNext l i = if length l > i
                   then l!!i else 0

countIncr :: [Int] -> Int -> Int
countIncr [] next = 0
countIncr (h:t) next = countIncr t next + (if h < getNext t next
                                             then 1 else 0)
                                
main = do
        file <- openFile "input.txt" ReadMode
        content <- hGetContents file
        let nums = lines content
        let list = map toInt nums
        print(countIncr list 0)
        print(countIncr list 2)
        hClose file


