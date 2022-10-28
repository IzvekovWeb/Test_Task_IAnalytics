
CREATE TABLE meet (
    meet_id SERIAL PRIMARY KEY,
    start_time time,
    end_time time,
    meet_name varchar(255)
);

CREATE TABLE employee (
    employee_id SERIAL PRIMARY KEY,
    start_work time,
    end_work time,
    name varchar(255),
    surname varchar(255),
    position varchar(255),
    phone varchar(255)
);

CREATE TABLE calendar (
    employee_id integer,
    meet_id integer,
    FOREIGN KEY (employee_id) REFERENCES employee (employee_id),
    FOREIGN KEY (meet_id) REFERENCES meet (meet_id)
);