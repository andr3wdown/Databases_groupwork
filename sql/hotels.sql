CREATE TABLE HOTELS(
    HotelID INT PRIMARY KEY AUTO_INCREMENT,
    HotelName VARCHAR(64) NOT NULL,
    Address VARCHAR(128) NOT NULL,
    FrontDeskNR VARCHAR(16) NOT NULL
);

INSERT INTO HOTELS (HotelName, Address, FrontDeskNR)
VALUES
    ("Trivago", "Tikkuraitinkuja 2, Vantaa 01350", "+358100000000"),
    ("Korvatunturi", "Korvatunturintie 1, Korvatunturi 80000", "+358100000001");