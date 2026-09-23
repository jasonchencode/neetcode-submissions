-- Write your query below

SELECT left_operand, operator, right_operand, CASE operator 
    WHEN '>' THEN (SELECT value FROM variables WHERE name=left_operand) > (SELECT value FROM variables WHERE name=right_operand) 
    WHEN '<' THEN (SELECT value FROM variables WHERE name=left_operand) < (SELECT value FROM variables WHERE name=right_operand) 
    ELSE (SELECT value FROM variables WHERE name=left_operand) = (SELECT value FROM variables WHERE name=right_operand) 
    END AS value
FROM expressions;
