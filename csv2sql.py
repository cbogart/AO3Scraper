
#id,replyto,username,forum,forum_types,discourse,title,when,annotation_link,annotation_rated,annotation_category,annotation_fandom,annotation_relationship,annotation_character,annotation_tags,annotation_status,annotation_comments,annotation_kudos,annotation_bookmarks,annotation_hits,dataset_file,post
#13762404_0001_00001,,madhadler,academia/Who Authorized This?/Chapter 1,FORUM/DOCUMENT/PARAGRAPH,AO3 academia,,2018-09-16T00:00:00,"<a href=""https://archiveofourown.org/works/13762404"">original</a>","[""Teen And Up Audiences""]",[],"[""\\u50d5\\u306e\\u30d2\\u30fc\\u30ed\\u30fc\\u30a2\\u30ab\\u30c7\\u30df\\u30a2 | Boku no Hero Academia | My Hero Academia""]","[""Bakugou Katsuki/Todoroki Shouto"", ""Bakugou Katsuki/Shinsou Hitoshi"", ""Ashido Mina/Kaminari Denki/Sero Hanta"", ""Kirishima Eijirou/Midoriya Izuku"", ""Jirou Kyouka/Yaoyorozu Momo"", ""Asui Tsuyu/Uraraka Ochako"", ""Bakugou Katsuki & Uraraka Ochako"", ""Bakugou Katsuki/Shinsou Hitoshi/Todoroki Shouto"", ""maybe more"", ""Aizawa Shouta | Eraserhead/Yamada Hizashi | Present Mic"", ""Dabi/Hawks (My Hero Academia)""]","[""Bakugou Katsuki"", ""Todoroki Shouto"", ""Uraraka Ochako"", ""Kirishima Eijirou"", ""Midoriya Izuku"", ""Iida Tenya"", ""Ashido Mina"", ""Kaminari Denki"", ""Asui Tsuyu"", ""Shinsou Hitoshi"", ""Sero Hanta"", ""Jirou Kyouka"", ""Yaoyorozu Momo"", ""Hagakure Tooru"", ""Yamada Hizashi | Present Mic"", ""Kayama Nemuri | Midnight"", ""Aizawa Shouta | Eraserhead"", ""Hawks (My Hero Academia)"", ""Dabi (My Hero Academia)""]","[""Bakugou Katsuki Swears A Lot"", ""This is just a mess"", ""I Am Too Lazy To List Every Character""]",Updated,264,1037,161,17340,ao3_academia,"Iidad added plain jane, ochahoe, and 17 others to CLASS 1A!"
#13762404_0001_00002,13762404_0001_00001,madhadler,academia/Who Authorized This?/Chapter 1,FORUM/DOCUMENT/PARAGRAPH,AO3 academia,,2018-09-16T00:00:00,"<a href=""https://archiveofourown.org/works/13762404"">original</a>","[""Teen And Up Audiences""]",[],"[""\\u50d5\\u306e\\u30d2\\u30fc\\u30ed\\u30fc\\u30a2\\u30ab\\u30c7\\u30df\\u30a2 | Boku no Hero Academia | My Hero Academia""]","[""Bakugou Katsuki/Todoroki Shouto"", ""Bakugou Katsuki/Shinsou Hitoshi"", ""Ashido Mina/Kaminari Denki/Sero Hanta"", ""Kirishima Eijirou/Midoriya Izuku"", ""Jirou Kyouka/Yaoyorozu Momo"", ""Asui Tsuyu/Uraraka Ochako"", ""Bakugou Katsuki & Uraraka Ochako"", ""Bakugou Katsuki/Shinsou Hitoshi/Todoroki Shouto"", ""maybe more"", ""Aizawa Shouta | Eraserhead/Yamada Hizashi | Present Mic"", ""Dabi/Hawks (My Hero Academia)""]","[""Bakugou Katsuki"", ""Todoroki Shouto"", ""Uraraka Ochako"", ""Kirishima Eijirou"", ""Midoriya Izuku"", ""Iida Tenya"", ""Ashido Mina"", ""Kaminari Denki"", ""Asui Tsuyu"", ""Shinsou Hitoshi"", ""Sero Hanta"", ""Jirou Kyouka"", ""Yaoyorozu Momo"", ""Hagakure Tooru"", ""Yamada Hizashi | Present Mic"", ""Kayama Nemuri | Midnight"", ""Aizawa Shouta | Eraserhead"", ""Hawks (My Hero Academia)"", ""Dabi (My Hero Academia)""]","[""Bakugou Katsuki Swears A Lot"", ""This is just a mess"", ""I Am Too Lazy To List Every Character""]",Updated,264,1037,161,17340,ao3_academia,Iidad:  Hello everyone! I have made this group chat so that we can all keep in contact!

dbname = "sample"

print (
"""-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: discoursedb_ext_%s
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `annotation_entity_proxy`
--

DROP TABLE IF EXISTS `annotation_entity_proxy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `annotation_entity_proxy` (
  `id_annotation_entity_proxy` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_annotation_entity_proxy`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `annotation_entity_proxy`
--

LOCK TABLES `annotation_entity_proxy` WRITE;
/*!40000 ALTER TABLE `annotation_entity_proxy` DISABLE KEYS */;
""", (,dbname))

proxy_values = 
print("""INSERT INTO `annotation_entity_proxy` VALUES """ + (1,'2018-09-19 14:19:51','2018-09-19 14:19:51',0),(2,'2018-09-19 14:19:52','2018-09-19 14:19:52',0),(3,'2018-09-19 14:19:52','2018-09-19 14:19:52',0),(4,'2018-09-19 14:19:52','2018-09-19 14:19:52',0),(5,'2018-09-19 14:19:52','2018-09-19 14:19:52',0),(6,'2018-09-19 14:20:08','2018-09-19 14:20:08',0),(7,'2018-09-19 14:20:08','2018-09-19 14:20:08',0),(8,'2018-09-19 14:20:08','2018-09-19 14:20:08',0);
/*!40000 ALTER TABLE `annotation_entity_proxy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `annotation_instance`
--

DROP TABLE IF EXISTS `annotation_instance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `annotation_instance` (
  `id_annotation_instance` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `annotator_email` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `begin_offset` int(11) DEFAULT NULL,
  `covered_text` text COLLATE utf8mb4_unicode_ci,
  `end_offset` int(11) DEFAULT NULL,
  `fk_data_sources` bigint(20) DEFAULT NULL,
  `fk_annotation_entity_proxy` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_annotation_instance`),
  KEY `FK_pjhx61f9ccn8mau851p2l2shf` (`fk_data_sources`),
  KEY `FK_ixf39ug518gw50j4o682hk9c9` (`fk_annotation_entity_proxy`),
  CONSTRAINT `FK_ixf39ug518gw50j4o682hk9c9` FOREIGN KEY (`fk_annotation_entity_proxy`) REFERENCES `annotation_entity_proxy` (`id_annotation_entity_proxy`),
  CONSTRAINT `FK_pjhx61f9ccn8mau851p2l2shf` FOREIGN KEY (`fk_data_sources`) REFERENCES `data_source_aggregate` (`id_data_sources`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `annotation_instance`
--

LOCK TABLES `annotation_instance` WRITE;
/*!40000 ALTER TABLE `annotation_instance` DISABLE KEYS */;
INSERT INTO `annotation_instance` VALUES (1,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,'link',NULL,0,NULL,0,NULL,1),(2,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,'rated',NULL,0,NULL,0,NULL,1),(3,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,'category',NULL,0,NULL,0,NULL,1),(4,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,'fandom',NULL,0,NULL,0,NULL,1),(5,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,'relationship',NULL,0,NULL,0,NULL,1),(6,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,'character',NULL,0,NULL,0,NULL,1),(7,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,'tags',NULL,0,NULL,0,NULL,1),(8,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,'status',NULL,0,NULL,0,NULL,1),(9,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,'comments',NULL,0,NULL,0,NULL,1),(10,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,'kudos',NULL,0,NULL,0,NULL,1),(11,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,'bookmarks',NULL,0,NULL,0,NULL,1),(12,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,'hits',NULL,0,NULL,0,NULL,1),(13,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'link',NULL,0,NULL,0,NULL,2),(14,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'rated',NULL,0,NULL,0,NULL,2),(15,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'category',NULL,0,NULL,0,NULL,2),(16,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'fandom',NULL,0,NULL,0,NULL,2),(17,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'relationship',NULL,0,NULL,0,NULL,2),(18,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'character',NULL,0,NULL,0,NULL,2),(19,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'tags',NULL,0,NULL,0,NULL,2),(20,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'status',NULL,0,NULL,0,NULL,2),(21,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'comments',NULL,0,NULL,0,NULL,2),(22,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'kudos',NULL,0,NULL,0,NULL,2),(23,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'bookmarks',NULL,0,NULL,0,NULL,2),(24,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'hits',NULL,0,NULL,0,NULL,2),(25,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'link',NULL,0,NULL,0,NULL,3),(26,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'rated',NULL,0,NULL,0,NULL,3),(27,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'category',NULL,0,NULL,0,NULL,3),(28,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'fandom',NULL,0,NULL,0,NULL,3),(29,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'relationship',NULL,0,NULL,0,NULL,3),(30,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'character',NULL,0,NULL,0,NULL,3),(31,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'tags',NULL,0,NULL,0,NULL,3),(32,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'status',NULL,0,NULL,0,NULL,3),(33,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'comments',NULL,0,NULL,0,NULL,3),(34,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'kudos',NULL,0,NULL,0,NULL,3),(35,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'bookmarks',NULL,0,NULL,0,NULL,3),(36,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'hits',NULL,0,NULL,0,NULL,3),(37,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'link',NULL,0,NULL,0,NULL,4),(38,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'rated',NULL,0,NULL,0,NULL,4),(39,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'category',NULL,0,NULL,0,NULL,4),(40,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'fandom',NULL,0,NULL,0,NULL,4),(41,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'relationship',NULL,0,NULL,0,NULL,4),(42,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'character',NULL,0,NULL,0,NULL,4),(43,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'tags',NULL,0,NULL,0,NULL,4),(44,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'status',NULL,0,NULL,0,NULL,4),(45,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'comments',NULL,0,NULL,0,NULL,4),(46,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'kudos',NULL,0,NULL,0,NULL,4),(47,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'bookmarks',NULL,0,NULL,0,NULL,4),(48,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'hits',NULL,0,NULL,0,NULL,4),(49,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'link',NULL,0,NULL,0,NULL,5),(50,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'rated',NULL,0,NULL,0,NULL,5),(51,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'category',NULL,0,NULL,0,NULL,5),(52,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'fandom',NULL,0,NULL,0,NULL,5),(53,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'relationship',NULL,0,NULL,0,NULL,5),(54,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'character',NULL,0,NULL,0,NULL,5),(55,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'tags',NULL,0,NULL,0,NULL,5),(56,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'status',NULL,0,NULL,0,NULL,5),(57,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'comments',NULL,0,NULL,0,NULL,5),(58,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'kudos',NULL,0,NULL,0,NULL,5),(59,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'bookmarks',NULL,0,NULL,0,NULL,5),(60,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,'hits',NULL,0,NULL,0,NULL,5),(61,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'link',NULL,0,NULL,0,NULL,6),(62,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'rated',NULL,0,NULL,0,NULL,6),(63,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'category',NULL,0,NULL,0,NULL,6),(64,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'fandom',NULL,0,NULL,0,NULL,6),(65,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'relationship',NULL,0,NULL,0,NULL,6),(66,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'character',NULL,0,NULL,0,NULL,6),(67,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'tags',NULL,0,NULL,0,NULL,6),(68,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'status',NULL,0,NULL,0,NULL,6),(69,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'comments',NULL,0,NULL,0,NULL,6),(70,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'kudos',NULL,0,NULL,0,NULL,6),(71,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'bookmarks',NULL,0,NULL,0,NULL,6),(72,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'hits',NULL,0,NULL,0,NULL,6),(73,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'link',NULL,0,NULL,0,NULL,7),(74,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'rated',NULL,0,NULL,0,NULL,7),(75,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'category',NULL,0,NULL,0,NULL,7),(76,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'fandom',NULL,0,NULL,0,NULL,7),(77,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'relationship',NULL,0,NULL,0,NULL,7),(78,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'character',NULL,0,NULL,0,NULL,7),(79,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'tags',NULL,0,NULL,0,NULL,7),(80,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'status',NULL,0,NULL,0,NULL,7),(81,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'comments',NULL,0,NULL,0,NULL,7),(82,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'kudos',NULL,0,NULL,0,NULL,7),(83,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'bookmarks',NULL,0,NULL,0,NULL,7),(84,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'hits',NULL,0,NULL,0,NULL,7),(85,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'link',NULL,0,NULL,0,NULL,8),(86,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'rated',NULL,0,NULL,0,NULL,8),(87,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'category',NULL,0,NULL,0,NULL,8),(88,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'fandom',NULL,0,NULL,0,NULL,8),(89,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'relationship',NULL,0,NULL,0,NULL,8),(90,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'character',NULL,0,NULL,0,NULL,8),(91,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'tags',NULL,0,NULL,0,NULL,8),(92,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'status',NULL,0,NULL,0,NULL,8),(93,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'comments',NULL,0,NULL,0,NULL,8),(94,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'kudos',NULL,0,NULL,0,NULL,8),(95,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'bookmarks',NULL,0,NULL,0,NULL,8),(96,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,'hits',NULL,0,NULL,0,NULL,8);
/*!40000 ALTER TABLE `annotation_instance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `annotation_relation`
--

DROP TABLE IF EXISTS `annotation_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `annotation_relation` (
  `id_annotation_relation` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `first_in_chain` int(11) NOT NULL,
  `fk_source` bigint(20) DEFAULT NULL,
  `fk_target` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_annotation_relation`),
  KEY `FK_3thy67erikhiyp85cfpcha6d` (`fk_source`),
  KEY `FK_fvnbst4kxhwkaoe28jtoxn3vq` (`fk_target`),
  CONSTRAINT `FK_3thy67erikhiyp85cfpcha6d` FOREIGN KEY (`fk_source`) REFERENCES `annotation_instance` (`id_annotation_instance`),
  CONSTRAINT `FK_fvnbst4kxhwkaoe28jtoxn3vq` FOREIGN KEY (`fk_target`) REFERENCES `annotation_instance` (`id_annotation_instance`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `annotation_relation`
--

LOCK TABLES `annotation_relation` WRITE;
/*!40000 ALTER TABLE `annotation_relation` DISABLE KEYS */;
/*!40000 ALTER TABLE `annotation_relation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audience`
--

DROP TABLE IF EXISTS `audience`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `audience` (
  `id_audience` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `fk_annotation` bigint(20) DEFAULT NULL,
  `fk_data_sources` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_audience`),
  KEY `FK_hy6mye4djx2275c0kjbhn99b0` (`fk_annotation`),
  KEY `FK_2yp1f0vsxuk6yklc2o336b4rf` (`fk_data_sources`),
  CONSTRAINT `FK_2yp1f0vsxuk6yklc2o336b4rf` FOREIGN KEY (`fk_data_sources`) REFERENCES `data_source_aggregate` (`id_data_sources`),
  CONSTRAINT `FK_hy6mye4djx2275c0kjbhn99b0` FOREIGN KEY (`fk_annotation`) REFERENCES `annotation_entity_proxy` (`id_annotation_entity_proxy`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audience`
--

LOCK TABLES `audience` WRITE;
/*!40000 ALTER TABLE `audience` DISABLE KEYS */;
/*!40000 ALTER TABLE `audience` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audience_has_group`
--

DROP TABLE IF EXISTS `audience_has_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `audience_has_group` (
  `id_audience_group` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `fk_audience` bigint(20) DEFAULT NULL,
  `fk_group` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_audience_group`),
  UNIQUE KEY `UK_3ecm91e8s5ta3ycpnpnbghqbs` (`fk_audience`,`fk_group`),
  KEY `FK_j71ambav2yd7hcrw37xqelad9` (`fk_group`),
  CONSTRAINT `FK_gp6718ra1tp00gaveubuwdsfk` FOREIGN KEY (`fk_audience`) REFERENCES `audience` (`id_audience`),
  CONSTRAINT `FK_j71ambav2yd7hcrw37xqelad9` FOREIGN KEY (`fk_group`) REFERENCES `group` (`id_group`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audience_has_group`
--

LOCK TABLES `audience_has_group` WRITE;
/*!40000 ALTER TABLE `audience_has_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `audience_has_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audience_has_user`
--

DROP TABLE IF EXISTS `audience_has_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `audience_has_user` (
  `id_audience_user` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `fk_audience` bigint(20) DEFAULT NULL,
  `fk_user` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_audience_user`),
  KEY `FK_iaqreew9mxm509aeeuhiqlocc` (`fk_audience`),
  KEY `FK_hcuurocx2swp7jeencc7i249i` (`fk_user`),
  CONSTRAINT `FK_hcuurocx2swp7jeencc7i249i` FOREIGN KEY (`fk_user`) REFERENCES `user` (`id_user`),
  CONSTRAINT `FK_iaqreew9mxm509aeeuhiqlocc` FOREIGN KEY (`fk_audience`) REFERENCES `audience` (`id_audience`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audience_has_user`
--

LOCK TABLES `audience_has_user` WRITE;
/*!40000 ALTER TABLE `audience_has_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `audience_has_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `content`
--

DROP TABLE IF EXISTS `content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `content` (
  `id_content` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `data` longblob,
  `text` longtext COLLATE utf8mb4_unicode_ci,
  `title` text COLLATE utf8mb4_unicode_ci,
  `fk_annotation` bigint(20) DEFAULT NULL,
  `fk_data_sources` bigint(20) DEFAULT NULL,
  `fk_user_id` bigint(20) DEFAULT NULL,
  `fk_next_revision` bigint(20) DEFAULT NULL,
  `fk_previous_revision` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_content`),
  KEY `FK_ltsosu4ohduohe1ewhxbxbjq6` (`fk_annotation`),
  KEY `FK_c6o3epjp27nob9g7vs9wutdfa` (`fk_data_sources`),
  KEY `FK_pcj8267433emqdcx83tadm5jk` (`fk_user_id`),
  KEY `FK_ddmryl7b1ri73wtaqo2i947a0` (`fk_next_revision`),
  KEY `FK_h835mqrhh3wlnqh3a71817mqv` (`fk_previous_revision`),
  CONSTRAINT `FK_c6o3epjp27nob9g7vs9wutdfa` FOREIGN KEY (`fk_data_sources`) REFERENCES `data_source_aggregate` (`id_data_sources`),
  CONSTRAINT `FK_ddmryl7b1ri73wtaqo2i947a0` FOREIGN KEY (`fk_next_revision`) REFERENCES `content` (`id_content`),
  CONSTRAINT `FK_h835mqrhh3wlnqh3a71817mqv` FOREIGN KEY (`fk_previous_revision`) REFERENCES `content` (`id_content`),
  CONSTRAINT `FK_ltsosu4ohduohe1ewhxbxbjq6` FOREIGN KEY (`fk_annotation`) REFERENCES `annotation_entity_proxy` (`id_annotation_entity_proxy`),
  CONSTRAINT `FK_pcj8267433emqdcx83tadm5jk` FOREIGN KEY (`fk_user_id`) REFERENCES `user` (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content`
--

LOCK TABLES `content` WRITE;
/*!40000 ALTER TABLE `content` DISABLE KEYS */;
INSERT INTO `content` VALUES (1,'2018-09-19 14:19:51','2018-09-19 14:19:51',1,NULL,'2018-09-16 00:00:00',NULL,'Iidad added plain jane, ochahoe, and 17 others to CLASS 1A!','',NULL,5,1,NULL,NULL),(2,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'2018-09-16 00:00:00',NULL,'Iidad:  Hello everyone! I have made this group chat so that we can all keep in contact!','',NULL,7,1,NULL,NULL),(3,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'2018-09-16 00:00:00',NULL,'StaticShock:  cheers bro I’ll drink to that','',NULL,9,1,NULL,NULL),(4,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'2018-09-16 00:00:00',NULL,'2/ 5 r single and pining','',NULL,12,1,NULL,NULL),(5,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'2018-09-16 00:00:00',NULL,'BubblegumBitch:  kiri how was ur date?','',NULL,14,1,NULL,NULL),(6,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'2018-09-16 00:00:00',NULL,'CLASS 1A','',NULL,17,1,NULL,NULL),(7,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'2018-09-16 00:00:00',NULL,'oneokrock:  someone help I’m trying to sing high school musical I Don’t Dance and every time I sing the “I don’t dance” Bakugou sings back in the tone of cardi b “I make money moves” and I have had ENOUGH','',NULL,19,1,NULL,NULL),(8,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'2018-09-16 00:00:00',NULL,'Albert Einstein:  does he rly have the moves tho','',NULL,21,1,NULL,NULL);
/*!40000 ALTER TABLE `content` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contribution`
--

DROP TABLE IF EXISTS `contribution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contribution` (
  `id_contribution` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `downvotes` int(11) DEFAULT NULL,
  `upvotes` int(11) DEFAULT NULL,
  `fk_annotation` bigint(20) DEFAULT NULL,
  `fk_data_sources` bigint(20) DEFAULT NULL,
  `fk_current_revision` bigint(20) DEFAULT NULL,
  `fk_first_revision` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_contribution`),
  KEY `FK_pump0fslyx0kqg9gys43ff07n` (`fk_annotation`),
  KEY `FK_sddu29xqypd54mm9i9mn5udhg` (`fk_data_sources`),
  KEY `FK_sl4gwv9bed7hbmdynn91p6pu4` (`fk_current_revision`),
  KEY `FK_obgv1pg2b6b0arty59h9pxdwd` (`fk_first_revision`),
  CONSTRAINT `FK_obgv1pg2b6b0arty59h9pxdwd` FOREIGN KEY (`fk_first_revision`) REFERENCES `content` (`id_content`),
  CONSTRAINT `FK_pump0fslyx0kqg9gys43ff07n` FOREIGN KEY (`fk_annotation`) REFERENCES `annotation_entity_proxy` (`id_annotation_entity_proxy`),
  CONSTRAINT `FK_sddu29xqypd54mm9i9mn5udhg` FOREIGN KEY (`fk_data_sources`) REFERENCES `data_source_aggregate` (`id_data_sources`),
  CONSTRAINT `FK_sl4gwv9bed7hbmdynn91p6pu4` FOREIGN KEY (`fk_current_revision`) REFERENCES `content` (`id_content`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contribution`
--

LOCK TABLES `contribution` WRITE;
/*!40000 ALTER TABLE `contribution` DISABLE KEYS */;
INSERT INTO `contribution` VALUES (1,'2018-09-19 14:19:51','2018-09-19 14:19:52',2,'POST',NULL,'2018-09-16 00:00:00',0,0,1,6,1,1),(2,'2018-09-19 14:19:52','2018-09-19 14:19:52',2,'POST',NULL,'2018-09-16 00:00:00',0,0,2,8,2,2),(3,'2018-09-19 14:19:52','2018-09-19 14:19:52',2,'POST',NULL,'2018-09-16 00:00:00',0,0,3,10,3,3),(4,'2018-09-19 14:19:52','2018-09-19 14:19:52',2,'POST',NULL,'2018-09-16 00:00:00',0,0,4,13,4,4),(5,'2018-09-19 14:19:52','2018-09-19 14:19:52',2,'POST',NULL,'2018-09-16 00:00:00',0,0,5,15,5,5),(6,'2018-09-19 14:20:08','2018-09-19 14:20:08',2,'POST',NULL,'2018-09-16 00:00:00',0,0,6,18,6,6),(7,'2018-09-19 14:20:08','2018-09-19 14:20:08',2,'POST',NULL,'2018-09-16 00:00:00',0,0,7,20,7,7),(8,'2018-09-19 14:20:08','2018-09-19 14:20:08',2,'POST',NULL,'2018-09-16 00:00:00',0,0,8,22,8,8);
/*!40000 ALTER TABLE `contribution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contribution_has_audience`
--

DROP TABLE IF EXISTS `contribution_has_audience`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contribution_has_audience` (
  `id_contribution_audience` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `fk_audience` bigint(20) DEFAULT NULL,
  `fk_contribution` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_contribution_audience`),
  KEY `FK_efnc2mxbs43owad2d6c0bc6xj` (`fk_audience`),
  KEY `FK_4g4xv7j61qfdjhfbytqi15kn0` (`fk_contribution`),
  CONSTRAINT `FK_4g4xv7j61qfdjhfbytqi15kn0` FOREIGN KEY (`fk_contribution`) REFERENCES `contribution` (`id_contribution`),
  CONSTRAINT `FK_efnc2mxbs43owad2d6c0bc6xj` FOREIGN KEY (`fk_audience`) REFERENCES `audience` (`id_audience`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contribution_has_audience`
--

LOCK TABLES `contribution_has_audience` WRITE;
/*!40000 ALTER TABLE `contribution_has_audience` DISABLE KEYS */;
/*!40000 ALTER TABLE `contribution_has_audience` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contribution_has_context`
--

DROP TABLE IF EXISTS `contribution_has_context`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contribution_has_context` (
  `id_contribution_context` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `begin_offset` int(11) DEFAULT NULL,
  `end_offset` int(11) DEFAULT NULL,
  `fk_context_content` bigint(20) DEFAULT NULL,
  `fk_context_contribution` bigint(20) DEFAULT NULL,
  `fk_contribution` bigint(20) NOT NULL,
  PRIMARY KEY (`id_contribution_context`),
  UNIQUE KEY `UK_b3x0om10diy25aye5p1vlx82u` (`fk_contribution`,`fk_context_contribution`,`fk_context_content`,`begin_offset`,`end_offset`),
  KEY `FK_kd7ptxjsqgplkdlah7juw08c` (`fk_context_content`),
  KEY `FK_8ich3fucolb45if0e5mksin7d` (`fk_context_contribution`),
  CONSTRAINT `FK_8ich3fucolb45if0e5mksin7d` FOREIGN KEY (`fk_context_contribution`) REFERENCES `contribution` (`id_contribution`),
  CONSTRAINT `FK_jirmpdqfctocoj8983s6yt86f` FOREIGN KEY (`fk_contribution`) REFERENCES `contribution` (`id_contribution`),
  CONSTRAINT `FK_kd7ptxjsqgplkdlah7juw08c` FOREIGN KEY (`fk_context_content`) REFERENCES `content` (`id_content`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contribution_has_context`
--

LOCK TABLES `contribution_has_context` WRITE;
/*!40000 ALTER TABLE `contribution_has_context` DISABLE KEYS */;
/*!40000 ALTER TABLE `contribution_has_context` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contribution_interaction`
--

DROP TABLE IF EXISTS `contribution_interaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contribution_interaction` (
  `id_contribution_interaction` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `fk_annotation` bigint(20) DEFAULT NULL,
  `fk_content` bigint(20) DEFAULT NULL,
  `fk_contribution` bigint(20) DEFAULT NULL,
  `fk_user` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_contribution_interaction`),
  UNIQUE KEY `UK_ipd0efnp472yqs79d1ie8t901` (`fk_user`,`type`,`fk_contribution`),
  UNIQUE KEY `UK_9y4o17k15wv5ywqf9h81gmbhr` (`fk_user`,`type`,`fk_content`),
  KEY `FK_2dy5j37flw2vmvj8ct6felont` (`fk_annotation`),
  KEY `FK_ot1ayxfcqeek9me1ipikw7kyd` (`fk_content`),
  KEY `FK_csr1j9woh8u8frxsjql2q3rco` (`fk_contribution`),
  CONSTRAINT `FK_2dy5j37flw2vmvj8ct6felont` FOREIGN KEY (`fk_annotation`) REFERENCES `annotation_entity_proxy` (`id_annotation_entity_proxy`),
  CONSTRAINT `FK_csr1j9woh8u8frxsjql2q3rco` FOREIGN KEY (`fk_contribution`) REFERENCES `contribution` (`id_contribution`),
  CONSTRAINT `FK_li5sbn6mdm2lwibwqians3i2n` FOREIGN KEY (`fk_user`) REFERENCES `user` (`id_user`),
  CONSTRAINT `FK_ot1ayxfcqeek9me1ipikw7kyd` FOREIGN KEY (`fk_content`) REFERENCES `content` (`id_content`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contribution_interaction`
--

LOCK TABLES `contribution_interaction` WRITE;
/*!40000 ALTER TABLE `contribution_interaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `contribution_interaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contribution_partof_discourse_part`
--

DROP TABLE IF EXISTS `contribution_partof_discourse_part`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contribution_partof_discourse_part` (
  `id_discourse_part_contribution` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `fk_contribution` bigint(20) DEFAULT NULL,
  `fk_discourse_part` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_discourse_part_contribution`),
  UNIQUE KEY `UK_25q84mih7txxybwnj0c74wx58` (`fk_contribution`,`fk_discourse_part`),
  KEY `FK_qrh8iershjb7gs1uujkbc24a7` (`fk_discourse_part`),
  CONSTRAINT `FK_9adsfievxemacex4e8u7t9g14` FOREIGN KEY (`fk_contribution`) REFERENCES `contribution` (`id_contribution`),
  CONSTRAINT `FK_qrh8iershjb7gs1uujkbc24a7` FOREIGN KEY (`fk_discourse_part`) REFERENCES `discourse_part` (`id_discourse_part`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contribution_partof_discourse_part`
--

LOCK TABLES `contribution_partof_discourse_part` WRITE;
/*!40000 ALTER TABLE `contribution_partof_discourse_part` DISABLE KEYS */;
INSERT INTO `contribution_partof_discourse_part` VALUES (1,'2018-09-19 14:19:51','2018-09-19 14:19:51',0,NULL,NULL,'2018-09-16 00:00:00',1,3),(2,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,NULL,NULL,'2018-09-16 00:00:00',2,3),(3,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,NULL,NULL,'2018-09-16 00:00:00',3,3),(4,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,NULL,NULL,'2018-09-16 00:00:00',4,4),(5,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,NULL,NULL,'2018-09-16 00:00:00',5,4),(6,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,NULL,NULL,'2018-09-16 00:00:00',6,5),(7,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,NULL,NULL,'2018-09-16 00:00:00',7,5),(8,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,NULL,NULL,'2018-09-16 00:00:00',8,5);
/*!40000 ALTER TABLE `contribution_partof_discourse_part` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_source_aggregate`
--

DROP TABLE IF EXISTS `data_source_aggregate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data_source_aggregate` (
  `id_data_sources` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_data_sources`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_source_aggregate`
--

LOCK TABLES `data_source_aggregate` WRITE;
/*!40000 ALTER TABLE `data_source_aggregate` DISABLE KEYS */;
INSERT INTO `data_source_aggregate` VALUES (1,'2018-09-19 14:19:51','2018-09-19 14:19:51',0),(2,'2018-09-19 14:19:51','2018-09-19 14:19:51',0),(3,'2018-09-19 14:19:51','2018-09-19 14:19:51',0),(4,'2018-09-19 14:19:51','2018-09-19 14:19:51',0),(5,'2018-09-19 14:19:51','2018-09-19 14:19:51',0),(6,'2018-09-19 14:19:51','2018-09-19 14:19:51',0),(7,'2018-09-19 14:19:52','2018-09-19 14:19:52',0),(8,'2018-09-19 14:19:52','2018-09-19 14:19:52',0),(9,'2018-09-19 14:19:52','2018-09-19 14:19:52',0),(10,'2018-09-19 14:19:52','2018-09-19 14:19:52',0),(11,'2018-09-19 14:19:52','2018-09-19 14:19:52',0),(12,'2018-09-19 14:19:52','2018-09-19 14:19:52',0),(13,'2018-09-19 14:19:52','2018-09-19 14:19:52',0),(14,'2018-09-19 14:19:52','2018-09-19 14:19:52',0),(15,'2018-09-19 14:19:52','2018-09-19 14:19:52',0),(16,'2018-09-19 14:20:08','2018-09-19 14:20:08',0),(17,'2018-09-19 14:20:08','2018-09-19 14:20:08',0),(18,'2018-09-19 14:20:08','2018-09-19 14:20:08',0),(19,'2018-09-19 14:20:08','2018-09-19 14:20:08',0),(20,'2018-09-19 14:20:08','2018-09-19 14:20:08',0),(21,'2018-09-19 14:20:08','2018-09-19 14:20:08',0),(22,'2018-09-19 14:20:08','2018-09-19 14:20:08',0);
/*!40000 ALTER TABLE `data_source_aggregate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_source_instance`
--

DROP TABLE IF EXISTS `data_source_instance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data_source_instance` (
  `id_data_source_instance` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `dataset_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `entity_source_descriptor` varchar(95) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `entity_source_id` varchar(95) COLLATE utf8mb4_unicode_ci NOT NULL,
  `source_type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fk_sources` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_data_source_instance`),
  UNIQUE KEY `UK_af1bx9964hucwyjtvl3jy302l` (`entity_source_id`,`entity_source_descriptor`,`dataset_name`),
  KEY `sourceId_descriptor_Index` (`entity_source_id`,`entity_source_descriptor`),
  KEY `sourceDescriptorIndex` (`entity_source_descriptor`),
  KEY `sourceIdIndex` (`entity_source_id`),
  KEY `FK_3j2xvtdxmtucbrawb2os521v5` (`fk_sources`),
  CONSTRAINT `FK_3j2xvtdxmtucbrawb2os521v5` FOREIGN KEY (`fk_sources`) REFERENCES `data_source_aggregate` (`id_data_sources`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_source_instance`
--

LOCK TABLES `data_source_instance` WRITE;
/*!40000 ALTER TABLE `data_source_instance` DISABLE KEYS */;
INSERT INTO `data_source_instance` VALUES (1,'2018-09-19 14:19:51','2018-09-19 14:19:51',0,'ao3_academia','ao3_academia#null#path','academia','OTHER',1),(2,'2018-09-19 14:19:51','2018-09-19 14:19:51',0,'ao3_academia','ao3_academia#null#path','academia/Who Authorized This?','OTHER',2),(3,'2018-09-19 14:19:51','2018-09-19 14:19:51',0,'ao3_academia','ao3_academia#null#path','academia/Who Authorized This?/Chapter 1','OTHER',3),(4,'2018-09-19 14:19:51','2018-09-19 14:19:51',0,'ao3_academia','ao3_academia#id#username','13762404_0001_00001','OTHER',4),(5,'2018-09-19 14:19:51','2018-09-19 14:19:51',0,'ao3_academia','ao3_academia#id#contribution','13762404_0001_00001','OTHER',5),(6,'2018-09-19 14:19:51','2018-09-19 14:19:51',0,'ao3_academia','ao3_academia#id#post','13762404_0001_00001','OTHER',6),(7,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'ao3_academia','ao3_academia#id#username','13762404_0001_00002','OTHER',4),(8,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'ao3_academia','ao3_academia#id#contribution','13762404_0001_00002','OTHER',7),(9,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'ao3_academia','ao3_academia#id#post','13762404_0001_00002','OTHER',8),(10,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'ao3_academia','ao3_academia#id#username','13762404_0001_00003','OTHER',4),(11,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'ao3_academia','ao3_academia#id#contribution','13762404_0001_00003','OTHER',9),(12,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'ao3_academia','ao3_academia#id#post','13762404_0001_00003','OTHER',10),(13,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'ao3_academia','ao3_academia#null#path','academia/Who Authorized This?/Chapter 2','OTHER',11),(14,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'ao3_academia','ao3_academia#id#username','13762404_0002_00001','OTHER',4),(15,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'ao3_academia','ao3_academia#id#contribution','13762404_0002_00001','OTHER',12),(16,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'ao3_academia','ao3_academia#id#post','13762404_0002_00001','OTHER',13),(17,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'ao3_academia','ao3_academia#id#username','13762404_0002_00002','OTHER',4),(18,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'ao3_academia','ao3_academia#id#contribution','13762404_0002_00002','OTHER',14),(19,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'ao3_academia','ao3_academia#id#post','13762404_0002_00002','OTHER',15),(20,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,'ao3_academia','ao3_academia#null#path','academia/Who Authorized This?/Chapter 3','OTHER',16),(21,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,'ao3_academia','ao3_academia#id#username','13762404_0003_00001','OTHER',4),(22,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,'ao3_academia','ao3_academia#id#contribution','13762404_0003_00001','OTHER',17),(23,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,'ao3_academia','ao3_academia#id#post','13762404_0003_00001','OTHER',18),(24,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,'ao3_academia','ao3_academia#id#username','13762404_0003_00002','OTHER',4),(25,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,'ao3_academia','ao3_academia#id#contribution','13762404_0003_00002','OTHER',19),(26,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,'ao3_academia','ao3_academia#id#post','13762404_0003_00002','OTHER',20),(27,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,'ao3_academia','ao3_academia#id#username','13762404_0003_00003','OTHER',4),(28,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,'ao3_academia','ao3_academia#id#contribution','13762404_0003_00003','OTHER',21),(29,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,'ao3_academia','ao3_academia#id#post','13762404_0003_00003','OTHER',22);
/*!40000 ALTER TABLE `data_source_instance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discourse`
--

DROP TABLE IF EXISTS `discourse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discourse` (
  `id_discourse` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `name` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_discourse`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discourse`
--

LOCK TABLES `discourse` WRITE;
/*!40000 ALTER TABLE `discourse` DISABLE KEYS */;
INSERT INTO `discourse` VALUES (1,'2018-09-19 14:19:51','2018-09-19 14:19:51',0,'AO3 academia');
/*!40000 ALTER TABLE `discourse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discourse_has_discourse_part`
--

DROP TABLE IF EXISTS `discourse_has_discourse_part`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discourse_has_discourse_part` (
  `id_discourse_has_discourse_part` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `fk_discourse` bigint(20) DEFAULT NULL,
  `fk_discourse_part` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_discourse_has_discourse_part`),
  UNIQUE KEY `UK_d9fefbc7oph9pcv0ix55k3rek` (`fk_discourse`,`fk_discourse_part`),
  KEY `FK_atsffbpm9dgg89bygmxaubn8g` (`fk_discourse_part`),
  CONSTRAINT `FK_atsffbpm9dgg89bygmxaubn8g` FOREIGN KEY (`fk_discourse_part`) REFERENCES `discourse_part` (`id_discourse_part`),
  CONSTRAINT `FK_ia9s1ksk7tj2p0uuy21vxay99` FOREIGN KEY (`fk_discourse`) REFERENCES `discourse` (`id_discourse`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discourse_has_discourse_part`
--

LOCK TABLES `discourse_has_discourse_part` WRITE;
/*!40000 ALTER TABLE `discourse_has_discourse_part` DISABLE KEYS */;
INSERT INTO `discourse_has_discourse_part` VALUES (1,'2018-09-19 14:19:51','2018-09-19 14:19:51',0,NULL,NULL,NULL,1,1),(2,'2018-09-19 14:19:51','2018-09-19 14:19:51',0,NULL,NULL,NULL,1,2),(3,'2018-09-19 14:19:51','2018-09-19 14:19:51',0,NULL,NULL,NULL,1,3),(4,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,NULL,NULL,NULL,1,4),(5,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,NULL,NULL,NULL,1,5);
/*!40000 ALTER TABLE `discourse_has_discourse_part` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discourse_part`
--

DROP TABLE IF EXISTS `discourse_part`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discourse_part` (
  `id_discourse_part` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `name` text COLLATE utf8mb4_unicode_ci,
  `fk_annotation` bigint(20) DEFAULT NULL,
  `fk_data_sources` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_discourse_part`),
  KEY `FK_l8yv94ques80jxdi71tpc78rq` (`fk_annotation`),
  KEY `FK_7o0ge2prm0quxlsthk425hdi1` (`fk_data_sources`),
  CONSTRAINT `FK_7o0ge2prm0quxlsthk425hdi1` FOREIGN KEY (`fk_data_sources`) REFERENCES `data_source_aggregate` (`id_data_sources`),
  CONSTRAINT `FK_l8yv94ques80jxdi71tpc78rq` FOREIGN KEY (`fk_annotation`) REFERENCES `annotation_entity_proxy` (`id_annotation_entity_proxy`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discourse_part`
--

LOCK TABLES `discourse_part` WRITE;
/*!40000 ALTER TABLE `discourse_part` DISABLE KEYS */;
INSERT INTO `discourse_part` VALUES (1,'2018-09-19 14:19:51','2018-09-19 14:19:51',2,'FORUM',NULL,NULL,'academia',NULL,1),(2,'2018-09-19 14:19:51','2018-09-19 14:19:51',2,'DOCUMENT',NULL,NULL,'Who Authorized This?',NULL,2),(3,'2018-09-19 14:19:51','2018-09-19 14:19:51',2,'PARAGRAPH',NULL,NULL,'Chapter 1',NULL,3),(4,'2018-09-19 14:19:52','2018-09-19 14:19:52',2,'PARAGRAPH',NULL,NULL,'Chapter 2',NULL,11),(5,'2018-09-19 14:20:08','2018-09-19 14:20:08',2,'PARAGRAPH',NULL,NULL,'Chapter 3',NULL,16);
/*!40000 ALTER TABLE `discourse_part` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discourse_part_interaction`
--

DROP TABLE IF EXISTS `discourse_part_interaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discourse_part_interaction` (
  `id_content_interaction` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `fk_annotation` bigint(20) DEFAULT NULL,
  `fk_discourse_part` bigint(20) DEFAULT NULL,
  `fk_user` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_content_interaction`),
  KEY `FK_qr1mcd9n48dfmyqr0qsv5xjme` (`fk_annotation`),
  KEY `FK_gnib12j7fb2qcb5f8lwrjrofe` (`fk_discourse_part`),
  KEY `FK_9gqkkhbdtnadqilsebi5th25p` (`fk_user`),
  CONSTRAINT `FK_9gqkkhbdtnadqilsebi5th25p` FOREIGN KEY (`fk_user`) REFERENCES `user` (`id_user`),
  CONSTRAINT `FK_gnib12j7fb2qcb5f8lwrjrofe` FOREIGN KEY (`fk_discourse_part`) REFERENCES `discourse_part` (`id_discourse_part`),
  CONSTRAINT `FK_qr1mcd9n48dfmyqr0qsv5xjme` FOREIGN KEY (`fk_annotation`) REFERENCES `annotation_entity_proxy` (`id_annotation_entity_proxy`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discourse_part_interaction`
--

LOCK TABLES `discourse_part_interaction` WRITE;
/*!40000 ALTER TABLE `discourse_part_interaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `discourse_part_interaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discourse_part_relation`
--

DROP TABLE IF EXISTS `discourse_part_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discourse_part_relation` (
  `id_discourse_part_relation` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `fk_source` bigint(20) DEFAULT NULL,
  `fk_target` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_discourse_part_relation`),
  KEY `FK_8vuu3te66eirwrybllamff79e` (`fk_source`),
  KEY `FK_1lm40u1xcf4c5mus56ua3j63e` (`fk_target`),
  CONSTRAINT `FK_1lm40u1xcf4c5mus56ua3j63e` FOREIGN KEY (`fk_target`) REFERENCES `discourse_part` (`id_discourse_part`),
  CONSTRAINT `FK_8vuu3te66eirwrybllamff79e` FOREIGN KEY (`fk_source`) REFERENCES `discourse_part` (`id_discourse_part`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discourse_part_relation`
--

LOCK TABLES `discourse_part_relation` WRITE;
/*!40000 ALTER TABLE `discourse_part_relation` DISABLE KEYS */;
INSERT INTO `discourse_part_relation` VALUES (1,'2018-09-19 14:19:51','2018-09-19 14:19:51',0,'SUBPART',NULL,NULL,1,2),(2,'2018-09-19 14:19:51','2018-09-19 14:19:51',0,'SUBPART',NULL,NULL,2,3),(3,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'SUBPART',NULL,NULL,2,4),(4,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,'SUBPART',NULL,NULL,2,5);
/*!40000 ALTER TABLE `discourse_part_relation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discourse_relation`
--

DROP TABLE IF EXISTS `discourse_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discourse_relation` (
  `id_discourse_relation` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `fk_annotation` bigint(20) DEFAULT NULL,
  `fk_source` bigint(20) DEFAULT NULL,
  `fk_target` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_discourse_relation`),
  KEY `FK_hf0onm6pd2w2r9gll8pm2lq23` (`fk_annotation`),
  KEY `FK_rjj0de6qye0qnkikka2xbl2rx` (`fk_source`),
  KEY `FK_ryrsu7h5bxjxirqs4hxh4n7x2` (`fk_target`),
  CONSTRAINT `FK_hf0onm6pd2w2r9gll8pm2lq23` FOREIGN KEY (`fk_annotation`) REFERENCES `annotation_entity_proxy` (`id_annotation_entity_proxy`),
  CONSTRAINT `FK_rjj0de6qye0qnkikka2xbl2rx` FOREIGN KEY (`fk_source`) REFERENCES `contribution` (`id_contribution`),
  CONSTRAINT `FK_ryrsu7h5bxjxirqs4hxh4n7x2` FOREIGN KEY (`fk_target`) REFERENCES `contribution` (`id_contribution`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discourse_relation`
--

LOCK TABLES `discourse_relation` WRITE;
/*!40000 ALTER TABLE `discourse_relation` DISABLE KEYS */;
INSERT INTO `discourse_relation` VALUES (1,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'REPLY',NULL,NULL,NULL,2,1),(2,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'REPLY',NULL,NULL,NULL,3,2),(3,'2018-09-19 14:19:52','2018-09-19 14:19:52',0,'REPLY',NULL,NULL,NULL,5,4),(4,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,'REPLY',NULL,NULL,NULL,7,6),(5,'2018-09-19 14:20:08','2018-09-19 14:20:08',0,'REPLY',NULL,NULL,NULL,8,7);
/*!40000 ALTER TABLE `discourse_relation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discoursedb`
--

DROP TABLE IF EXISTS `discoursedb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discoursedb` (
  `id_discoursedb` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `schema_version` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fk_annotation` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_discoursedb`),
  KEY `FK_aaquam9a3w77xhoxh0ym1tpmu` (`fk_annotation`),
  CONSTRAINT `FK_aaquam9a3w77xhoxh0ym1tpmu` FOREIGN KEY (`fk_annotation`) REFERENCES `annotation_entity_proxy` (`id_annotation_entity_proxy`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discoursedb`
--

LOCK TABLES `discoursedb` WRITE;
/*!40000 ALTER TABLE `discoursedb` DISABLE KEYS */;
/*!40000 ALTER TABLE `discoursedb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feature`
--

DROP TABLE IF EXISTS `feature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feature` (
  `id_feature` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `value` text COLLATE utf8mb4_unicode_ci,
  `fk_annotation_instance` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_feature`),
  KEY `FK_ho2dcy7jlerhf9417yjvpfguq` (`fk_annotation_instance`),
  CONSTRAINT `FK_ho2dcy7jlerhf9417yjvpfguq` FOREIGN KEY (`fk_annotation_instance`) REFERENCES `annotation_instance` (`id_annotation_instance`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feature`
--

LOCK TABLES `feature` WRITE;
/*!40000 ALTER TABLE `feature` DISABLE KEYS */;
INSERT INTO `feature` VALUES (1,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,NULL,'<a href=\"https://archiveofourown.org/works/13762404\">original</a>',1),(2,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,NULL,'[\"Teen And Up Audiences\"]',2),(3,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,NULL,'[]',3),(4,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,NULL,'[\"\\u50d5\\u306e\\u30d2\\u30fc\\u30ed\\u30fc\\u30a2\\u30ab\\u30c7\\u30df\\u30a2 | Boku no Hero Academia | My Hero Academia\"]',4),(5,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,NULL,'[\"Bakugou Katsuki/Todoroki Shouto\", \"Bakugou Katsuki/Shinsou Hitoshi\", \"Ashido Mina/Kaminari Denki/Sero Hanta\", \"Kirishima Eijirou/Midoriya Izuku\", \"Jirou Kyouka/Yaoyorozu Momo\", \"Asui Tsuyu/Uraraka Ochako\", \"Bakugou Katsuki & Uraraka Ochako\", \"Bakugou Katsuki/Shinsou Hitoshi/Todoroki Shouto\", \"maybe more\", \"Aizawa Shouta | Eraserhead/Yamada Hizashi | Present Mic\", \"Dabi/Hawks (My Hero Academia)\"]',5),(6,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,NULL,'[\"Bakugou Katsuki\", \"Todoroki Shouto\", \"Uraraka Ochako\", \"Kirishima Eijirou\", \"Midoriya Izuku\", \"Iida Tenya\", \"Ashido Mina\", \"Kaminari Denki\", \"Asui Tsuyu\", \"Shinsou Hitoshi\", \"Sero Hanta\", \"Jirou Kyouka\", \"Yaoyorozu Momo\", \"Hagakure Tooru\", \"Yamada Hizashi | Present Mic\", \"Kayama Nemuri | Midnight\", \"Aizawa Shouta | Eraserhead\", \"Hawks (My Hero Academia)\", \"Dabi (My Hero Academia)\"]',6),(7,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,NULL,'[\"Bakugou Katsuki Swears A Lot\", \"This is just a mess\", \"I Am Too Lazy To List Every Character\"]',7),(8,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,NULL,'Updated',8),(9,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,NULL,'264',9),(10,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,NULL,'1037',10),(11,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,NULL,'161',11),(12,'2018-09-19 14:19:51','2018-09-19 14:19:52',1,NULL,'17340',12),(13,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'<a href=\"https://archiveofourown.org/works/13762404\">original</a>',13),(14,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Teen And Up Audiences\"]',14),(15,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[]',15),(16,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"\\u50d5\\u306e\\u30d2\\u30fc\\u30ed\\u30fc\\u30a2\\u30ab\\u30c7\\u30df\\u30a2 | Boku no Hero Academia | My Hero Academia\"]',16),(17,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Bakugou Katsuki/Todoroki Shouto\", \"Bakugou Katsuki/Shinsou Hitoshi\", \"Ashido Mina/Kaminari Denki/Sero Hanta\", \"Kirishima Eijirou/Midoriya Izuku\", \"Jirou Kyouka/Yaoyorozu Momo\", \"Asui Tsuyu/Uraraka Ochako\", \"Bakugou Katsuki & Uraraka Ochako\", \"Bakugou Katsuki/Shinsou Hitoshi/Todoroki Shouto\", \"maybe more\", \"Aizawa Shouta | Eraserhead/Yamada Hizashi | Present Mic\", \"Dabi/Hawks (My Hero Academia)\"]',17),(18,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Bakugou Katsuki\", \"Todoroki Shouto\", \"Uraraka Ochako\", \"Kirishima Eijirou\", \"Midoriya Izuku\", \"Iida Tenya\", \"Ashido Mina\", \"Kaminari Denki\", \"Asui Tsuyu\", \"Shinsou Hitoshi\", \"Sero Hanta\", \"Jirou Kyouka\", \"Yaoyorozu Momo\", \"Hagakure Tooru\", \"Yamada Hizashi | Present Mic\", \"Kayama Nemuri | Midnight\", \"Aizawa Shouta | Eraserhead\", \"Hawks (My Hero Academia)\", \"Dabi (My Hero Academia)\"]',18),(19,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Bakugou Katsuki Swears A Lot\", \"This is just a mess\", \"I Am Too Lazy To List Every Character\"]',19),(20,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'Updated',20),(21,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'264',21),(22,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'1037',22),(23,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'161',23),(24,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'17340',24),(25,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'<a href=\"https://archiveofourown.org/works/13762404\">original</a>',25),(26,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Teen And Up Audiences\"]',26),(27,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[]',27),(28,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"\\u50d5\\u306e\\u30d2\\u30fc\\u30ed\\u30fc\\u30a2\\u30ab\\u30c7\\u30df\\u30a2 | Boku no Hero Academia | My Hero Academia\"]',28),(29,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Bakugou Katsuki/Todoroki Shouto\", \"Bakugou Katsuki/Shinsou Hitoshi\", \"Ashido Mina/Kaminari Denki/Sero Hanta\", \"Kirishima Eijirou/Midoriya Izuku\", \"Jirou Kyouka/Yaoyorozu Momo\", \"Asui Tsuyu/Uraraka Ochako\", \"Bakugou Katsuki & Uraraka Ochako\", \"Bakugou Katsuki/Shinsou Hitoshi/Todoroki Shouto\", \"maybe more\", \"Aizawa Shouta | Eraserhead/Yamada Hizashi | Present Mic\", \"Dabi/Hawks (My Hero Academia)\"]',29),(30,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Bakugou Katsuki\", \"Todoroki Shouto\", \"Uraraka Ochako\", \"Kirishima Eijirou\", \"Midoriya Izuku\", \"Iida Tenya\", \"Ashido Mina\", \"Kaminari Denki\", \"Asui Tsuyu\", \"Shinsou Hitoshi\", \"Sero Hanta\", \"Jirou Kyouka\", \"Yaoyorozu Momo\", \"Hagakure Tooru\", \"Yamada Hizashi | Present Mic\", \"Kayama Nemuri | Midnight\", \"Aizawa Shouta | Eraserhead\", \"Hawks (My Hero Academia)\", \"Dabi (My Hero Academia)\"]',30),(31,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Bakugou Katsuki Swears A Lot\", \"This is just a mess\", \"I Am Too Lazy To List Every Character\"]',31),(32,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'Updated',32),(33,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'264',33),(34,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'1037',34),(35,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'161',35),(36,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'17340',36),(37,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'<a href=\"https://archiveofourown.org/works/13762404\">original</a>',37),(38,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Teen And Up Audiences\"]',38),(39,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[]',39),(40,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"\\u50d5\\u306e\\u30d2\\u30fc\\u30ed\\u30fc\\u30a2\\u30ab\\u30c7\\u30df\\u30a2 | Boku no Hero Academia | My Hero Academia\"]',40),(41,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Bakugou Katsuki/Todoroki Shouto\", \"Bakugou Katsuki/Shinsou Hitoshi\", \"Ashido Mina/Kaminari Denki/Sero Hanta\", \"Kirishima Eijirou/Midoriya Izuku\", \"Jirou Kyouka/Yaoyorozu Momo\", \"Asui Tsuyu/Uraraka Ochako\", \"Bakugou Katsuki & Uraraka Ochako\", \"Bakugou Katsuki/Shinsou Hitoshi/Todoroki Shouto\", \"maybe more\", \"Aizawa Shouta | Eraserhead/Yamada Hizashi | Present Mic\", \"Dabi/Hawks (My Hero Academia)\"]',41),(42,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Bakugou Katsuki\", \"Todoroki Shouto\", \"Uraraka Ochako\", \"Kirishima Eijirou\", \"Midoriya Izuku\", \"Iida Tenya\", \"Ashido Mina\", \"Kaminari Denki\", \"Asui Tsuyu\", \"Shinsou Hitoshi\", \"Sero Hanta\", \"Jirou Kyouka\", \"Yaoyorozu Momo\", \"Hagakure Tooru\", \"Yamada Hizashi | Present Mic\", \"Kayama Nemuri | Midnight\", \"Aizawa Shouta | Eraserhead\", \"Hawks (My Hero Academia)\", \"Dabi (My Hero Academia)\"]',42),(43,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Bakugou Katsuki Swears A Lot\", \"This is just a mess\", \"I Am Too Lazy To List Every Character\"]',43),(44,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'Updated',44),(45,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'264',45),(46,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'1037',46),(47,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'161',47),(48,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'17340',48),(49,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'<a href=\"https://archiveofourown.org/works/13762404\">original</a>',49),(50,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Teen And Up Audiences\"]',50),(51,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[]',51),(52,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"\\u50d5\\u306e\\u30d2\\u30fc\\u30ed\\u30fc\\u30a2\\u30ab\\u30c7\\u30df\\u30a2 | Boku no Hero Academia | My Hero Academia\"]',52),(53,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Bakugou Katsuki/Todoroki Shouto\", \"Bakugou Katsuki/Shinsou Hitoshi\", \"Ashido Mina/Kaminari Denki/Sero Hanta\", \"Kirishima Eijirou/Midoriya Izuku\", \"Jirou Kyouka/Yaoyorozu Momo\", \"Asui Tsuyu/Uraraka Ochako\", \"Bakugou Katsuki & Uraraka Ochako\", \"Bakugou Katsuki/Shinsou Hitoshi/Todoroki Shouto\", \"maybe more\", \"Aizawa Shouta | Eraserhead/Yamada Hizashi | Present Mic\", \"Dabi/Hawks (My Hero Academia)\"]',53),(54,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Bakugou Katsuki\", \"Todoroki Shouto\", \"Uraraka Ochako\", \"Kirishima Eijirou\", \"Midoriya Izuku\", \"Iida Tenya\", \"Ashido Mina\", \"Kaminari Denki\", \"Asui Tsuyu\", \"Shinsou Hitoshi\", \"Sero Hanta\", \"Jirou Kyouka\", \"Yaoyorozu Momo\", \"Hagakure Tooru\", \"Yamada Hizashi | Present Mic\", \"Kayama Nemuri | Midnight\", \"Aizawa Shouta | Eraserhead\", \"Hawks (My Hero Academia)\", \"Dabi (My Hero Academia)\"]',54),(55,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'[\"Bakugou Katsuki Swears A Lot\", \"This is just a mess\", \"I Am Too Lazy To List Every Character\"]',55),(56,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'Updated',56),(57,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'264',57),(58,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'1037',58),(59,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'161',59),(60,'2018-09-19 14:19:52','2018-09-19 14:19:52',1,NULL,'17340',60),(61,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'<a href=\"https://archiveofourown.org/works/13762404\">original</a>',61),(62,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[\"Teen And Up Audiences\"]',62),(63,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[]',63),(64,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[\"\\u50d5\\u306e\\u30d2\\u30fc\\u30ed\\u30fc\\u30a2\\u30ab\\u30c7\\u30df\\u30a2 | Boku no Hero Academia | My Hero Academia\"]',64),(65,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[\"Bakugou Katsuki/Todoroki Shouto\", \"Bakugou Katsuki/Shinsou Hitoshi\", \"Ashido Mina/Kaminari Denki/Sero Hanta\", \"Kirishima Eijirou/Midoriya Izuku\", \"Jirou Kyouka/Yaoyorozu Momo\", \"Asui Tsuyu/Uraraka Ochako\", \"Bakugou Katsuki & Uraraka Ochako\", \"Bakugou Katsuki/Shinsou Hitoshi/Todoroki Shouto\", \"maybe more\", \"Aizawa Shouta | Eraserhead/Yamada Hizashi | Present Mic\", \"Dabi/Hawks (My Hero Academia)\"]',65),(66,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[\"Bakugou Katsuki\", \"Todoroki Shouto\", \"Uraraka Ochako\", \"Kirishima Eijirou\", \"Midoriya Izuku\", \"Iida Tenya\", \"Ashido Mina\", \"Kaminari Denki\", \"Asui Tsuyu\", \"Shinsou Hitoshi\", \"Sero Hanta\", \"Jirou Kyouka\", \"Yaoyorozu Momo\", \"Hagakure Tooru\", \"Yamada Hizashi | Present Mic\", \"Kayama Nemuri | Midnight\", \"Aizawa Shouta | Eraserhead\", \"Hawks (My Hero Academia)\", \"Dabi (My Hero Academia)\"]',66),(67,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[\"Bakugou Katsuki Swears A Lot\", \"This is just a mess\", \"I Am Too Lazy To List Every Character\"]',67),(68,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'Updated',68),(69,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'264',69),(70,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'1037',70),(71,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'161',71),(72,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'17340',72),(73,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'<a href=\"https://archiveofourown.org/works/13762404\">original</a>',73),(74,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[\"Teen And Up Audiences\"]',74),(75,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[]',75),(76,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[\"\\u50d5\\u306e\\u30d2\\u30fc\\u30ed\\u30fc\\u30a2\\u30ab\\u30c7\\u30df\\u30a2 | Boku no Hero Academia | My Hero Academia\"]',76),(77,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[\"Bakugou Katsuki/Todoroki Shouto\", \"Bakugou Katsuki/Shinsou Hitoshi\", \"Ashido Mina/Kaminari Denki/Sero Hanta\", \"Kirishima Eijirou/Midoriya Izuku\", \"Jirou Kyouka/Yaoyorozu Momo\", \"Asui Tsuyu/Uraraka Ochako\", \"Bakugou Katsuki & Uraraka Ochako\", \"Bakugou Katsuki/Shinsou Hitoshi/Todoroki Shouto\", \"maybe more\", \"Aizawa Shouta | Eraserhead/Yamada Hizashi | Present Mic\", \"Dabi/Hawks (My Hero Academia)\"]',77),(78,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[\"Bakugou Katsuki\", \"Todoroki Shouto\", \"Uraraka Ochako\", \"Kirishima Eijirou\", \"Midoriya Izuku\", \"Iida Tenya\", \"Ashido Mina\", \"Kaminari Denki\", \"Asui Tsuyu\", \"Shinsou Hitoshi\", \"Sero Hanta\", \"Jirou Kyouka\", \"Yaoyorozu Momo\", \"Hagakure Tooru\", \"Yamada Hizashi | Present Mic\", \"Kayama Nemuri | Midnight\", \"Aizawa Shouta | Eraserhead\", \"Hawks (My Hero Academia)\", \"Dabi (My Hero Academia)\"]',78),(79,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[\"Bakugou Katsuki Swears A Lot\", \"This is just a mess\", \"I Am Too Lazy To List Every Character\"]',79),(80,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'Updated',80),(81,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'264',81),(82,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'1037',82),(83,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'161',83),(84,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'17340',84),(85,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'<a href=\"https://archiveofourown.org/works/13762404\">original</a>',85),(86,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[\"Teen And Up Audiences\"]',86),(87,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[]',87),(88,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[\"\\u50d5\\u306e\\u30d2\\u30fc\\u30ed\\u30fc\\u30a2\\u30ab\\u30c7\\u30df\\u30a2 | Boku no Hero Academia | My Hero Academia\"]',88),(89,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[\"Bakugou Katsuki/Todoroki Shouto\", \"Bakugou Katsuki/Shinsou Hitoshi\", \"Ashido Mina/Kaminari Denki/Sero Hanta\", \"Kirishima Eijirou/Midoriya Izuku\", \"Jirou Kyouka/Yaoyorozu Momo\", \"Asui Tsuyu/Uraraka Ochako\", \"Bakugou Katsuki & Uraraka Ochako\", \"Bakugou Katsuki/Shinsou Hitoshi/Todoroki Shouto\", \"maybe more\", \"Aizawa Shouta | Eraserhead/Yamada Hizashi | Present Mic\", \"Dabi/Hawks (My Hero Academia)\"]',89),(90,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[\"Bakugou Katsuki\", \"Todoroki Shouto\", \"Uraraka Ochako\", \"Kirishima Eijirou\", \"Midoriya Izuku\", \"Iida Tenya\", \"Ashido Mina\", \"Kaminari Denki\", \"Asui Tsuyu\", \"Shinsou Hitoshi\", \"Sero Hanta\", \"Jirou Kyouka\", \"Yaoyorozu Momo\", \"Hagakure Tooru\", \"Yamada Hizashi | Present Mic\", \"Kayama Nemuri | Midnight\", \"Aizawa Shouta | Eraserhead\", \"Hawks (My Hero Academia)\", \"Dabi (My Hero Academia)\"]',90),(91,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'[\"Bakugou Katsuki Swears A Lot\", \"This is just a mess\", \"I Am Too Lazy To List Every Character\"]',91),(92,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'Updated',92),(93,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'264',93),(94,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'1037',94),(95,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'161',95),(96,'2018-09-19 14:20:08','2018-09-19 14:20:08',1,NULL,'17340',96);
/*!40000 ALTER TABLE `feature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group`
--

DROP TABLE IF EXISTS `group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `group` (
  `id_group` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `name` text COLLATE utf8mb4_unicode_ci,
  `fk_annotation` bigint(20) DEFAULT NULL,
  `fk_data_sources` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_group`),
  KEY `FK_2s7d17725094uyy4oddvxbjqi` (`fk_annotation`),
  KEY `FK_50012om58qj8vxyqhpeq794uq` (`fk_data_sources`),
  CONSTRAINT `FK_2s7d17725094uyy4oddvxbjqi` FOREIGN KEY (`fk_annotation`) REFERENCES `annotation_entity_proxy` (`id_annotation_entity_proxy`),
  CONSTRAINT `FK_50012om58qj8vxyqhpeq794uq` FOREIGN KEY (`fk_data_sources`) REFERENCES `data_source_aggregate` (`id_data_sources`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group`
--

LOCK TABLES `group` WRITE;
/*!40000 ALTER TABLE `group` DISABLE KEYS */;
/*!40000 ALTER TABLE `group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id_user` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `country` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ip` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `language` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `location` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `realname` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `username` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fk_annotation` bigint(20) DEFAULT NULL,
  `fk_data_sources` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_user`),
  KEY `userNameIndex` (`username`),
  KEY `FK_in0cnnkh7f32e5jl8aq7vf4kv` (`fk_annotation`),
  KEY `FK_xss8wv8gkqcwq7d6en5nhrhm` (`fk_data_sources`),
  CONSTRAINT `FK_in0cnnkh7f32e5jl8aq7vf4kv` FOREIGN KEY (`fk_annotation`) REFERENCES `annotation_entity_proxy` (`id_annotation_entity_proxy`),
  CONSTRAINT `FK_xss8wv8gkqcwq7d6en5nhrhm` FOREIGN KEY (`fk_data_sources`) REFERENCES `data_source_aggregate` (`id_data_sources`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'2018-09-19 14:19:51','2018-09-19 14:19:51',1,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,'madhadler',NULL,4);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_memberof_discourse`
--

DROP TABLE IF EXISTS `user_memberof_discourse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_memberof_discourse` (
  `id_user` bigint(20) NOT NULL,
  `id_discourse` bigint(20) NOT NULL,
  PRIMARY KEY (`id_user`,`id_discourse`),
  KEY `FK_of7lgtf2l4fies0abapw01tgb` (`id_discourse`),
  CONSTRAINT `FK_of7lgtf2l4fies0abapw01tgb` FOREIGN KEY (`id_discourse`) REFERENCES `discourse` (`id_discourse`),
  CONSTRAINT `FK_pqvgq9dlouba1m2kg5jwivieh` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_memberof_discourse`
--

LOCK TABLES `user_memberof_discourse` WRITE;
/*!40000 ALTER TABLE `user_memberof_discourse` DISABLE KEYS */;
INSERT INTO `user_memberof_discourse` VALUES (1,1);
/*!40000 ALTER TABLE `user_memberof_discourse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_memberof_group`
--

DROP TABLE IF EXISTS `user_memberof_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_memberof_group` (
  `id_group_user` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `fk_group` bigint(20) DEFAULT NULL,
  `fk_user` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_group_user`),
  UNIQUE KEY `UK_purdv175c1xu9orge3vrc7wnr` (`fk_group`,`fk_user`),
  KEY `FK_nn20lirmfpa3ceh4pl27nn33d` (`fk_user`),
  CONSTRAINT `FK_1kcbdo089ng772hoj98nsplnw` FOREIGN KEY (`fk_group`) REFERENCES `group` (`id_group`),
  CONSTRAINT `FK_nn20lirmfpa3ceh4pl27nn33d` FOREIGN KEY (`fk_user`) REFERENCES `user` (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_memberof_group`
--

LOCK TABLES `user_memberof_group` WRITE;
/*!40000 ALTER TABLE `user_memberof_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_memberof_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_relation`
--

DROP TABLE IF EXISTS `user_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_relation` (
  `id_user_relation` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `fk_annotation` bigint(20) DEFAULT NULL,
  `fk_source` bigint(20) DEFAULT NULL,
  `fk_target` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_user_relation`),
  KEY `FK_lkw6pumj9iw7nlh0q94inetp4` (`fk_annotation`),
  KEY `FK_t0ep88u5euorirn8c37qdq4au` (`fk_source`),
  KEY `FK_d9i97thxamwxhpr18td4eg6ua` (`fk_target`),
  CONSTRAINT `FK_d9i97thxamwxhpr18td4eg6ua` FOREIGN KEY (`fk_target`) REFERENCES `user` (`id_user`),
  CONSTRAINT `FK_lkw6pumj9iw7nlh0q94inetp4` FOREIGN KEY (`fk_annotation`) REFERENCES `annotation_entity_proxy` (`id_annotation_entity_proxy`),
  CONSTRAINT `FK_t0ep88u5euorirn8c37qdq4au` FOREIGN KEY (`fk_source`) REFERENCES `user` (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_relation`
--

LOCK TABLES `user_relation` WRITE;
/*!40000 ALTER TABLE `user_relation` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_relation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-19 14:20:21
