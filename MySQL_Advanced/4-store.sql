-- Creating a trigger that triggers
-- ?? when a new order inserted


CREATE TRIGGER DECREASE_QUANTITY AFTER
INSERT ON
orders
FOR
EACH
ROW
UPDATE items 
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;