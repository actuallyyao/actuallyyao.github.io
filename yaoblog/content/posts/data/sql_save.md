---
title: "Useful SQL"
date: 2022-10-14T21:44:51+08:00
draft: true
hiddenInHomeList: true
tags: ['SQL', 'Data']
ShowWordCount: true
# cover:
#   image: "/posts/data/learn_data/data.jpg"
#   # can also paste direct link from external site
#   # ex. https://i.ibb.co/K0HVPBd/paper-mod-profilemode.png
# #   alt: "<alt text>"
# #   caption: "<text>"
# #   relative: false # To use relative path for cover image, used in hugo Page-bundles
---



### Window Function

先分举报量分层取各个举报原因对应的举报次数，然后通过开窗函数取每个举报量分层中举报次数排第一的举报原因

```sql
SELECT
    DISTINCT report_cnt_range,
    report_reason_name,
    report_cnt,
    ROW_NUMBER () OVER (
        PARTITION BY report_cnt_range
        ORDER BY
            report_cnt
    ) as rank
FROM
    (
        SELECT
            DISTINCT user_range.report_cnt_range as report_cnt_range,
            report_detail.report_reason_name as report_reason_name,
            COUNT (DISTINCT report_detail.object_id) as report_cnt
        FROM
            XXX
    )
WHERE
    rank = 1
```
### WR-A Sampling

Use log to retain precision

```sql
SELECT
    room_id,
    log(rand) *(1 /(vv / vv_all)) AS key
FROM
    (
        SELECT
            type,
            room_id,
            vv,
            sum(vv) OVER(partition by type) AS all_vv,
            rand() AS rand
        FROM
            (
                SELECT
                    'all' AS type,
                    room_id,
                    vv
                FROM
                    room_id_vv
            )
    )
ORDER BY
    key DESC
LIMIT
    100
```

### COLLECT_SET and SORT_ARRAY

如果需要array中的元素保持一定的顺序，可以使用`sort_array`函数来实现的：

`sort_array(Array<T> a)` 根据数组元素的自然顺序按升序对输入数组排序并返回它

`select sort_array(collect_set(col))`
