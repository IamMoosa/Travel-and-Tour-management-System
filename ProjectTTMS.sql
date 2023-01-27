
--Tour and Travel Management System--

--Creating Database--
create database projectTTMS

--Using Database 'projectTTMS'--
use projectTTMS


--==============================================================================--

--Creating Tables--
CREATE TABLE Tour_Package (
    package_id varchar(50) PRIMARY KEY,
    package_name VARCHAR(255),
    package_description TEXT,
    package_price VARCHAR(20),
    package_duration INTEGER
);

CREATE TABLE Customer (
    customer_id varchar(50) PRIMARY KEY,
    customer_name VARCHAR(255),
    customer_email VARCHAR(255),
    customer_phone VARCHAR(255)
);

CREATE TABLE Transport (
    transport_id varchar(50) PRIMARY KEY,
    transport_type VARCHAR(255),
    transport_description TEXT,
    transport_capacity INTEGER
);

CREATE TABLE Hotel (
    hotel_id varchar(50) PRIMARY KEY,
    hotel_name VARCHAR(255),
    hotel_description TEXT,
    hotel_location VARCHAR(255),
    hotel_rating DECIMAL
);

CREATE TABLE Tourism_Place (
    place_id varchar(50) PRIMARY KEY,
    place_name VARCHAR(255),
    place_description TEXT,
    place_location VARCHAR(255),
    place_category VARCHAR(255)
);

CREATE TABLE Tour_Booking (
    booking_id INTEGER PRIMARY KEY identity(100,1),
    package_id VARCHAR(50),
    customer_id VARCHAR(50),
    transport_id VARCHAR(50),
    hotel_id VARCHAR(50),
    place_id VARCHAR(50),
    booking_date DATE,
    booking_total_price VARCHAR(50),
    booking_status VARCHAR(255),
    FOREIGN KEY (package_id) REFERENCES Tour_Package (package_id),
    FOREIGN KEY (customer_id) REFERENCES Customer (customer_id),
    FOREIGN KEY (transport_id) REFERENCES Transport (transport_id),
    FOREIGN KEY (hotel_id) REFERENCES Hotel (hotel_id),
    FOREIGN KEY (place_id) REFERENCES Tourism_Place (place_id)
);



--==============================================================================--
--INSERTION--


INSERT INTO Tour_Package (package_id, package_name, package_description, package_price, package_duration)
VALUES ('1', 'Hunza Valley Tour', 'Experience the beauty of Hunza with our comprehensive tour package', '5000', 7),
       ('2', 'Simple Swat Tour  ', 'Explore the diverse cultures of Asia with our tour package', '4000', 10),
       ('3', 'Super Saver Kashmir ', 'Experience the beauty of Kashmir with our comprehensive tour package', '6000', 14),
       ('4', 'Inspirational Kaghan'  , 'Experience the beauty of kaghan with our comprehensive tour package', '29000' ,5),
       ('5', 'Skardu Big Trip'	  , 'Experience the beauty of Skardu with our comprehensive tour package', '60000' ,4),
       ('6', 'Short trip to Kumrat' , 'Experience the beauty of Kumrat with our comprehensive tour package' , '15999' ,7)

INSERT INTO Customer (customer_id, customer_name, customer_email, customer_phone)
VALUES ('1', 'John Smith', 'john.smith@gmail.com', '123-456-7890'),
       ('2', 'Jane Doe', 'jane.doe@gmail.com', '234-567-8901'),
       ('3', 'Bob Johnson', 'bob.johnson@gmail.com', '345-678-9012');

INSERT INTO Transport (transport_id, transport_type, transport_description, transport_capacity)
VALUES ('1', 'By Air', 'PIA', 300),
       ('2', 'By Air', 'SERENE', 200),
       ('3', 'By Air', 'AIR SIAL', 250),
       ('4', 'By Air', 'AIR BLUE', 200);
	   
INSERT INTO Hotel (hotel_id, hotel_name, hotel_description, hotel_location, hotel_rating)
VALUES ('1', 'Hotel Crown Plaza', 'in the heart of Islamabad', 'Islamabad', 7.1),
       ('2', 'Shelton Hotel Johar Town', 'The hotel features elegant rooms',  'Lahore Pakistan', 3.0),
       ('3', 'Swat View Hotel', 'The hotel features a garden a restaurant a terrace', 'Sawat Pakistan', 6.8),
       ('4', 'Pine Park Hotel','Pine Park Hotel is located in Shogran Naran','Shogran Naran Pakistan' ,8.0),
       ('5', 'Hotel Felton',' It is a three Star Hotel','Muree Pakistan',7.0);

INSERT INTO Tourism_Place (place_id, place_name, place_description, place_location, place_category)
VALUES ('1', 'Hunza Valley', 'Mountainous  Valley', 'Gilgit Baltistan', 'Exotic place'),
       ('2', 'Swat',       'Mountainous  Valley', 'Malakand, KPK', 'Natural geographic region'),
       ('3', 'Kashmir',   'A Land of Unimaginable Beauty ', 'Azad Kashmir', 'Adventurous '),
       ('4', 'Kaghan' , 'Alpine Valley' , 'Mansehra KPK' , 'Exotic place'),
       ('5', 'Skardu' , 'Mountainous, Cold desert' , 'Gilgit Baltistan' , 'Adventurous'),
       ('6', 'Kumrat' , 'Mountainous  Valley' , 'Dir, KPK' , 'Natural geographic region');

INSERT INTO Tour_Booking (package_id, customer_id, transport_id, hotel_id, place_id, booking_date, booking_total_price, booking_status)
VALUES ('1', '1','1', '1', '1', '2022-01-01', '5000', 'Confirmed'),
       ('2', '2', '2', '2', '2', '2022-02-01', '4000', 'Confirmed'),
       ('3', '3', '3', '3','3', '2022-03-01', '6000', 'Confirmed');


--==============================================================================--
--VIEWING--


select * from Customer

select * from Hotel

select * from Tour_Booking

select * from Tour_Package

select * from Tourism_Place

select * from Transport

