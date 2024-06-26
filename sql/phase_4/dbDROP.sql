SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS FavoriteList;
DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS Auction;
DROP TABLE IF EXISTS Bid;
DROP TABLE IF EXISTS Message;
DROP TABLE IF EXISTS Transaction;
DROP TABLE IF EXISTS Review;
DROP TABLE IF EXISTS Shipping;
DROP TRIGGER IF EXISTS SetAuctionPostDate;
DROP PROCEDURE IF EXISTS GetHighestBid;
DROP VIEW IF EXISTS AuctionDetails;
SET FOREIGN_KEY_CHECKS = 1;