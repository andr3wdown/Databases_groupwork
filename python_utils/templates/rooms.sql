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
_inserts_