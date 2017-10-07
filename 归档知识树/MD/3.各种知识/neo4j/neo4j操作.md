删除清空neo4j数据库
match (n) detach delete n
创建唯一约束
CREATE CONSTRAINT ON (cc:Person)
ASSERT cc.name IS UNIQUE