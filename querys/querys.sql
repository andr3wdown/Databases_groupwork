-- 1. selects all the hotel names from the HOTEL table.
SELECT HotelName AS Name
FROM HOTEL;

-- 2. selects all the rooms that have a daily price greater than 1000 or a capacity greater than 6.
SELECT *
FROM ROOM
WHERE DailyPrice > 1000 OR Capacity > 6;

-- 3. selects all the reservations that start on '2025-03-10' and end on '2025-03-15'.
SELECT * FROM RESERVATION
WHERE StartDate = '2025-03-10' AND EndDate = '2025-03-15';

-- 4. shows the total number of customers.
SELECT COUNT(*) AS TotalCustomers
FROM CUSTOMER;

-- 5. averages the daily price of all rooms.
SELECT AVG(DailyPrice) AS AveragePrice
FROM ROOM;

-- 6. sums the capacity of all rooms for the total capacity of all hotels.
SELECT SUM(Capacity) AS TotalCapacity
FROM ROOM;

-- 7. counts the number of rooms for  each hotel.
SELECT HotelID, COUNT(*) AS NumRooms
FROM ROOM
GROUP BY HotelID;

-- 8. selects the hotel ID, room ID, and daily price of all rooms that have a daily price less than or equal to 600.
SELECT HotelID, RoomID, DailyPrice
FROM ROOM
GROUP BY HotelID, RoomID, DailyPrice
HAVING DailyPrice <= 600;

-- 9. selects the hotel name and room ID of all rooms that are available between '2025-03-06' and '2025-03-12'.
SELECT h.HotelName, r.RoomID
FROM ROOM r
LEFT JOIN HOTEL h ON r.HotelID = h.HotelID
INNER JOIN RESERVATION re ON r.RoomID = re.RoomID
WHERE '2025-03-06' NOT BETWEEN re.StartDate AND re.EndDate
AND '2025-03-12' NOT BETWEEN re.StartDate AND re.EndDate
ORDER BY h.HotelName, r.RoomID;

-- 10. selects the first name, last name, room ID, start date, and start time of all shifts for employee ID 1.
SELECT e.FirstName, e.LastName, s.RoomID, s.StartDate, s.StartTime
FROM SHIFT s
INNER JOIN EMPLOYEE e ON s.EmployeeID = e.EmployeeID
WHERE s.EmployeeID = 1
ORDER BY s.StartDate, s.StartTime;