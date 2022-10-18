-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 18, 2022 at 08:40 AM
-- Server version: 8.0.30
-- PHP Version: 7.4.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mini_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `doctor_table`
--

CREATE TABLE `doctor_table` (
  `doctor_reg` varchar(15) NOT NULL,
  `doctor_name` varchar(45) NOT NULL,
  `doctor_sex` varchar(45) NOT NULL,
  `doctor_age` varchar(45) NOT NULL,
  `doctor_add` varchar(45) NOT NULL,
  `doctor_tel` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `doctor_table`
--

INSERT INTO `doctor_table` (`doctor_reg`, `doctor_name`, `doctor_sex`, `doctor_age`, `doctor_add`, `doctor_tel`) VALUES
('D2177', 'Fernando sanira', 'Male', '52', 'Nattandiya', '742686520'),
('D2232', 'Ranga Perera', 'Male', '45', 'Matale', '775896235'),
('D2369', 'Nishantha JAS', 'Male', '29', 'Negombo', '702569854'),
('D2578', 'Mahesh Sudarshana', 'Female', '38', 'Kandy', '778956854'),
('D4545', 'Mahesh Fernando', 'Male', '34', 'Baticolo', '752569789'),
('D4578', 'Nalika Fernando', 'Femal', '32', 'Marawila', '712569552'),
('D4758', 'Kalhara Mendis', 'Femal', '44', 'Chilaw', '758965821'),
('D8575', 'Madushanka', 'Male', '53', 'Colombo', '775865244');

-- --------------------------------------------------------

--
-- Table structure for table `login_table`
--

CREATE TABLE `login_table` (
  `id` int NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `login_table`
--

INSERT INTO `login_table` (`id`, `username`, `password`) VALUES
(1, 'shehan', 'shehan123'),
(2, 'madu', 'madu123');

-- --------------------------------------------------------

--
-- Table structure for table `patient_table`
--

CREATE TABLE `patient_table` (
  `patient_reg` varchar(15) NOT NULL,
  `patient_name` varchar(45) NOT NULL,
  `patient_sex` varchar(45) NOT NULL,
  `patient_age` varchar(45) NOT NULL,
  `patient_address` varchar(45) NOT NULL,
  `patient_tel` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `patient_table`
--

INSERT INTO `patient_table` (`patient_reg`, `patient_name`, `patient_sex`, `patient_age`, `patient_address`, `patient_tel`) VALUES
('P2175', 'shehan', '27', 'Male', 'Nattandiya', '776925883'),
('P2176', 'Sihina', '25', 'Male', 'Nattandiya', '752686520'),
('P2178', 'shehan', 'Male', '26', 'Nattandiya', '776925883'),
('P2578', 'Mahesh Sudarshana', 'Female', '38', 'Kandy', '7789568544'),
('P7555', 'Nihala', 'Male', '27', 'India', '0776925883');

-- --------------------------------------------------------

--
-- Table structure for table `schedule_table`
--

CREATE TABLE `schedule_table` (
  `doctor_reg` varchar(15) NOT NULL,
  `slot1` varchar(45) DEFAULT NULL,
  `slot2` varchar(45) DEFAULT NULL,
  `slot3` varchar(45) DEFAULT NULL,
  `slot4` varchar(45) DEFAULT NULL,
  `slot5` varchar(45) DEFAULT NULL,
  `slot6` varchar(45) DEFAULT NULL,
  `slot7` varchar(45) DEFAULT NULL,
  `slot8` varchar(45) DEFAULT NULL,
  `slot9` varchar(45) DEFAULT NULL,
  `slot10` varchar(45) DEFAULT NULL,
  `slot11` varchar(45) DEFAULT NULL,
  `slot12` varchar(45) DEFAULT NULL,
  `slot13` varchar(45) DEFAULT NULL,
  `slot14` varchar(45) DEFAULT NULL,
  `slot15` varchar(45) DEFAULT NULL,
  `slot16` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `schedule_table`
--

INSERT INTO `schedule_table` (`doctor_reg`, `slot1`, `slot2`, `slot3`, `slot4`, `slot5`, `slot6`, `slot7`, `slot8`, `slot9`, `slot10`, `slot11`, `slot12`, `slot13`, `slot14`, `slot15`, `slot16`) VALUES
('D2169', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('D2177', 'P2178', 'P2178', NULL, NULL, 'P2176', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('D2232', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('D2369', 'P2578', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('D2578', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('D4545', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('D4578', 'P2176', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('D4758', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('D8575', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `doctor_table`
--
ALTER TABLE `doctor_table`
  ADD PRIMARY KEY (`doctor_reg`);

--
-- Indexes for table `login_table`
--
ALTER TABLE `login_table`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patient_table`
--
ALTER TABLE `patient_table`
  ADD PRIMARY KEY (`patient_reg`);

--
-- Indexes for table `schedule_table`
--
ALTER TABLE `schedule_table`
  ADD PRIMARY KEY (`doctor_reg`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `login_table`
--
ALTER TABLE `login_table`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
