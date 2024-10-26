/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 8.0.33 : Database - wanderlust
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`wanderlust` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `wanderlust`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add hotel',7,'add_hotel'),
(26,'Can change hotel',7,'change_hotel'),
(27,'Can delete hotel',7,'delete_hotel'),
(28,'Can view hotel',7,'view_hotel'),
(29,'Can add login',8,'add_login'),
(30,'Can change login',8,'change_login'),
(31,'Can delete login',8,'delete_login'),
(32,'Can view login',8,'view_login'),
(33,'Can add package',9,'add_package'),
(34,'Can change package',9,'change_package'),
(35,'Can delete package',9,'delete_package'),
(36,'Can view package',9,'view_package'),
(37,'Can add place',10,'add_place'),
(38,'Can change place',10,'change_place'),
(39,'Can delete place',10,'delete_place'),
(40,'Can view place',10,'view_place'),
(41,'Can add user',11,'add_user'),
(42,'Can change user',11,'change_user'),
(43,'Can delete user',11,'delete_user'),
(44,'Can view user',11,'view_user'),
(45,'Can add package_ booking',12,'add_package_booking'),
(46,'Can change package_ booking',12,'change_package_booking'),
(47,'Can delete package_ booking',12,'delete_package_booking'),
(48,'Can view package_ booking',12,'view_package_booking'),
(49,'Can add hotel_ booking',13,'add_hotel_booking'),
(50,'Can change hotel_ booking',13,'change_hotel_booking'),
(51,'Can delete hotel_ booking',13,'delete_hotel_booking'),
(52,'Can view hotel_ booking',13,'view_hotel_booking'),
(53,'Can add guide',14,'add_guide'),
(54,'Can change guide',14,'change_guide'),
(55,'Can delete guide',14,'delete_guide'),
(56,'Can view guide',14,'view_guide'),
(57,'Can add feedback',15,'add_feedback'),
(58,'Can change feedback',15,'change_feedback'),
(59,'Can delete feedback',15,'delete_feedback'),
(60,'Can view feedback',15,'view_feedback'),
(61,'Can add complaints',16,'add_complaints'),
(62,'Can change complaints',16,'change_complaints'),
(63,'Can delete complaints',16,'delete_complaints'),
(64,'Can view complaints',16,'view_complaints'),
(65,'Can add guide_ booking',17,'add_guide_booking'),
(66,'Can change guide_ booking',17,'change_guide_booking'),
(67,'Can delete guide_ booking',17,'delete_guide_booking'),
(68,'Can view guide_ booking',17,'view_guide_booking'),
(69,'Can add chat',18,'add_chat'),
(70,'Can change chat',18,'change_chat'),
(71,'Can delete chat',18,'delete_chat'),
(72,'Can view chat',18,'view_chat');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(18,'myapp','chat'),
(16,'myapp','complaints'),
(15,'myapp','feedback'),
(14,'myapp','guide'),
(17,'myapp','guide_booking'),
(7,'myapp','hotel'),
(13,'myapp','hotel_booking'),
(8,'myapp','login'),
(9,'myapp','package'),
(12,'myapp','package_booking'),
(10,'myapp','place'),
(11,'myapp','user'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-10-18 07:19:55.963648'),
(2,'auth','0001_initial','2024-10-18 07:19:56.518041'),
(3,'admin','0001_initial','2024-10-18 07:19:56.642576'),
(4,'admin','0002_logentry_remove_auto_add','2024-10-18 07:19:56.654233'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-10-18 07:19:56.663910'),
(6,'contenttypes','0002_remove_content_type_name','2024-10-18 07:19:56.738657'),
(7,'auth','0002_alter_permission_name_max_length','2024-10-18 07:19:56.790038'),
(8,'auth','0003_alter_user_email_max_length','2024-10-18 07:19:56.813625'),
(9,'auth','0004_alter_user_username_opts','2024-10-18 07:19:56.824162'),
(10,'auth','0005_alter_user_last_login_null','2024-10-18 07:19:56.874741'),
(11,'auth','0006_require_contenttypes_0002','2024-10-18 07:19:56.879404'),
(12,'auth','0007_alter_validators_add_error_messages','2024-10-18 07:19:56.889421'),
(13,'auth','0008_alter_user_username_max_length','2024-10-18 07:19:56.946887'),
(14,'auth','0009_alter_user_last_name_max_length','2024-10-18 07:19:57.000724'),
(15,'auth','0010_alter_group_name_max_length','2024-10-18 07:19:57.020706'),
(16,'auth','0011_update_proxy_permissions','2024-10-18 07:19:57.032019'),
(17,'auth','0012_alter_user_first_name_max_length','2024-10-18 07:19:57.092582'),
(18,'myapp','0001_initial','2024-10-18 07:19:57.744378'),
(19,'sessions','0001_initial','2024-10-18 07:19:57.778444'),
(20,'myapp','0002_remove_hotel_booking_name','2024-10-21 05:59:58.992970'),
(21,'myapp','0003_remove_package_booking_name','2024-10-21 06:13:10.608611'),
(22,'myapp','0004_auto_20241021_1221','2024-10-21 06:51:31.321150'),
(23,'myapp','0005_guide_booking','2024-10-21 08:37:03.152822'),
(24,'myapp','0006_auto_20241021_1410','2024-10-21 08:40:24.208825'),
(25,'myapp','0007_chat','2024-10-21 09:14:11.207478');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('770fmcngmtad1dg2ewa4amzrhw5za26j','eyJsaWQiOjF9:1t2ivj:ceUDypEoJ-7oZZ4kqAffU8jE4IakkL_1fbH0ZnmTCHE','2024-11-04 03:18:03.480306'),
('a05nevh34jl92f8iq7839noe6rphwk04','eyJsaWQiOjIsInVzZXJpZCI6IjUiLCJuZXciOiI1In0:1t3oXO:FpLOFSuyr4XrEL84fZUYnvjIC9o7T1P3rqKwSmnrX9o','2024-11-07 03:29:26.424038'),
('btp9uhsqm3acduugau9l6nz5ya1ancnc','eyJsaWQiOjF9:1t1lMS:aLdcnkMV8u9ssaBqhXfDd7iOExRt3YbDF-EmCTEYREU','2024-11-01 11:41:40.747214'),
('cdfev6hyxuvsrl2hv69e12fhzho61n8w','eyJsaWQiOjIsInVzZXJpZCI6IjIiLCJuZXciOiIyIn0:1t35jM:2GTuUEaUNMayy-Rd8-cx07lrFsVNliftq2ReoTzEVjw','2024-11-05 03:38:48.264227'),
('cgsxdt1imu2a2tppyejsrc21lc5nyigj','eyJsaWQiOjF9:1t2kEO:qFl0UxKlvj7wPZqMhn65hHd4axhQpJp2v_SZkJu-8ao','2024-11-04 04:41:24.925377'),
('oyn9z61apgmzbhs2mpvh90ttey2gwmx0','eyJsaWQiOiIiLCJ1c2VyaWQiOiIyIiwibmV3IjoiMiJ9:1t2ouf:QCAQWBuPmOS_M2GqeLbS2FyKUCiCt4w5LvhTUaV8tQE','2024-11-04 09:41:21.577127'),
('wbvamvtuh1p53myvwc9m2mvlzq9ea0wc','eyJsaWQiOjQsInVzZXJpZCI6IjIiLCJuZXciOiIyIn0:1t2q2t:HdWRgLISn1a1gCBkAmUFUdlTZuHvOJELKvvQpp7dq0c','2024-11-04 10:53:55.127132');

/*Table structure for table `myapp_chat` */

DROP TABLE IF EXISTS `myapp_chat`;

CREATE TABLE `myapp_chat` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `FROMID_id` bigint NOT NULL,
  `TOID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_chat_FROMID_id_c34a39e8_fk_myapp_login_id` (`FROMID_id`),
  KEY `myapp_chat_TOID_id_c3a45261_fk_myapp_login_id` (`TOID_id`),
  CONSTRAINT `myapp_chat_FROMID_id_c34a39e8_fk_myapp_login_id` FOREIGN KEY (`FROMID_id`) REFERENCES `myapp_login` (`id`),
  CONSTRAINT `myapp_chat_TOID_id_c3a45261_fk_myapp_login_id` FOREIGN KEY (`TOID_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_chat` */

insert  into `myapp_chat`(`id`,`message`,`date`,`FROMID_id`,`TOID_id`) values 
(1,'ff','2024-10-21',4,2),
(2,'hi','2024-10-21',4,2),
(3,'ok','2024-10-21',2,4),
(4,'ok','2024-10-21',2,4),
(5,'ok','2024-10-21',2,4),
(6,'hello','2024-10-21',2,4),
(7,'hlo','2024-10-21',2,4),
(8,'jo','2024-10-21',2,4),
(9,'fghn','2024-10-21',2,4),
(10,'ok','2024-10-21',4,2),
(11,'will check','2024-10-21',4,2),
(12,'ok','2024-10-21',4,2),
(13,'hello','2024-10-21',4,2),
(14,'hai','2024-10-21',2,4),
(15,'hello','2024-10-21',2,4),
(16,'hi','2024-10-22',2,5),
(17,'hi','2024-10-22',4,2);

/*Table structure for table `myapp_complaints` */

DROP TABLE IF EXISTS `myapp_complaints`;

CREATE TABLE `myapp_complaints` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_complaints_USER_id_f1892848_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_complaints_USER_id_f1892848_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_complaints` */

insert  into `myapp_complaints`(`id`,`complaint`,`reply`,`date`,`USER_id`) values 
(1,'wertgfh','ok','2024-10-21',1),
(2,'defrdgtfhygjk','pending','2024-10-22',1);

/*Table structure for table `myapp_feedback` */

DROP TABLE IF EXISTS `myapp_feedback`;

CREATE TABLE `myapp_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_feedback_USER_id_fce7ccff_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_feedback_USER_id_fce7ccff_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_feedback` */

insert  into `myapp_feedback`(`id`,`feedback`,`rating`,`date`,`USER_id`) values 
(1,'sd','3','2024-10-21',1),
(2,'asdfgh','1','2024-10-22',1);

/*Table structure for table `myapp_guide` */

DROP TABLE IF EXISTS `myapp_guide`;

CREATE TABLE `myapp_guide` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_guide_LOGIN_id_76f92f79_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_guide_LOGIN_id_76f92f79_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_guide` */

insert  into `myapp_guide`(`id`,`name`,`place`,`email`,`phone`,`post`,`LOGIN_id`) values 
(2,'Sankar Das N','sedrftg','sankardasnasd@gmail.com','9961207239','dfgh',4),
(3,'akshay babu','sedrftg','akshay@gmail.com','9961207244','dfgh',5);

/*Table structure for table `myapp_guide_booking` */

DROP TABLE IF EXISTS `myapp_guide_booking`;

CREATE TABLE `myapp_guide_booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` varchar(100) NOT NULL,
  `GUIDE_id` bigint NOT NULL,
  `PACKAGE_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_guide_booking_GUIDE_id_33e51780_fk_myapp_guide_id` (`GUIDE_id`),
  KEY `myapp_guide_booking_PACKAGE_id_a31f6cf2_fk_myapp_package_id` (`PACKAGE_id`),
  KEY `myapp_guide_booking_USER_id_c93e78c4_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_guide_booking_GUIDE_id_33e51780_fk_myapp_guide_id` FOREIGN KEY (`GUIDE_id`) REFERENCES `myapp_guide` (`id`),
  CONSTRAINT `myapp_guide_booking_PACKAGE_id_a31f6cf2_fk_myapp_package_id` FOREIGN KEY (`PACKAGE_id`) REFERENCES `myapp_package` (`id`),
  CONSTRAINT `myapp_guide_booking_USER_id_c93e78c4_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_guide_booking` */

insert  into `myapp_guide_booking`(`id`,`date`,`GUIDE_id`,`PACKAGE_id`,`USER_id`,`status`) values 
(2,'2024-10-22',2,4,1,'booked');

/*Table structure for table `myapp_hotel` */

DROP TABLE IF EXISTS `myapp_hotel`;

CREATE TABLE `myapp_hotel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` double NOT NULL,
  `description` varchar(100) NOT NULL,
  `facility` varchar(100) NOT NULL,
  `PLACE_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_hotel_PLACE_id_218a6e17_fk_myapp_place_id` (`PLACE_id`),
  CONSTRAINT `myapp_hotel_PLACE_id_218a6e17_fk_myapp_place_id` FOREIGN KEY (`PLACE_id`) REFERENCES `myapp_place` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_hotel` */

insert  into `myapp_hotel`(`id`,`name`,`image`,`price`,`description`,`facility`,`PLACE_id`) values 
(3,'grand hayath','/media/2024-10-21-16-59-00.jpg',20000,'sssa','pool',4),
(5,'lulu','/media/2024-10-22-08-57-15.jpg',40000,'erereerwer','pool',5);

/*Table structure for table `myapp_hotel_booking` */

DROP TABLE IF EXISTS `myapp_hotel_booking`;

CREATE TABLE `myapp_hotel_booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` varchar(100) NOT NULL,
  `price` double NOT NULL,
  `number_rooms` varchar(100) NOT NULL,
  `HOTEL_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_hotel_booking_HOTEL_id_bd1361ae_fk_myapp_hotel_id` (`HOTEL_id`),
  KEY `myapp_hotel_booking_USER_id_e901f8ea_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_hotel_booking_HOTEL_id_bd1361ae_fk_myapp_hotel_id` FOREIGN KEY (`HOTEL_id`) REFERENCES `myapp_hotel` (`id`),
  CONSTRAINT `myapp_hotel_booking_USER_id_e901f8ea_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_hotel_booking` */

insert  into `myapp_hotel_booking`(`id`,`date`,`price`,`number_rooms`,`HOTEL_id`,`USER_id`) values 
(3,'2024-10-21',160000,'8.0',3,1),
(4,'2024-10-22',160000,'8.0',3,1);

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'u','u','user'),
(4,'g','g','guide'),
(5,'akshay@gmail.com','9961207244','guide');

/*Table structure for table `myapp_package` */

DROP TABLE IF EXISTS `myapp_package`;

CREATE TABLE `myapp_package` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `number_days` varchar(100) NOT NULL,
  `PLACE_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_package_PLACE_id_e3efc47e_fk_myapp_place_id` (`PLACE_id`),
  CONSTRAINT `myapp_package_PLACE_id_e3efc47e_fk_myapp_place_id` FOREIGN KEY (`PLACE_id`) REFERENCES `myapp_place` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_package` */

insert  into `myapp_package`(`id`,`name`,`image`,`price`,`description`,`number_days`,`PLACE_id`) values 
(4,'bandipur','/media/2024-10-21-16-58-30.jpg','40000.0','qwq','2',4),
(6,'maldives','/media/2024-10-22-08-55-39.jpg','22500.0','qqw','30',4);

/*Table structure for table `myapp_package_booking` */

DROP TABLE IF EXISTS `myapp_package_booking`;

CREATE TABLE `myapp_package_booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` varchar(100) NOT NULL,
  `price` double NOT NULL,
  `PACKAGE_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_package_booking_PACKAGE_id_d948080f_fk_myapp_package_id` (`PACKAGE_id`),
  KEY `myapp_package_booking_USER_id_689cc166_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_package_booking_PACKAGE_id_d948080f_fk_myapp_package_id` FOREIGN KEY (`PACKAGE_id`) REFERENCES `myapp_package` (`id`),
  CONSTRAINT `myapp_package_booking_USER_id_689cc166_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_package_booking` */

insert  into `myapp_package_booking`(`id`,`date`,`price`,`PACKAGE_id`,`USER_id`) values 
(5,'2024-10-21',40000,4,1),
(6,'2024-10-22',40000,4,1);

/*Table structure for table `myapp_place` */

DROP TABLE IF EXISTS `myapp_place`;

CREATE TABLE `myapp_place` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `latitude` varchar(100) NOT NULL,
  `longitude` varchar(100) NOT NULL,
  `speciality` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_place` */

insert  into `myapp_place`(`id`,`name`,`place`,`image`,`latitude`,`longitude`,`speciality`,`description`) values 
(4,'bangalore','banasawadi','/media/2024-10-21-16-56-50.jpg','11.5000','76.0000','bnm,','ftghjn'),
(5,'kolkota','kolkota66','/media/2024-10-21-17-22-49.jpg','11.5000','76.0000','bnm,','ftghjn'),
(7,'Sankar Das N','perinthalmannawdwd79','/media/2024-10-22-08-48-27.jpg','10.976036','76.225441','asdf4','weeeer');

/*Table structure for table `myapp_user` */

DROP TABLE IF EXISTS `myapp_user`;

CREATE TABLE `myapp_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_user` */

insert  into `myapp_user`(`id`,`name`,`place`,`email`,`phone`,`post`,`LOGIN_id`) values 
(1,'Sankar Das N','sedrftg','admin@gmail.com','9961207239','dfgh',2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
