import os

dbname = "sample"

class SqlTable(object):
    def __init__(self, dirname, dbname, seq, tablename, top):
        self.dirname = dirname
        self.dbname = dbname
        self.tablename = tablename
        self.top = """--
-- Table structure for table `%s`
--

DROP TABLE IF EXISTS `%s`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `%s` (""" % (self.tablename, self.tablename, self.tablename) + top + \
""") ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;"""

        self.insert_header = """--
-- Dumping data for table `%s`
--

LOCK TABLES `%s` WRITE;
/*!40000 ALTER TABLE `%s` DISABLE KEYS */;
INSERT INTO `%s` VALUES """ % (self.tablename, self.tablename, self.tablename, self.tablename)
        self.bottom =""";
/*!40000 ALTER TABLE `%s` ENABLE KEYS */;
UNLOCK TABLES;""" % (self.tablename,)
        self.comma = ""
        self.stage = "top"
        try: os.makedirs(self.dirname)
        except Exception, e: 
            pass
        self.fn = self.dirname + "/" + seq + "_" + tablename + ".sql"

    def append(self, stuff):
        with open(self.fn, "ab") as f:
            f.write(stuff)

    def write(self, stuff):
        with open(self.fn, "wb") as f:
            f.write(stuff)

    def open(self):
        assert self.stage == "top", "Table "+ self.tablename+ " written out of order; "+ self.stage+ "!= top"
        self.write(self.top)
        self.stage = "insert_head"
    def insert_head(self):
        assert self.stage == "insert_head", "Table "+ self.tablename+ " written out of order; "+ self.stage+ "!= insert_head"
        self.append(self.insert_header)
        self.stage = "insert_value"
    def insertion(self, values):
        if self.stage == "insert_head": self.insert_head()
        assert self.stage == "insert_value", "Table "+ self.tablename+ " written out of order; "+ self.stage+ "!= insert_value"
        self.append(self.comma + "(" + (",".join(values)) + ")")
        self.comma = ","
    def close(self):
        assert self.stage == "insert_head" or self.stage == "insert_value", \
               "Table "+ self.tablename+ " written out of order; "+ self.stage+ "!= top or head"
        self.append(self.bottom)
        self.stage = "done"

class Sqlout(object):
    def __init__(self, dirname, dbname):
        self.dirname = dirname
        self.dbname = dbname
        self.tables = {}
        try: os.makedirs(self.dirname)
        except: pass
        self.header()
        self.load_tables()
        for t in self.tables:
            self.tables[t].open()

    def insert_table(self, t, values):
        self.tables[t].insertion(values) 

    def close(self):
        for t in self.tables:
            self.tables[t].close()
        self.footer()

    def footer(self):
        with open(self.dirname + "/99_foot.sql","wb") as f:
            f.write("""
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed """)

    def header(self):
        with open(self.dirname + "/00_head.sql","wb") as f:
            f.write(
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
"""% (self.dbname,))

    def load_tables(self):
        self.tables["annotation_entity_proxy"] =  \
            SqlTable(self.dirname, self.dbname, "01", "annotation_entity_proxy", 
"""  `id_annotation_entity_proxy` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_annotation_entity_proxy`)
""")
        self.tables["annotation_instance"] =  \
            SqlTable(self.dirname, self.dbname, "02", "annotation_instance", 
"""
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
""")



        self.tables["annotation_relation"] = \
            SqlTable(self.dirname, self.dbname, "03", "annotation_relation", 
  """`id_annotation_relation` bigint(20) NOT NULL AUTO_INCREMENT,
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
""")

        self.tables["audience"] = \
            SqlTable(self.dirname, self.dbname, "04", "audience", 
""" `id_audience` bigint(20) NOT NULL AUTO_INCREMENT,
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
""")
        self.tables["audience_has_group"] = \
            SqlTable(self.dirname, self.dbname, "05", "audience_has_group", 
"""
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
""")
        self.tables["audience_has_user"] = \
            SqlTable(self.dirname, self.dbname, "06", "audience_has_user", 
"""
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
""")
        self.tables["content"] = \
            SqlTable(self.dirname, self.dbname, "07", "content", 
"""
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
""")
        self.tables["contribution"] = \
            SqlTable(self.dirname, self.dbname, "08", "contribution", 
  """`id_contribution` bigint(20) NOT NULL AUTO_INCREMENT,
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
""")
        self.tables["contribution_has_audience"] = \
            SqlTable(self.dirname, self.dbname, "09", "contribution_has_audience", 
"""
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
""")
        self.tables["contribution_has_context"] = \
            SqlTable(self.dirname, self.dbname, "10", "contribution_has_context", 
"""
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
""")
        self.tables["contribution_interaction"] = \
            SqlTable(self.dirname, self.dbname, "11", "contribution_interaction", 
"""
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
""")
        self.tables["contribution_partof_discourse_part"] = \
            SqlTable(self.dirname, self.dbname, "12", "contribution_partof_discourse_part", 
"""
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
""")
        self.tables["data_source_aggregate"] = \
            SqlTable(self.dirname, self.dbname, "13", "data_source_aggregate", 
"""
  `id_data_sources` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_data_sources`)
""")
        self.tables["data_source_instance"] = \
            SqlTable(self.dirname, self.dbname, "14", "data_source_instance", 
"""
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
""")
        self.tables["discourse"] = \
            SqlTable(self.dirname, self.dbname, "15", "discourse", 
"""
  `id_discourse` bigint(20) NOT NULL AUTO_INCREMENT,
  `entity_created` datetime DEFAULT NULL,
  `entity_modified` datetime DEFAULT NULL,
  `entity_version` bigint(20) DEFAULT NULL,
  `name` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_discourse`)
""")
        self.tables["discourse_has_discourse_part"] = \
            SqlTable(self.dirname, self.dbname, "16", "discourse_has_discourse_part", 
"""
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
""")
        self.tables["discourse_part"] = \
            SqlTable(self.dirname, self.dbname, "17", "discourse_part", 
"""
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
""")
        self.tables["discourse_part_interaction"] = \
            SqlTable(self.dirname, self.dbname, "18", "discourse_part_interaction", 
"""
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
""")
        self.tables["discourse_part_relation"] = \
            SqlTable(self.dirname, self.dbname, "19", "discourse_part_relation", 
"""
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
""")
        self.tables["discourse_relation"] = \
            SqlTable(self.dirname, self.dbname, "20", "discourse_relation", 
"""
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
""")
        self.tables["discoursedb"] = \
            SqlTable(self.dirname, self.dbname, "21", "discoursedb", 
"""
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
""")
        self.tables["feature"] = \
            SqlTable(self.dirname, self.dbname, "22", "feature", 
"""
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
""")
        self.tables["group"] = \
            SqlTable(self.dirname, self.dbname, "23", "group", 
"""
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
""")
        self.tables["user"] = \
            SqlTable(self.dirname, self.dbname, "24", "user", 
"""
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
""")
        self.tables["user_memberof_discourse"] = \
            SqlTable(self.dirname, self.dbname, "25", "user_memberof_discourse", 
"""
  `id_user` bigint(20) NOT NULL,
  `id_discourse` bigint(20) NOT NULL,
  PRIMARY KEY (`id_user`,`id_discourse`),
  KEY `FK_of7lgtf2l4fies0abapw01tgb` (`id_discourse`),
  CONSTRAINT `FK_of7lgtf2l4fies0abapw01tgb` FOREIGN KEY (`id_discourse`) REFERENCES `discourse` (`id_discourse`),
  CONSTRAINT `FK_pqvgq9dlouba1m2kg5jwivieh` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`)
""")
        self.tables["user_memberof_group"] = \
            SqlTable(self.dirname, self.dbname, "26", "user_memberof_group", 
"""
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
""")
        self.tables["user_relation"] = \
            SqlTable(self.dirname, self.dbname, "27", "user_relation", 
"""
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
""")
