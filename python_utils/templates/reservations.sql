CREATE TABLE RESERVATION(
    ReservationID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    RoomID INT NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES CUSTOMER(CustomerID),
    FOREIGN KEY (RoomID) REFERENCES ROOM(RoomID)
);

INSERT INTO RESERVATION(CustomerID, RoomID, StartDate, EndDate)
VALUES
_inserts_