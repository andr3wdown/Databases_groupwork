CREATE TABLE ROOM(
    RoomID INT PRIMARY KEY AUTO_INCREMENT,
    HotelID INT NOT NULL,
    Capacity int NOT NULL,
    DailyPrice DECIMAL(10, 2) NOT NULL,
    RoomPhoneNr VARCHAR(16) NOT NULL,
    FOREIGN KEY (HotelID) REFERENCES HOTEL(HotelID)
);

INSERT INTO ROOM(HotelID, Capacity, DailyPrice, RoomPhoneNr)
VALUES
    (2, 5, 750, "+358100000002"),
    (2, 6, 900, "+358100000003"),
    (2, 2, 300, "+358100000004"),
    (2, 8, 1200, "+358100000005"),
    (2, 7, 1050, "+358100000006"),
    (1, 8, 1200, "+358100000007"),
    (1, 3, 450, "+358100000008"),
    (1, 5, 750, "+358100000009"),
    (1, 8, 1200, "+358100000010"),
    (2, 2, 300, "+358100000011"),
    (2, 5, 750, "+358100000012"),
    (2, 7, 1050, "+358100000013"),
    (1, 6, 900, "+358100000014"),
    (1, 5, 750, "+358100000015"),
    (1, 5, 750, "+358100000016"),
    (2, 4, 600, "+358100000017"),
    (2, 7, 1050, "+358100000018"),
    (2, 6, 900, "+358100000019"),
    (1, 3, 450, "+358100000020"),
    (1, 6, 900, "+358100000021"),
    (1, 8, 1200, "+358100000022"),
    (2, 3, 450, "+358100000023"),
    (1, 8, 1200, "+358100000024"),
    (2, 8, 1200, "+358100000025"),
    (2, 2, 300, "+358100000026"),
    (2, 8, 1200, "+358100000027"),
    (1, 2, 300, "+358100000028"),
    (1, 4, 600, "+358100000029"),
    (2, 3, 450, "+358100000030"),
    (1, 4, 600, "+358100000031");