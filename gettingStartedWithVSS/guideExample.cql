CREATE TABLE vector_example.foo(
    i int primary key, 
    j float vector[3]
);


CREATE TABLE products (
  id UUID PRIMARY KEY,
  name varchar,
  description varchar,
  item_vector VECTOR<float, 3>
);

CREATE CUSTOM INDEX item_ann_index ON product(item_vector) USING 'VectorMemtableIndex';

SELECT * FROM product WHERE item_vector ANN OF [3.4, 7.8, 9.1];