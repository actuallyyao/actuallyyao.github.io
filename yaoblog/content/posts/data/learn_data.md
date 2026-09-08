---
title: "我是如何学习数据分析的"
date: 2022-12-30T21:44:51+08:00
draft: False
tags: ["SQL", "Data"]
ShowWordCount: true
# cover:
#   image: "/posts/data/learn_data/data.jpg"
#   # can also paste direct link from external site
#   # ex. https://i.ibb.co/K0HVPBd/paper-mod-profilemode.png
# #   alt: "<alt text>"
# #   caption: "<text>"
# #   relative: false # To use relative path for cover image, used in hugo Page-bundles
---

2019 年毕业进入互联网行业，虽然不是技术岗位，但日常的工作离不开数据。

随着工作年限的提升，工作对我数据能力的要求也在迅速上升。从一开始使用公司内部的 BI 平台做数据查询、日常观测<abbr title="Tableau约在2020年被前司淘汰，转而使用自研的BI平台">Tableau 看板</abbr>advanced level 的 SQL。

第一次接触 SQL 已经是工作之后，那时看到数据分析师的电脑屏幕上总是密密麻麻的代码，不仅觉得无比高端，同时也觉得与自己无关。

直到项目上需要取数 DA 排期排不上，才第一次想，需求也不复杂，要不自己试试。于是一边网上看教程（这里主要是[W3Cschool](https://www.w3cschool.cn/sql/)），一边看着之前 DA 给写过的 SQL 照猫画虎，终于写成了自己的第一个 SQL。原本觉得和自己无关的代码，突然可以自己写出来，还是很激动的，并且也并不觉得很难。从此，我便能自己写就自己写，不知不觉节省了不少等排期的功夫。

来到 2021 年，我逐渐觉得自己的 SQL 能力遇到了瓶颈，于是想找一找网课做系统性的学习。这里不记得如何找到了 [DataCamp](https://www.datacamp.com/)，它也是这篇博客的主角。

<!-- {{<friend name="DataCamp" url="https://app.datacamp.com/learn/skill-tracks/sql-fundamentals?version=2" logo="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/hq30ze9287y9ztkmcdhy" word="DataCamp offers interactive R, Python, Sheets, SQL and shell courses.">}} -->

这里不得不提 DataCamp 的 Tracks。网站针对你想要学习到的技能（Skill Tracks），或成为的角色（Career Tracks），把需要学习的课程按照一定顺序排列起来组成 Tracks，交给你一步一步学，实质其实就是课程的 list。当时的我想要系统学习 SQL，便 enroll 了名为[SQL Fundamentals](https://app.datacamp.com/learn/skill-tracks/sql-fundamentals?version=2)的 Skill Track。

我们先来看看这个 Track 的介绍：

> Gain the fundamental skills you need to interact with and query your data in SQL—a powerful language used by data-driven businesses large and small to explore and manipulate their data to extract meaningful insights.
>
> In this track, you'll learn the skills you need to level up your data skills and leave Excel behind you. Through hands-on exercises, you’ll discover how to quickly summarize, join tables, and use window functions and built-in PostgreSQL functions to analyze your data.

从介绍可知，这个 Track 主要针对 SQL 零基础入门，从包含课程也可以看到，基本囊括了一个 SQL 新手需要学习的所有 SQL 知识（不过课程使用的 PostgreSQL，我实际工作中用到的是 hiveSQL，所以会发现一些进阶的函数两者不匹配，但相似度还是很高的）：

-   Intermediate SQL Queries
-   SQL for Joining Data
-   Data Manipulation in SQL
-   Functions for Manipulating Date in PostgreSQL
