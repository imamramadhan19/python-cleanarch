/*
 Navicat Premium Data Transfer

 Source Server         : blog
 Source Server Type    : PostgreSQL
 Source Server Version : 100300
 Source Host           : 127.0.0.1:5432
 Source Catalog        : blog
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 100300
 File Encoding         : 65001

 Date: 12/09/2018 14:31:19
*/


CREATE SEQUENCE posts_id_seq
   START WITH 1
   INCREMENT BY 1
   NO MINVALUE
   NO MAXVALUE
   CACHE 1;

-- ----------------------------
-- Table structure for articles
-- ----------------------------
DROP TABLE IF EXISTS "articles";
CREATE TABLE "articles" (
  "id" int4 NOT NULL DEFAULT nextval('posts_id_seq'::regclass),
  "title" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "category_id" int2 DEFAULT NULL,
  "author_id" int2 DEFAULT NULL,
  "created_at" timestamp(0) DEFAULT NULL,
  "updated_at" timestamp(0) DEFAULT NULL,
  "content" text COLLATE "pg_catalog"."default" DEFAULT NULL,
  "is_active" bool DEFAULT NULL
)
;
ALTER TABLE "articles" OWNER TO "blog";

-- ----------------------------
-- Records of articles
-- ----------------------------
BEGIN;
INSERT INTO "articles" VALUES (72, 'Title blog', 1, 1, '2018-07-24 14:44:17', '2018-07-24 14:44:17', 'Content blog', 't');
INSERT INTO "articles" VALUES (103, 'TEST CREATE FROM API', 1, 1, '2018-07-24 15:58:10', '2018-07-24 15:58:10', 'CONTENT', 't');
INSERT INTO "articles" VALUES (104, 'TEST CREATE FROM API', 1, 1, '2018-07-24 15:58:27', '2018-07-24 15:58:27', 'CONTENT', 't');
INSERT INTO "articles" VALUES (105, 'TEST CREATE FROM API', 1, 1, '2018-07-24 15:59:24', '2018-07-24 15:59:24', 'CONTENT', 't');
INSERT INTO "articles" VALUES (106, 'TEST CREATE FROM API', 1, 1, '2018-07-24 16:02:00', '2018-07-24 16:02:00', 'CONTENT', 't');
INSERT INTO "articles" VALUES (107, 'TEST CREATE FROM API', 1, 1, '2018-07-24 16:06:25', '2018-07-24 16:06:25', 'CONTENT', 't');
INSERT INTO "articles" VALUES (108, 'TEST CREATE FROM API', 1, 1, '2018-07-24 16:07:40', '2018-07-24 16:07:40', 'CONTENT', 't');
INSERT INTO "articles" VALUES (1, 'Belajar bikin blog 1', 1, 1, '2018-07-19 00:00:00', '2018-07-19 00:00:00', 'Lorem ipsum doler si amet lorem ipsum doler', 't');
INSERT INTO "articles" VALUES (2, 'Belajar Devops 1', 2, 2, '2018-07-19 00:00:00', '2018-07-19 00:00:00', 'Lorem ipsum doler si amet lorem ipsum doler', 't');
INSERT INTO "articles" VALUES (3, 'Title blog', 1, 1, '2018-07-19 17:19:47', '2018-07-19 17:19:47', 'Content blog', NULL);
INSERT INTO "articles" VALUES (4, 'Title blog', 1, 1, '2018-07-19 17:19:51', '2018-07-19 17:19:51', 'Content blog', NULL);
INSERT INTO "articles" VALUES (5, 'Title blog', 1, 1, '2018-07-19 17:20:45', '2018-07-19 17:20:45', 'Content blog', NULL);
INSERT INTO "articles" VALUES (6, 'Title blog', 1, 1, '2018-07-19 17:23:02', '2018-07-19 17:23:02', 'Content blog', 't');
INSERT INTO "articles" VALUES (7, 'Title blog', 1, 1, '2018-07-19 17:23:09', '2018-07-19 17:23:09', 'Content blog', 't');
INSERT INTO "articles" VALUES (8, 'Title blog', 1, 1, '2018-07-24 11:36:57', '2018-07-24 11:36:57', 'Content blog', 't');
INSERT INTO "articles" VALUES (9, 'Title blog Update', 1, 1, '2018-07-24 11:36:57', '2018-07-24 11:36:57', 'Content blog', 't');
INSERT INTO "articles" VALUES (11, 'Title blog Update', 1, 1, '2018-07-24 11:40:25', '2018-07-24 11:40:25', 'Content blog', 't');
INSERT INTO "articles" VALUES (12, 'Title blog', 1, 1, '2018-07-24 11:40:49', '2018-07-24 11:40:49', 'Content blog', 't');
INSERT INTO "articles" VALUES (13, 'Title blog Update', 1, 1, '2018-07-24 11:40:49', '2018-07-24 11:40:49', 'Content blog', 't');
INSERT INTO "articles" VALUES (15, 'Title blog Update', 1, 1, '2018-07-24 11:41:17', '2018-07-24 11:41:17', 'Content blog', 't');
INSERT INTO "articles" VALUES (17, 'Title blog Update', 1, 1, '2018-07-24 11:42:03', '2018-07-24 11:42:03', 'Content blog', 't');
INSERT INTO "articles" VALUES (19, 'Title blog Update 21', 1, 1, '2018-07-24 11:43:18', '2018-07-24 11:43:18', 'Content blog', 't');
INSERT INTO "articles" VALUES (24, 'Title blog Update 21', 1, 1, '2018-07-24 11:44:49', '2018-07-24 11:44:49', 'Content blog', 't');
INSERT INTO "articles" VALUES (26, 'Title blog Update 21', 1, 1, '2018-07-24 11:45:12', '2018-07-24 11:45:12', 'Content blog', 't');
INSERT INTO "articles" VALUES (28, 'Title blog Update 21', 1, 1, '2018-07-24 11:45:49', '2018-07-24 11:45:49', 'Content blog', 't');
INSERT INTO "articles" VALUES (99, 'TEST CREATE FROM API', 1, 1, '2018-07-24 15:56:06', '2018-07-24 15:56:06', 'CONTENT', 't');
INSERT INTO "articles" VALUES (100, 'TEST CREATE FROM API', 1, 1, '2018-07-24 15:56:50', '2018-07-24 15:56:50', 'CONTENT', 't');
INSERT INTO "articles" VALUES (102, 'TEST CREATE FROM API', 1, 1, '2018-07-24 15:57:23', '2018-07-24 15:57:23', 'CONTENT', 't');
COMMIT;

-- ----------------------------
-- Primary Key structure for table articles
-- ----------------------------
ALTER TABLE "articles" ADD CONSTRAINT "articles_pkey" PRIMARY KEY ("id");


/*
 Navicat Premium Data Transfer

 Source Server         : blog
 Source Server Type    : PostgreSQL
 Source Server Version : 100300
 Source Host           : 127.0.0.1:5432
 Source Catalog        : blog
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 100300
 File Encoding         : 65001

 Date: 12/09/2018 14:31:42
*/


-- ----------------------------
-- Table structure for authors
-- ----------------------------
DROP TABLE IF EXISTS "authors";
CREATE TABLE "authors" (
  "id" int4 NOT NULL DEFAULT NULL,
  "name" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "created_at" timestamp(0) DEFAULT NULL::timestamp without time zone,
  "updated_at" timestamp(0) DEFAULT NULL::timestamp without time zone,
  "email" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL
)
;
ALTER TABLE "authors" OWNER TO "blog";

-- ----------------------------
-- Records of authors
-- ----------------------------
BEGIN;
INSERT INTO "authors" VALUES (1, 'Jhon Lenon', '2018-07-19 00:00:00', '2018-07-19 00:00:00', 'jhon.lenon@email.com');
INSERT INTO "authors" VALUES (2, 'Uncle Bob', '2018-07-19 00:00:00', '2018-07-19 00:00:00', 'uncle.bob@email.com');
COMMIT;

-- ----------------------------
-- Primary Key structure for table authors
-- ----------------------------
ALTER TABLE "authors" ADD CONSTRAINT "categories_copy1_pkey" PRIMARY KEY ("id");


/*
 Navicat Premium Data Transfer

 Source Server         : blog
 Source Server Type    : PostgreSQL
 Source Server Version : 100300
 Source Host           : 127.0.0.1:5432
 Source Catalog        : blog
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 100300
 File Encoding         : 65001

 Date: 12/09/2018 14:31:53
*/


-- ----------------------------
-- Table structure for categories
-- ----------------------------
DROP TABLE IF EXISTS "categories";
CREATE TABLE "categories" (
  "id" int4 NOT NULL DEFAULT NULL,
  "title" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "updated_at" timestamp(0) DEFAULT NULL::timestamp without time zone,
  "created_at" timestamp(0) DEFAULT NULL
)
;
ALTER TABLE "categories" OWNER TO "blog";

-- ----------------------------
-- Records of categories
-- ----------------------------
BEGIN;
INSERT INTO "categories" VALUES (1, 'Programming', '2018-07-19 00:00:00', '2018-07-19 00:00:00');
INSERT INTO "categories" VALUES (2, 'DevOps', '2018-07-19 00:00:00', '2018-07-19 00:00:00');
COMMIT;

-- ----------------------------
-- Primary Key structure for table categories
-- ----------------------------
ALTER TABLE "categories" ADD CONSTRAINT "posts_copy1_pkey" PRIMARY KEY ("id");
