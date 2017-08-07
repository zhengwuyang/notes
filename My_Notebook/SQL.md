```
CREATE TEMP TABLE dept_bsr_map AS
SELECT 
    n.dept_id,
    b.id bsr_id,
    b.name
FROM amz_us_list_node n 
LEFT JOIN amz_us_bestsellers_node b 
ON 
    n.name=b.name 
WHERE 
    n.node_id='0' 
    AND 
    b._ancestor_ids='__root__' 
ORDER BY 
    n.dept_id;

SELECT DISTINCT ON (bsr_id, user_id) * FROM (
    SELECT
        user_id,
        (s.dept_id, s.node_id, s.parent_node_id) node_ident,
        COALESCE(dept_bsr_map.bsr_id, b.id) bsr_id,
        COALESCE(dept_bsr_map.name, b.name) node_name

    FROM amz_us_user_growing_bs s
    LEFT JOIN dept_bsr_map ON s.node_id = '0' AND s.dept_id = dept_bsr_map.dept_id
    LEFT JOIN (SELECT DISTINCT ON (node_id) * FROM amz_us_bestsellers_node) b ON s.node_id <> '0' AND s.node_id = b.node_id
) t
WHERE bsr_id IS NOT NULL
ORDER BY bsr_id, user_id;
```

psql导出数据表
`pg_dump -t <table> -f <sql_file> <db_name>`
psql导出数据库
`pg_dump <db_name> > <sql_file>`