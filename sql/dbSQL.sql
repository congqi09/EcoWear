-- 1. List all items along with their category names
SELECT I.itemId, I.title, I.description, C.name AS categoryName
FROM Item I
JOIN Category C ON I.categoryId = C.categoryId;
/* 
The expected output would be the Columns: itemId, title, description, categoryName
*/

-- 2. List the top 3 most active sellers based on the number of items listed for auction
SELECT U.username, COUNT(A.itemId) AS totalItemsListed
FROM Auction A JOIN User U ON A.sellerId = U.userId
GROUP BY U.username
ORDER BY totalItemsListed DESC
LIMIT 3;
/* 
The expected output would be the Columns: username, totalItemsListed
*/

-- 3. List items that have never been part of an auction (using a subquery)
SELECT I.itemId, I.title
FROM Item I
WHERE I.itemId NOT IN (
    SELECT DISTINCT A.itemId
    FROM Auction A
);
/* 
The expected output would be the Columns: itemId, title
*/

-- 4. Rank seller's selling amount, whose selling amount extend 100
SELECT U.username AS sellerName, SUM(T.amount) AS totalSales
FROM Transaction T
JOIN User U ON T.sellerId = U.userId
GROUP BY U.username
HAVING SUM(T.amount) > 100
ORDER BY totalSales DESC;
/* 
The expected output would be the Columns: sellerName, totalSales
*/

-- 5. List all item's average bidAmount, which has at least 3 bidAmount. 
SELECT A.itemId, AVG(B.bidAmount) AS averageBid
FROM Bid B
JOIN Auction A ON B.auctionId = A.auctionId
GROUP BY A.itemId
HAVING COUNT(B.bidId) >= 3
ORDER BY averageBid DESC;
/* 
The expected output would be the Columns: itemId, averageBid
*/

-- 6. Show the current highest bid and bidder details for an item I (UserID 6685, Ryan) am selling using a subquery to find the maximum bid amount.
SELECT B.bidderID, U.userName, B.bidAmount
FROM Bid B
JOIN Auction A ON B.auctionID = A.auctionID
JOIN User U ON B.bidderID = U.userID
WHERE A.sellerID = 6685 AND B.bidAmount = (
    SELECT MAX(bidAmount)
    FROM Bid
    WHERE auctionID = A.auctionID
);
/* 
The expected output would be the Columns: bidderID, userName, and bidAmount for the highest bid on the item. 
*/

-- 7. Generate a shipping label for an item I (UserID 1763) have sold.
SELECT T.transactionID, S.*
FROM Transaction T
JOIN Shipping S ON T.transactionID = S.transactionID
WHERE T.sellerID = 1763;
/* 
The expected output would be the Columns: transactionID and all columns from the Shipping table for transactions where the current user is the seller.
*/


