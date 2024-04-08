CREATE TABLE User (
	userId			INT				NOT NULL,
	username		VARCHAR(33)		NOT NULL,
	firstName		VARCHAR(33),
	lastName		VARCHAR(33),
	email 			VARCHAR(33),
	password		VARCHAR(33)		NOT NULL,
	address			VARCHAR(99),
	phone	  		VARCHAR(15),
	profilePicture	VARCHAR(255),
	userGroup		ENUM('admin', 'user'),
	userRating		DECIMAL(10,2),
	registerDate	DATE,
	lastLoginDate	DATE,
	PRIMARY KEY (userId)
);

CREATE TABLE Category (
	categoryId		INT				NOT NULL,
	name			VARCHAR(33)
);

CREATE TABLE Item (
	itemId 		INT AUTO_INCREMENT	NOT NULL,
	title 			VARCHAR(33)		NOT NULL,
	description		VARCHAR(255),
	categoryId		INT,
	size			VARCHAR(33),
	brand			VARCHAR(33),
	itemCondition	VARCHAR(15),
	image			VARCHAR(255),
	PRIMARY KEY (itemId)
);

CREATE TABLE FavoriteList (
	userId			INT				NOT NULL,
	itemId			INT				NOT NULL
);

CREATE TABLE Auction (
	auctionId		INT				NOT NULL,
	itemId			INT				NOT NULL,
	sellerId		INT				NOT NULL,
	buyerId			INT,
	status			VARCHAR(15)		NOT NULL,
	startPrice		DECIMAL(10,2),
	currentBid		DECIMAL(10,2),
	buyNowPrice		DECIMAL(10,2),
	postDate		DATE,
	endDate			DATE,
	PRIMARY KEY (auctionId)
);

CREATE TABLE Bid (
	bidId			INT				NOT NULL,
	auctionId		INT				NOT NULL,
	bidderId		INT				NOT NULL,
	bidAmount		DECIMAL(10, 2),
	bidTime			DATE,
	PRIMARY KEY (bidId)
);

CREATE TABLE Message (
	messageId		INT				NOT NULL,
	senderId		INT				NOT NULL,
	receiverId		INT				NOT NULL,
	itemId			INT,
	content			VARCHAR(255),
	timeSent		DATE,
	PRIMARY KEY (messageId)
);

CREATE TABLE Transaction (
	transactionId	INT				NOT NULL,
	transactionDate	DATE			NOT NULL,
	amount			DECIMAL(10, 2)	NOT NULL,
	itemId			INT				NOT NULL,
	buyerId			INT				NOT NULL,
	sellerId		INT				NOT NULL,
	type			VARCHAR(15),
	PRIMARY KEY (transactionId)
);

CREATE TABLE Shipping (
	shippingId			INT			NOT NULL,
	transactionId		INT			NOT NULL,
	trackingNumber		VARCHAR(33),
	shippingDate		DATE,
	estimatedDelivery	DATE,
	PRIMARY KEY (shippingId)
);

CREATE TABLE Review (
	reviewId		INT				NOT NULL,
	UserId			INT				NOT NULL,
	transactionId	INT				NOT NULL,
	rating			INT				NOT NULL,
	comment			VARCHAR(255),
	reviewDate		DATE,
	PRIMARY KEY (reviewId)
);

-- automatically set the `Auction` postDate
DELIMITER //
CREATE TRIGGER SetAuctionPostDate BEFORE INSERT ON Auction
FOR EACH ROW
BEGIN
    SET NEW.postDate = CURRENT_DATE();
END;
//
DELIMITER ;

-- calculate the highest bidAmount
DELIMITER //
CREATE PROCEDURE GetHighestBid(IN auctionId INT, OUT highestBid DECIMAL(10,2))
BEGIN
    SELECT MAX(bidAmount) INTO highestBid FROM Bid WHERE auctionId = auctionId;
END;
//
DELIMITER ;

-- The view of every auction bid's detail
CREATE VIEW AuctionDetails AS
SELECT A.auctionId, I.title, A.startPrice, A.currentBid, A.endDate
FROM Auction A
JOIN Item I ON A.itemId = I.itemId;