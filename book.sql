-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 18, 2023 at 11:09 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `book`
--

-- --------------------------------------------------------

--
-- Table structure for table `area`
--

CREATE TABLE `area` (
  `id` bigint(20) NOT NULL,
  `area_name` varchar(100) NOT NULL,
  `city_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `area`
--

INSERT INTO `area` (`id`, `area_name`, `city_id`) VALUES
(1, 'Nikol', 1);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add area', 7, 'add_area'),
(26, 'Can change area', 7, 'change_area'),
(27, 'Can delete area', 7, 'delete_area'),
(28, 'Can view area', 7, 'view_area'),
(29, 'Can add category', 8, 'add_category'),
(30, 'Can change category', 8, 'change_category'),
(31, 'Can delete category', 8, 'delete_category'),
(32, 'Can view category', 8, 'view_category'),
(33, 'Can add city', 9, 'add_city'),
(34, 'Can change city', 9, 'change_city'),
(35, 'Can delete city', 9, 'delete_city'),
(36, 'Can view city', 9, 'view_city'),
(37, 'Can add customer', 10, 'add_customer'),
(38, 'Can change customer', 10, 'change_customer'),
(39, 'Can delete customer', 10, 'delete_customer'),
(40, 'Can view customer', 10, 'view_customer'),
(41, 'Can add inquiry', 11, 'add_inquiry'),
(42, 'Can change inquiry', 11, 'change_inquiry'),
(43, 'Can delete inquiry', 11, 'delete_inquiry'),
(44, 'Can view inquiry', 11, 'view_inquiry'),
(45, 'Can add order', 12, 'add_order'),
(46, 'Can change order', 12, 'change_order'),
(47, 'Can delete order', 12, 'delete_order'),
(48, 'Can view order', 12, 'view_order'),
(49, 'Can add payment_ details', 13, 'add_payment_details'),
(50, 'Can change payment_ details', 13, 'change_payment_details'),
(51, 'Can delete payment_ details', 13, 'delete_payment_details'),
(52, 'Can view payment_ details', 13, 'view_payment_details'),
(53, 'Can add state', 14, 'add_state'),
(54, 'Can change state', 14, 'change_state'),
(55, 'Can delete state', 14, 'delete_state'),
(56, 'Can view state', 14, 'view_state'),
(57, 'Can add subcategory', 15, 'add_subcategory'),
(58, 'Can change subcategory', 15, 'change_subcategory'),
(59, 'Can delete subcategory', 15, 'delete_subcategory'),
(60, 'Can view subcategory', 15, 'view_subcategory'),
(61, 'Can add shipping', 16, 'add_shipping'),
(62, 'Can change shipping', 16, 'change_shipping'),
(63, 'Can delete shipping', 16, 'delete_shipping'),
(64, 'Can view shipping', 16, 'view_shipping'),
(65, 'Can add seller', 17, 'add_seller'),
(66, 'Can change seller', 17, 'change_seller'),
(67, 'Can delete seller', 17, 'delete_seller'),
(68, 'Can view seller', 17, 'view_seller'),
(69, 'Can add product', 18, 'add_product'),
(70, 'Can change product', 18, 'change_product'),
(71, 'Can delete product', 18, 'delete_product'),
(72, 'Can view product', 18, 'view_product'),
(73, 'Can add order_details', 19, 'add_order_details'),
(74, 'Can change order_details', 19, 'change_order_details'),
(75, 'Can delete order_details', 19, 'delete_order_details'),
(76, 'Can view order_details', 19, 'view_order_details'),
(77, 'Can add feedback', 20, 'add_feedback'),
(78, 'Can change feedback', 20, 'change_feedback'),
(79, 'Can delete feedback', 20, 'delete_feedback'),
(80, 'Can view feedback', 20, 'view_feedback'),
(81, 'Can add cart', 21, 'add_cart'),
(82, 'Can change cart', 21, 'change_cart'),
(83, 'Can delete cart', 21, 'delete_cart'),
(84, 'Can view cart', 21, 'view_cart'),
(85, 'Can add billing', 22, 'add_billing'),
(86, 'Can change billing', 22, 'change_billing'),
(87, 'Can delete billing', 22, 'delete_billing'),
(88, 'Can view billing', 22, 'view_billing'),
(89, 'Can add seller_ shop', 17, 'add_seller_shop'),
(90, 'Can change seller_ shop', 17, 'change_seller_shop'),
(91, 'Can delete seller_ shop', 17, 'delete_seller_shop'),
(92, 'Can view seller_ shop', 17, 'view_seller_shop');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$Xb1dkkWS2OyaBJyNSbkqgE$5OQkj/dJncnRyZeL/DWOog+yAObU6b7v9SrYycfX+zM=', '2023-04-18 08:51:42.372767', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2023-04-12 10:04:34.416931'),
(2, 'pbkdf2_sha256$600000$7flef3OM9zDmTlE63EDNqn$JcAhm23e5Pa0401PWe9Zidwf7Hkcqs0ASuSHurmPyRk=', '2023-04-18 08:36:35.229483', 0, 'abhi', 'abhi', 'patoliya', 'patoliyabhi17@gmail.com', 0, 1, '2023-04-12 10:05:32.281244'),
(3, 'pbkdf2_sha256$600000$8IqB0qzyHNhdsKXWznyExB$Ckhh6Q4LRdvls+OTxtFXIf2iYwc1rYFuoPtYCNp1z3o=', '2023-04-18 08:36:46.324942', 0, 'krish', 'krish', 'patel', 'krish@gmail.com', 0, 1, '2023-04-14 12:53:55.358490');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `billing`
--

CREATE TABLE `billing` (
  `id` bigint(20) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `address` longtext NOT NULL,
  `email` varchar(50) NOT NULL,
  `pin` varchar(50) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `area_id` bigint(20) NOT NULL,
  `city_id` bigint(20) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  `order_id` bigint(20) NOT NULL,
  `payment_details_id` bigint(20) NOT NULL,
  `state_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `billing`
--

INSERT INTO `billing` (`id`, `fname`, `lname`, `address`, `email`, `pin`, `phone`, `area_id`, `city_id`, `customer_id`, `order_id`, `payment_details_id`, `state_id`) VALUES
(9, 'krish', 'patel', 'ahmedabd', 'krish@gmail.com', '111', 56345346, 1, 1, 2, 10, 9, 1),
(10, 'abhi', 'patoliya', 'B/501 Shivam Casa', 'patoliyabhi17@gmail.com', '1234', 8980203030, 1, 1, 1, 11, 10, 1);

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `id` bigint(20) NOT NULL,
  `quantity` bigint(20) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id` bigint(20) NOT NULL,
  `cat_name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `cat_name`) VALUES
(1, 'Fiction');

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

CREATE TABLE `city` (
  `id` bigint(20) NOT NULL,
  `city_name` varchar(30) NOT NULL,
  `state_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `city`
--

INSERT INTO `city` (`id`, `city_name`, `state_id`) VALUES
(1, 'Ahmedabad', 1);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` bigint(20) NOT NULL,
  `contact` bigint(20) NOT NULL,
  `address` longtext NOT NULL,
  `gender` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `area_id` bigint(20) NOT NULL,
  `city_id` bigint(20) NOT NULL,
  `state_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `contact`, `address`, `gender`, `date`, `area_id`, `city_id`, `state_id`, `user_id`) VALUES
(1, 8980203030, 'B/501 Shivam Casa', 'male', '2023-04-12', 1, 1, 1, 2),
(2, 56345346, 'ahmedabd', 'male', '2023-04-14', 1, 1, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'myadmin', 'area'),
(22, 'myadmin', 'billing'),
(21, 'myadmin', 'cart'),
(8, 'myadmin', 'category'),
(9, 'myadmin', 'city'),
(10, 'myadmin', 'customer'),
(20, 'myadmin', 'feedback'),
(11, 'myadmin', 'inquiry'),
(12, 'myadmin', 'order'),
(19, 'myadmin', 'order_details'),
(13, 'myadmin', 'payment_details'),
(18, 'myadmin', 'product'),
(17, 'myadmin', 'seller_shop'),
(16, 'myadmin', 'shipping'),
(14, 'myadmin', 'state'),
(15, 'myadmin', 'subcategory'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-04-12 10:03:52.301753'),
(2, 'auth', '0001_initial', '2023-04-12 10:03:53.288164'),
(3, 'admin', '0001_initial', '2023-04-12 10:03:53.538165'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-04-12 10:03:53.585041'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-04-12 10:03:53.600666'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-04-12 10:03:53.772540'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-04-12 10:03:53.912105'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-04-12 10:03:53.943354'),
(9, 'auth', '0004_alter_user_username_opts', '2023-04-12 10:03:53.958985'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-04-12 10:03:54.052745'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-04-12 10:03:54.052745'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-04-12 10:03:54.068372'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-04-12 10:03:54.115230'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-04-12 10:03:54.193357'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-04-12 10:03:54.287108'),
(16, 'auth', '0011_update_proxy_permissions', '2023-04-12 10:03:54.333982'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-04-12 10:03:54.380857'),
(18, 'myadmin', '0001_initial', '2023-04-12 10:03:59.141430'),
(19, 'sessions', '0001_initial', '2023-04-12 10:03:59.220429'),
(20, 'myadmin', '0002_rename_seller_seller_shop_remove_order_customer_and_more', '2023-04-15 08:38:06.223503'),
(21, 'myadmin', '0003_rename_from_customer_order_details_seller', '2023-04-15 08:45:32.181351'),
(22, 'myadmin', '0004_product_stock_alter_customer_date', '2023-04-17 08:53:59.618647'),
(23, 'myadmin', '0002_order_return_date', '2023-04-17 09:39:57.046192'),
(24, 'myadmin', '0003_alter_order_return_date', '2023-04-17 09:41:14.689337'),
(25, 'myadmin', '0004_alter_order_penalty_alter_order_refund_and_more', '2023-04-17 09:46:14.779976'),
(26, 'myadmin', '0005_product_stock', '2023-04-17 09:47:36.010539'),
(27, 'myadmin', '0002_product_rent', '2023-04-17 11:41:40.906484');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('9rz995g7c1fj4y37r5w5jcti22kpdtb0', '.eJxtjDsOwjAQBe_imlj-xDihpOcM1q7XS8LHlhKnQtydREoBEu3Me_MSAZY6hGVOUxhJnIQWh2-GEO8pb4JukK9FxpLrNKLcJnK3s7wUSo_zvv0JDDAP65uB2XmFxhACxKhQt9xbS2yUZdWjNaR8ZN85k3yXYuodRTwyYstOb1GeyjMQ1LTmjDK2UW2j_Spq-YPfHw1ERY4:1pohK2:5U_XC_aI5HPzXG4rjzMPvwCgWT3rgV0Lrb-BJhSWq0o', '2023-05-02 09:08:22.565045'),
('fi9nbz8lj3qsea08k875edpf9y94w12l', '.eJxVjDsOwjAQBe_iGlnZdby2Kek5g7X-4QBypDipEHeHSCmgfTPzXsLztla_9bz4KYmzUOL0uwWOj9x2kO7cbrOMc1uXKchdkQft8jqn_Lwc7t9B5V6_NbN1EE0uYQDCUeukxgjFUlGo0Q0ElhCCI4M2BQMGKXAmygqJExjx_gDG-Tbn:1poLkV:GpPSX5xM0kNNET2oqvZ9BkRtvG4qheE6q0FSXbQNy2o', '2023-05-01 10:06:15.099987');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` bigint(20) NOT NULL,
  `rating` varchar(30) NOT NULL,
  `comment` longtext NOT NULL,
  `date` date NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `inquiry`
--

CREATE TABLE `inquiry` (
  `id` bigint(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `contact` bigint(20) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `message` longtext NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `id` bigint(20) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `seller_id` bigint(20) NOT NULL,
  `buyer_id` bigint(20) NOT NULL,
  `penalty` decimal(5,2) NOT NULL,
  `refund` decimal(5,2) NOT NULL,
  `rent` decimal(5,2) NOT NULL,
  `return_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order`
--

INSERT INTO `order` (`id`, `amount`, `date`, `status`, `seller_id`, `buyer_id`, `penalty`, `refund`, `rent`, `return_date`) VALUES
(10, '1100.00', '2023-03-17', 'returned', 1, 2, '13.33', '986.67', '100.00', '2023-04-18'),
(11, '3000.00', '2023-04-17', 'pending', 2, 1, '0.00', '0.00', '0.00', '2023-04-17');

-- --------------------------------------------------------

--
-- Table structure for table `order_details`
--

CREATE TABLE `order_details` (
  `id` bigint(20) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `order_id` bigint(20) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `seller_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order_details`
--

INSERT INTO `order_details` (`id`, `quantity`, `price`, `order_id`, `product_id`, `seller_id`) VALUES
(16, 1, '1100.00', 10, 2, 1),
(17, 1, '3000.00', 11, 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `payment_details`
--

CREATE TABLE `payment_details` (
  `id` bigint(20) NOT NULL,
  `payment_method` varchar(30) NOT NULL,
  `payment_id` longtext NOT NULL,
  `signature` longtext NOT NULL,
  `order_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payment_details`
--

INSERT INTO `payment_details` (`id`, `payment_method`, `payment_id`, `signature`, `order_id`) VALUES
(9, 'cod', 'cod', 'cod', 10),
(10, 'cod', 'cod', 'cod', 11);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` bigint(20) NOT NULL,
  `pname` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `quantity` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(255) NOT NULL,
  `author` varchar(100) NOT NULL,
  `t_type` varchar(20) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  `subcategory_id` bigint(20) NOT NULL,
  `stock` varchar(20) NOT NULL,
  `rent` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `pname`, `price`, `quantity`, `description`, `image`, `author`, `t_type`, `category_id`, `customer_id`, `subcategory_id`, `stock`, `rent`) VALUES
(1, 'THE HANGING GARDEN', '2000.00', '1', 'THE HANGING GARDENS', 'The_Notebook_Cover_2kO2UWR.jpg', 'George Orwell', 'sell', 1, 1, 1, 'in', '200.00'),
(2, 'Nineteen Eighty-Four', '1000.00', '1', 'Nineteen Eighty-Four', '1984first.jpg', 'Phillip E. Pack', 'rent', 1, 1, 1, 'in', '100.00'),
(4, 'Sapiens: A Brief History of Humankind', '3000.00', '1', 'Sapiens: A Brief History of Humankind', 'THE HANGING GARDEN.jpg', 'Nicholas Sparks', 'sell', 1, 2, 1, 'out', '300.00'),
(5, 'CliffsNotes AP Biology, 5th Edition ', '2000.00', '1', 'biology book', '1984first_1hWdswt.jpg', 'Shakespeare', 'rent', 1, 2, 1, 'in', '200.00');

-- --------------------------------------------------------

--
-- Table structure for table `seller_shop`
--

CREATE TABLE `seller_shop` (
  `id` bigint(20) NOT NULL,
  `contact` bigint(20) NOT NULL,
  `address` longtext NOT NULL,
  `owner_name` varchar(30) NOT NULL,
  `photo` varchar(255) NOT NULL,
  `about` longtext NOT NULL,
  `area_id` bigint(20) NOT NULL,
  `city_id` bigint(20) NOT NULL,
  `state_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `shipping`
--

CREATE TABLE `shipping` (
  `id` bigint(20) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `address` longtext NOT NULL,
  `email` varchar(50) NOT NULL,
  `pin` varchar(50) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `area_id` bigint(20) NOT NULL,
  `city_id` bigint(20) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  `order_id` bigint(20) NOT NULL,
  `payment_details_id` bigint(20) NOT NULL,
  `state_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shipping`
--

INSERT INTO `shipping` (`id`, `fname`, `lname`, `address`, `email`, `pin`, `phone`, `area_id`, `city_id`, `customer_id`, `order_id`, `payment_details_id`, `state_id`) VALUES
(9, 'krish', 'patel', 'ahmedabd', 'krish@gmail.com', '111', 56345346, 1, 1, 2, 10, 9, 1),
(10, 'abhi', 'patoliya', 'B/501 Shivam Casa', 'patoliyabhi17@gmail.com', '1234', 8980203030, 1, 1, 1, 11, 10, 1);

-- --------------------------------------------------------

--
-- Table structure for table `state`
--

CREATE TABLE `state` (
  `id` bigint(20) NOT NULL,
  `state_name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `state`
--

INSERT INTO `state` (`id`, `state_name`) VALUES
(1, 'Gujarat');

-- --------------------------------------------------------

--
-- Table structure for table `subcategory`
--

CREATE TABLE `subcategory` (
  `id` bigint(20) NOT NULL,
  `subcat_name` varchar(30) NOT NULL,
  `category_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subcategory`
--

INSERT INTO `subcategory` (`id`, `subcat_name`, `category_id`) VALUES
(1, 'Mystery', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`id`),
  ADD KEY `area_city_id_6c07a4b7_fk_city_id` (`city_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `billing`
--
ALTER TABLE `billing`
  ADD PRIMARY KEY (`id`),
  ADD KEY `billing_area_id_29f6b82a_fk_area_id` (`area_id`),
  ADD KEY `billing_city_id_848d4a2c_fk_city_id` (`city_id`),
  ADD KEY `billing_customer_id_e385dcd5_fk_customer_id` (`customer_id`),
  ADD KEY `billing_order_id_60886b31_fk_order_id` (`order_id`),
  ADD KEY `billing_payment_details_id_769adc83_fk_Payment_Details_id` (`payment_details_id`),
  ADD KEY `billing_state_id_fb26b84f_fk_state_id` (`state_id`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cart_customer_id_29e92815_fk_customer_id` (`customer_id`),
  ADD KEY `cart_product_id_508e72da_fk_product_id` (`product_id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`id`),
  ADD KEY `city_state_id_b686921b_fk_state_id` (`state_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD KEY `customer_state_id_bb047267_fk_state_id` (`state_id`),
  ADD KEY `customer_area_id_916acf30_fk_area_id` (`area_id`),
  ADD KEY `customer_city_id_f1096d59_fk_city_id` (`city_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`),
  ADD KEY `feedback_user_id_0104a377_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `inquiry`
--
ALTER TABLE `inquiry`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_buyer_id_d70e4ec3_fk_customer_id` (`buyer_id`),
  ADD KEY `order_seller_id_48ec66ac_fk_customer_id` (`seller_id`);

--
-- Indexes for table `order_details`
--
ALTER TABLE `order_details`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Order_details_order_id_54fca8f6_fk_order_id` (`order_id`),
  ADD KEY `Order_details_product_id_b3e730da_fk_product_id` (`product_id`),
  ADD KEY `Order_details_seller_id_881a98a0_fk_customer_id` (`seller_id`);

--
-- Indexes for table `payment_details`
--
ALTER TABLE `payment_details`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Payment_Details_order_id_303907f5_fk_order_id` (`order_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product_category_id_640030a0_fk_category_id` (`category_id`),
  ADD KEY `product_customer_id_9bc13c54_fk_customer_id` (`customer_id`),
  ADD KEY `product_subcategory_id_5651b678_fk_subcategory_id` (`subcategory_id`);

--
-- Indexes for table `seller_shop`
--
ALTER TABLE `seller_shop`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD KEY `seller_area_id_1fda800e_fk_area_id` (`area_id`),
  ADD KEY `seller_city_id_2e3de8a6_fk_city_id` (`city_id`),
  ADD KEY `seller_state_id_7c7eb780_fk_state_id` (`state_id`);

--
-- Indexes for table `shipping`
--
ALTER TABLE `shipping`
  ADD PRIMARY KEY (`id`),
  ADD KEY `shipping_area_id_f46fdcae_fk_area_id` (`area_id`),
  ADD KEY `shipping_city_id_0d30cbeb_fk_city_id` (`city_id`),
  ADD KEY `shipping_customer_id_ef7f4bc5_fk_customer_id` (`customer_id`),
  ADD KEY `shipping_order_id_fadc1339_fk_order_id` (`order_id`),
  ADD KEY `shipping_payment_details_id_a2918ec4_fk_Payment_Details_id` (`payment_details_id`),
  ADD KEY `shipping_state_id_74912c3f_fk_state_id` (`state_id`);

--
-- Indexes for table `state`
--
ALTER TABLE `state`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `subcategory`
--
ALTER TABLE `subcategory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `subcategory_category_id_4b55556d_fk_category_id` (`category_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `area`
--
ALTER TABLE `area`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=93;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `billing`
--
ALTER TABLE `billing`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `city`
--
ALTER TABLE `city`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inquiry`
--
ALTER TABLE `inquiry`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `order_details`
--
ALTER TABLE `order_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `payment_details`
--
ALTER TABLE `payment_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `seller_shop`
--
ALTER TABLE `seller_shop`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `shipping`
--
ALTER TABLE `shipping`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `state`
--
ALTER TABLE `state`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `subcategory`
--
ALTER TABLE `subcategory`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `area`
--
ALTER TABLE `area`
  ADD CONSTRAINT `area_city_id_6c07a4b7_fk_city_id` FOREIGN KEY (`city_id`) REFERENCES `city` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `billing`
--
ALTER TABLE `billing`
  ADD CONSTRAINT `billing_area_id_29f6b82a_fk_area_id` FOREIGN KEY (`area_id`) REFERENCES `area` (`id`),
  ADD CONSTRAINT `billing_city_id_848d4a2c_fk_city_id` FOREIGN KEY (`city_id`) REFERENCES `city` (`id`),
  ADD CONSTRAINT `billing_customer_id_e385dcd5_fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  ADD CONSTRAINT `billing_order_id_60886b31_fk_order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`),
  ADD CONSTRAINT `billing_payment_details_id_769adc83_fk_Payment_Details_id` FOREIGN KEY (`payment_details_id`) REFERENCES `payment_details` (`id`),
  ADD CONSTRAINT `billing_state_id_fb26b84f_fk_state_id` FOREIGN KEY (`state_id`) REFERENCES `state` (`id`);

--
-- Constraints for table `cart`
--
ALTER TABLE `cart`
  ADD CONSTRAINT `cart_customer_id_29e92815_fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  ADD CONSTRAINT `cart_product_id_508e72da_fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`);

--
-- Constraints for table `city`
--
ALTER TABLE `city`
  ADD CONSTRAINT `city_state_id_b686921b_fk_state_id` FOREIGN KEY (`state_id`) REFERENCES `state` (`id`);

--
-- Constraints for table `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `customer_area_id_916acf30_fk_area_id` FOREIGN KEY (`area_id`) REFERENCES `area` (`id`),
  ADD CONSTRAINT `customer_city_id_f1096d59_fk_city_id` FOREIGN KEY (`city_id`) REFERENCES `city` (`id`),
  ADD CONSTRAINT `customer_state_id_bb047267_fk_state_id` FOREIGN KEY (`state_id`) REFERENCES `state` (`id`),
  ADD CONSTRAINT `customer_user_id_fde49d68_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `feedback`
--
ALTER TABLE `feedback`
  ADD CONSTRAINT `feedback_user_id_0104a377_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `order_buyer_id_d70e4ec3_fk_customer_id` FOREIGN KEY (`buyer_id`) REFERENCES `customer` (`id`),
  ADD CONSTRAINT `order_seller_id_48ec66ac_fk_customer_id` FOREIGN KEY (`seller_id`) REFERENCES `customer` (`id`);

--
-- Constraints for table `order_details`
--
ALTER TABLE `order_details`
  ADD CONSTRAINT `Order_details_order_id_54fca8f6_fk_order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`),
  ADD CONSTRAINT `Order_details_product_id_b3e730da_fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`),
  ADD CONSTRAINT `Order_details_seller_id_881a98a0_fk_customer_id` FOREIGN KEY (`seller_id`) REFERENCES `customer` (`id`);

--
-- Constraints for table `payment_details`
--
ALTER TABLE `payment_details`
  ADD CONSTRAINT `Payment_Details_order_id_303907f5_fk_order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`);

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `product_category_id_640030a0_fk_category_id` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`),
  ADD CONSTRAINT `product_customer_id_9bc13c54_fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  ADD CONSTRAINT `product_subcategory_id_5651b678_fk_subcategory_id` FOREIGN KEY (`subcategory_id`) REFERENCES `subcategory` (`id`);

--
-- Constraints for table `seller_shop`
--
ALTER TABLE `seller_shop`
  ADD CONSTRAINT `seller_area_id_1fda800e_fk_area_id` FOREIGN KEY (`area_id`) REFERENCES `area` (`id`),
  ADD CONSTRAINT `seller_city_id_2e3de8a6_fk_city_id` FOREIGN KEY (`city_id`) REFERENCES `city` (`id`),
  ADD CONSTRAINT `seller_state_id_7c7eb780_fk_state_id` FOREIGN KEY (`state_id`) REFERENCES `state` (`id`),
  ADD CONSTRAINT `seller_user_id_2915e6aa_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `shipping`
--
ALTER TABLE `shipping`
  ADD CONSTRAINT `shipping_area_id_f46fdcae_fk_area_id` FOREIGN KEY (`area_id`) REFERENCES `area` (`id`),
  ADD CONSTRAINT `shipping_city_id_0d30cbeb_fk_city_id` FOREIGN KEY (`city_id`) REFERENCES `city` (`id`),
  ADD CONSTRAINT `shipping_customer_id_ef7f4bc5_fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  ADD CONSTRAINT `shipping_order_id_fadc1339_fk_order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`),
  ADD CONSTRAINT `shipping_payment_details_id_a2918ec4_fk_Payment_Details_id` FOREIGN KEY (`payment_details_id`) REFERENCES `payment_details` (`id`),
  ADD CONSTRAINT `shipping_state_id_74912c3f_fk_state_id` FOREIGN KEY (`state_id`) REFERENCES `state` (`id`);

--
-- Constraints for table `subcategory`
--
ALTER TABLE `subcategory`
  ADD CONSTRAINT `subcategory_category_id_4b55556d_fk_category_id` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
