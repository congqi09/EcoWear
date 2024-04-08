-- Populate User table
INSERT INTO User VALUES (3622, 'kthornton', 'Stephanie', 'Wright', 'maria69@olson-cohen.com', '!WW!DkYhn1', '1811 Dickson Mission Rodriguezville, KY 13079', '0824313413', 'https://placekitten.com/24/748', 'admin', 4.20, '2023-01-15', '2024-02-01');
INSERT INTO User VALUES (6460, 'josephmartin', 'Kaylee', 'Jimenez', 'caitlin30@gmail.com', 'X#PBZIrt&1', '916 Swanson Rue Apt. 660 Daniellemouth, MO 11307', '233-830-4587', 'https://placekitten.com/402/763', 'admin', 4.25, '2019-04-29', '2023-05-02');
INSERT INTO User VALUES (6685, 'fmason', 'Ryan', 'Perez', 'deborahpotts@collins.biz', 't!5R(je#1L', '03526 Jason Tunnel West Christopher, IA 88896', '+1-147-232-7069', 'https://placeimg.com/738/712/any', 'user', 3.79, '2022-11-11', '2023-10-15');
INSERT INTO User VALUES (1989, 'taylormichael', 'Randall', 'Lloyd', 'sullivanwilliam@parker.org', '&y$VUkB81d', '05218 Martin Circle Port Edwardside, NY 50972', '+1-781-667-8135', 'https://placekitten.com/607/984', 'user', 3.86, '2021-12-17', '2023-07-08');
INSERT INTO User VALUES (1762, 'mason70', 'Brenda', 'Bailey', 'brent11@hotmail.com', 'K%1O4rPDW)', '3792 Trujillo Rest Suite 375 North Rebeccaside, NY 48822', '1-555-622-7282', 'https://placekitten.com/300/300', 'user', 4.57, '2020-03-24', '2023-12-01');
INSERT INTO User VALUES (9138, 'charles55', 'Jessica', 'Murray', 'daniel82@yahoo.com', '2V)1XAcb7m', '508 Gregory Row Robinsonmouth, NE 46652', '2482461947', 'https://dummyimage.com/30x949', 'user', 3.76, '2022-02-01', '2023-04-24');
INSERT INTO User VALUES (3919, 'davidhoover', 'Anne', 'Jones', 'newmanjennifer@gmail.com', 'iA9TCQOap@', 'USS Ellis FPO AA 74858', '(662)153-7477', 'https://www.lorempixel.com/235/421', 'user', 3.24, '2022-10-05', '2023-08-15');
INSERT INTO User VALUES (803, 'qramirez', 'Jose', 'Perkins', 'bwilliams@yahoo.com', '(#7eXzIUek', 'Unit 9449 Box 1711 DPO AP 73499', '895.046.0998', 'https://placekitten.com/1002/555', 'user', 3.55, '2022-06-29', '2023-11-20');
INSERT INTO User VALUES (2000, 'solisrobert', 'Michael', 'Rodriguez', 'michele92@compton.com', '6%N3XlaktK', 'Unit 9284 Box 9883 DPO AA 82328', '007.332.3321', 'https://www.lorempixel.com/691/327', 'user', 4.11, '2019-10-17', '2024-01-12');
INSERT INTO User VALUES (1005, 'andersonjames', 'Sabrina', 'Mcclure', 'hudsonamber@hotmail.com', '*3GQRuaeQT', '349 Tabitha Square Apt. 812 Vegashire, FL 36374', '694-280-8629', 'https://placeimg.com/60/99/any', 'user', 4.98, '2023-11-24', '2023-07-09');
INSERT INTO User VALUES (5001, 'emilyr', 'Emily', 'Robinson', 'emilyr@example.com', 'p@ssW0rd!', '1234 Elm Street, Springfield, IL 62704', '555-123-4567', 'https://placekitten.com/200/300', 'user', 4.5, '2021-08-15', '2024-02-28');

-- Populate Category table
INSERT INTO Category VALUES (1, 'T-Shirts');
INSERT INTO Category VALUES (2, 'Dresses');
INSERT INTO Category VALUES (3, 'Jeans');
INSERT INTO Category VALUES (4, 'Jackets');
INSERT INTO Category VALUES (5, 'Sweaters');
INSERT INTO Category VALUES (6, 'Shoes');
INSERT INTO Category VALUES (7, 'Accessories');



-- Populate Item table
INSERT INTO Item VALUES (1, 'Vintage Rock Band T-Shirt', 'A well-loved vintage t-shirt featuring a classic rock band.', 1, 'M', 'Vintage', 'Used', '/images/item1.jpg');
INSERT INTO Item VALUES (2, 'Floral Summer Dress', 'A light and airy summer dress with a floral pattern.', 2, 'L', 'H&M', 'Like New', '/images/item2.jpg');
INSERT INTO Item VALUES (3, 'High-Waisted Denim Jeans', 'Trendy high-waisted denim jeans in excellent condition.', 3, '30', 'Levi\'s', 'Excellent', '/images/item3.jpg');
INSERT INTO Item VALUES (4, 'Leather Biker Jacket', 'Genuine leather biker jacket with a vintage feel.', 4, 'XL', 'Vintage', 'Good', '/images/item4.jpg');
INSERT INTO Item VALUES (5, 'Cozy Wool Sweater', 'A cozy wool sweater perfect for cold weather.', 5, 'M', 'Woolrich', 'Very Good', '/images/item5.jpg');
INSERT INTO Item VALUES (6, 'Running Shoes', 'Lightweight and comfortable running shoes.', 6, '9', 'Nike', 'Used', '/images/item6.jpg');
INSERT INTO Item VALUES (7, 'Leather Wallet', 'A compact leather wallet with multiple compartments.', 7, 'One Size', 'Coach', 'New', '/images/item7.jpg');
INSERT INTO Item VALUES (8, 'Stylish Fedora Hat', 'A stylish fedora hat, perfect for any occasion.', 7, 'One Size', 'Generic', 'New', '/images/item8.jpg');
INSERT INTO Item VALUES (9, 'Elegant Watch', 'An elegant watch suitable for every occasion.', 7, 'One Size', 'Seiko', 'New', '/images/item9.jpg');
INSERT INTO Item VALUES (10, 'Classic Leather Boots', 'Durable and stylish classic leather boots.', 6, '10', 'Timberland', 'New', '/images/item10.jpg');



-- Populate FavoriteList table
INSERT INTO FavoriteList VALUES (3622, 7);
INSERT INTO FavoriteList VALUES (6460, 3);
INSERT INTO FavoriteList VALUES (6685, 5);
INSERT INTO FavoriteList VALUES (1989, 6);
INSERT INTO FavoriteList VALUES (1762, 8);
INSERT INTO FavoriteList VALUES (9138, 1);
INSERT INTO FavoriteList VALUES (3919, 2);
INSERT INTO FavoriteList VALUES (803, 4);
INSERT INTO FavoriteList VALUES (2000, 3);
INSERT INTO FavoriteList VALUES (1005, 2);


-- Populate Auction table
INSERT INTO Auction (auctionId, itemId, sellerId, status, startPrice, currentBid, buyNowPrice, endDate) VALUES (1, 1, 3622, 'closed', 10.00, 15.00, 25.00, '2024-03-15');
INSERT INTO Auction (auctionId, itemId, sellerId, status, startPrice, currentBid, buyNowPrice, endDate) VALUES (2, 2, 6460, 'closed', 20.00, 40.00, 50.00, '2024-03-20');
INSERT INTO Auction (auctionId, itemId, sellerId, status, startPrice, currentBid, buyNowPrice, endDate) VALUES (3, 3, 6685, 'active', 15.00, 22.50, 40.00, '2024-03-25');
INSERT INTO Auction (auctionId, itemId, sellerId, status, startPrice, currentBid, buyNowPrice, endDate) VALUES (4, 4, 1989, 'active', 50.00, 55.00, 80.00, '2024-03-30');
INSERT INTO Auction (auctionId, itemId, sellerId, status, startPrice, currentBid, buyNowPrice, endDate) VALUES (5, 5, 1762, 'closed', 25.00, 35.00, 60.00, '2024-04-04');
INSERT INTO Auction (auctionId, itemId, sellerId, status, startPrice, currentBid, buyNowPrice, endDate) VALUES (6, 6, 9138, 'active', 30.00, 45.00, 70.00, '2024-04-09');
INSERT INTO Auction (auctionId, itemId, sellerId, status, startPrice, currentBid, buyNowPrice, endDate) VALUES (7, 7, 3919, 'active', 5.00, 10.00, 15.00, '2024-04-14');
INSERT INTO Auction (auctionId, itemId, sellerId, status, startPrice, currentBid, buyNowPrice, endDate) VALUES (8, 8, 5001, 'active', 10.00, 200.00, 300.00, '2024-04-20');


-- Bid entries
INSERT INTO Bid (bidId, auctionId, bidderId, bidAmount, bidTime) VALUES (1, 1, 803, 15.00, '2024-03-05');
INSERT INTO Bid (bidId, auctionId, bidderId, bidAmount, bidTime) VALUES (2, 2, 2000, 30.00, '2024-03-10');
INSERT INTO Bid (bidId, auctionId, bidderId, bidAmount, bidTime) VALUES (3, 3, 1005, 22.50, '2024-03-15');
INSERT INTO Bid (bidId, auctionId, bidderId, bidAmount, bidTime) VALUES (4, 4, 3622, 55.00, '2024-03-20');
INSERT INTO Bid (bidId, auctionId, bidderId, bidAmount, bidTime) VALUES (6, 6, 6685, 45.00, '2024-03-30');
INSERT INTO Bid (bidId, auctionId, bidderId, bidAmount, bidTime) VALUES (7, 7, 1989, 10.00, '2024-04-02');
-- Additional bids to simulate competition and interest
INSERT INTO Bid (bidId, auctionId, bidderId, bidAmount, bidTime) VALUES (8, 4, 1762, 60.00, '2024-03-06');
INSERT INTO Bid (bidId, auctionId, bidderId, bidAmount, bidTime) VALUES (9, 2, 9138, 35.00, '2024-03-11');
INSERT INTO Bid (bidId, auctionId, bidderId, bidAmount, bidTime) VALUES (10, 3, 3919, 25.00, '2024-03-16');
INSERT INTO Bid (bidId, auctionId, bidderId, bidAmount, bidTime) VALUES (11, 2, 3919, 36.00, '2024-03-12');
INSERT INTO Bid (bidId, auctionId, bidderId, bidAmount, bidTime) VALUES (12, 2, 803, 37.00, '2024-03-13');
INSERT INTO Bid (bidId, auctionId, bidderId, bidAmount, bidTime) VALUES (13, 2, 2000, 38.00, '2024-03-14');
INSERT INTO Bid (bidId, auctionId, bidderId, bidAmount, bidTime) VALUES (14, 2, 1005, 40.00, '2024-03-15');
INSERT INTO Bid (bidId, auctionId, bidderId, bidAmount, bidTime) VALUES (15, 8, 1989, 200.00, '2024-04-05');
-- To simulate the auction closing and proceeding to a transaction, we'll close the auction.
UPDATE Auction SET status = 'closed' WHERE auctionId = 3;
UPDATE Auction SET status = 'closed' WHERE auctionId = 4;
UPDATE Auction SET status = 'closed' WHERE auctionId = 6;
UPDATE Auction SET status = 'closed' WHERE auctionId = 8;



-- Message entries
INSERT INTO Message (messageId, senderId, receiverId, itemId, content, timeSent) VALUES (1, 3622, 6460, 1, 'Is this t-shirt still available?', '2024-03-01');
INSERT INTO Message (messageId, senderId, receiverId, itemId, content, timeSent) VALUES (2, 6460, 3622, 1, 'Yes, it is still available.', '2024-03-01');
INSERT INTO Message (messageId, senderId, receiverId, itemId, content, timeSent) VALUES (3, 1989, 6685, 3, 'Can you provide more details about the jeans condition?', '2024-03-02');
INSERT INTO Message (messageId, senderId, receiverId, itemId, content, timeSent) VALUES (4, 6685, 1989, 3, 'Sure, they are in excellent condition with no signs of wear.', '2024-03-02');
INSERT INTO Message (messageId, senderId, receiverId, itemId, content, timeSent) VALUES (5, 803, 1762, 6, 'Do the shoes fit true to size?', '2024-03-03');
INSERT INTO Message (messageId, senderId, receiverId, itemId, content, timeSent) VALUES (6, 1762, 803, 6, 'Yes, they fit true to size.', '2024-03-03');
INSERT INTO Message (messageId, senderId, receiverId, itemId, content, timeSent) VALUES (7, 9138, 3919, 7, 'Is the wallet still up for sale?', '2024-03-04');
INSERT INTO Message (messageId, senderId, receiverId, itemId, content, timeSent) VALUES (8, 3919, 9138, 7, 'Yes, the wallet is still available.', '2024-03-04');


-- Populate Transaction table
INSERT INTO Transaction (transactionId, transactionDate, amount, itemId, buyerId, sellerId, type) VALUES (1, '2024-03-15', 15.00, 1, 803, 3622, 'online');
INSERT INTO Transaction (transactionId, transactionDate, amount, itemId, buyerId, sellerId, type) VALUES (2, '2024-04-04', 60.00, 5, 2000, 1763, 'offline');
INSERT INTO Transaction (transactionId, transactionDate, amount, itemId, buyerId, sellerId, type) VALUES (3, '2024-03-20', 40.00, 2, 1005, 6460, 'online');
INSERT INTO Transaction (transactionId, transactionDate, amount, itemId, buyerId, sellerId, type) VALUES (4, '2024-04-21', 200.00, 8, 1989, 5001, 'online');
INSERT INTO Transaction (transactionId, transactionDate, amount, itemId, buyerId, sellerId, type) VALUES (5, '2024-04-23', 30.00, 3, 9138, 3919, 'online');
INSERT INTO Transaction (transactionId, transactionDate, amount, itemId, buyerId, sellerId, type) VALUES (6, '2024-04-24', 66.00, 4, 1005, 2000, 'online');
INSERT INTO Transaction (transactionId, transactionDate, amount, itemId, buyerId, sellerId, type) VALUES (7, '2024-04-25', 76.00, 6, 1005, 1763, 'online');

-- Populate Shipping table
INSERT INTO Shipping (shippingId, transactionId, trackingNumber, shippingDate, estimatedDelivery) VALUES (1, 1, 'TRACK123A', '2024-03-16', '2024-03-20');
INSERT INTO Shipping (shippingId, transactionId, trackingNumber, shippingDate, estimatedDelivery) VALUES (2, 2, 'TRACK123E', '2024-04-04', '2024-04-06');
INSERT INTO Shipping (shippingId, transactionId, trackingNumber, shippingDate, estimatedDelivery) VALUES (3, 3, 'TRACK123F', '2024-03-23', '2024-03-27');
INSERT INTO Shipping (shippingId, transactionId, trackingNumber, shippingDate, estimatedDelivery) VALUES (4, 4, 'TRACK124B', '2024-04-22', '2024-04-25');
INSERT INTO Shipping (shippingId, transactionId, trackingNumber, shippingDate, estimatedDelivery) VALUES (5, 5, 'TRACK125B', '2024-04-25', '2024-04-27');
INSERT INTO Shipping (shippingId, transactionId, trackingNumber, shippingDate, estimatedDelivery) VALUES (6, 6, 'TRACK126B', '2024-04-26', '2024-04-28');
INSERT INTO Shipping (shippingId, transactionId, trackingNumber, shippingDate, estimatedDelivery) VALUES (7, 7, 'TRACK125B', '2024-04-27', '2024-04-30');


-- Populate Review table
INSERT INTO Review (reviewId, UserId, transactionId, rating, comment, reviewDate) VALUES (1, 803, 1, 5, 'Excellent quality and fast shipping!', '2024-03-22');
INSERT INTO Review (reviewId, UserId, transactionId, rating, comment, reviewDate) VALUES (2, 2000, 2, 4, 'Item as described, but delivery was delayed.', '2024-04-10');
INSERT INTO Review (reviewId, UserId, transactionId, rating, comment, reviewDate) VALUES (3, 1005, 3, 5, 'The dress was even better than described, and the delivery was prompt. Highly recommend!', '2024-03-28');
INSERT INTO Review (reviewId, UserId, transactionId, rating, comment, reviewDate) VALUES (4, 1989, 4, 5, 'The hat is even more stylish in person, and the shipping was incredibly fast!', '2024-04-26');
INSERT INTO Review (reviewId, UserId, transactionId, rating, comment, reviewDate) VALUES (5, 9138, 5, 5,'Very fast diliveried! Good packaging. Thanks!','2024-04-27');
INSERT INTO Review (reviewId, UserId, transactionId, rating, comment, reviewDate) VALUES (6, 1005, 6, 5,'Very Good packaging. ','2024-04-29');
INSERT INTO Review (reviewId, UserId, transactionId, rating, comment, reviewDate) VALUES (7, 1005, 7, 2,'Very good diliveried! but bad packaging. ','2024-05-01');