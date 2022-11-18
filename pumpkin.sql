-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-11-2022 a las 17:26:30
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `pumpkin`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eventsdht11`
--

CREATE TABLE `eventsdht11` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `idPlant` int(11) NOT NULL,
  `temperature` int(11) NOT NULL,
  `humidity` int(11) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--load data infile 'C:/Users/angel/3D Objects/dht11data.csv' into table eventsdht11 fields terminated by ',' lines terminated by '\n';
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eventssi1145`
--

CREATE TABLE `eventssi1145` (
  `id` int(11) NOT NULL,
  `idPlant` int(11) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `uv` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eventssoilmoisture`
--

CREATE TABLE `eventssoilmoisture` (
  `id` int(11) NOT NULL,
  `idPlant` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `soilMoisture` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventary`
--

CREATE TABLE `inventary` (
  `id` int(11) NOT NULL,
  `userId` int(11) NOT NULL,
  `plantName` text NOT NULL,
  `plantType` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `inventary`
--

INSERT INTO `inventary` (`id`, `userId`, `plantName`, `plantType`) VALUES
(1, 0, 'veaaloe', 'Aloe Vera'),
(7, 8, 'dddd', 'Aloe Vera'),
(8, 8, 'xsxs', 'Lemon Tree'),
(9, 2, 'xsxsxdxd', 'Peace Lily'),
(10, 9, 'Yellow Lemon', 'Lemon Tree'),
(11, 1, 'RosaRosa', 'Peace Lily'),
(12, 8, 'dede', 'Peace Lily'),
(13, 8, 'cdcdcdcdcdcd', 'Peace Lily'),
(14, 8, 'angel', 'Aloe Vera'),
(15, 8, 'de', 'Aloe Vera');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `plants`
--

CREATE TABLE `plants` (
  `Id` int(11) NOT NULL,
  `commonName` text NOT NULL,
  `temperatureMax` int(11) NOT NULL,
  `temperatureMin` int(11) NOT NULL,
  `ambientHumidityMax` int(11) NOT NULL,
  `ambientHumidityMin` int(11) NOT NULL,
  `soilHumidityMax` int(11) NOT NULL,
  `soilHumidityMin` int(11) NOT NULL,
  `uvLevelMax` int(11) NOT NULL,
  `uvLevelMin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `plants`
--

INSERT INTO `plants` (`Id`, `commonName`, `temperatureMax`, `temperatureMin`, `ambientHumidityMax`, `ambientHumidityMin`, `soilHumidityMax`, `soilHumidityMin`, `uvLevelMax`, `uvLevelMin`) VALUES
(1, 'Lemon Tree', 25, 10, 20, 60, 2, 4, 1, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `Id` int(11) NOT NULL,
  `name` text NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `email` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`Id`, `name`, `username`, `password`, `email`) VALUES
(1, 'alvarogomez', 'agomez', 'sisisi', 'mail@mail.com'),
(2, 'aaa', 'aaa', 'aaa\r\n', 'aaa@mail.com'),
(8, 'tim', 'tim', 'tim', 'tim@mail.com'),
(9, 'James Smith', 'jamesSmith72', 'jamessmith', 'james.smith@gmail.com');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `eventsdht11`
--
ALTER TABLE `eventsdht11`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `eventssi1145`
--
ALTER TABLE `eventssi1145`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `eventssoilmoisture`
--
ALTER TABLE `eventssoilmoisture`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `inventary`
--
ALTER TABLE `inventary`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `plants`
--
ALTER TABLE `plants`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `eventsdht11`
--
ALTER TABLE `eventsdht11`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `eventssi1145`
--
ALTER TABLE `eventssi1145`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `eventssoilmoisture`
--
ALTER TABLE `eventssoilmoisture`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `inventary`
--
ALTER TABLE `inventary`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `plants`
--
ALTER TABLE `plants`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
