-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 23, 2023 at 06:41 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `registrasi_mahasiswa`
--

-- --------------------------------------------------------

--
-- Table structure for table `daftar`
--

CREATE TABLE `daftar` (
  `Nim` int(10) NOT NULL,
  `Nama` varchar(100) NOT NULL,
  `Mata_kuliah` varchar(100) NOT NULL,
  `Biaya` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `daftar`
--

INSERT INTO `daftar` (`Nim`, `Nama`, `Mata_kuliah`, `Biaya`) VALUES
(0, '', '', 0),
(2183, 'mio', 'pemweb', 9000),
(2183, 'mio', 'pemweb', 9000),
(2183, 'mio', 'pemweb', 9000),
(2156, 'cio', 'jerman', 12000);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
