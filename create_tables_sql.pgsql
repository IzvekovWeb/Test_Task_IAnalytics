
DROP TABLE employee, calendar, meet;

CREATE TABLE IF NOT EXISTS meet (
    meet_id SERIAL PRIMARY KEY,
    start_time time,
    end_time time,
    meet_name varchar(255),
    UNIQUE (start_time, end_time)
);

CREATE TABLE IF NOT EXISTS employee (
    employee_id SERIAL PRIMARY KEY,
    start_work time,
    end_work time,
    name varchar(255),
    surname varchar(255),
    position varchar(255),
    phone varchar(255) UNIQUE
);

CREATE TABLE IF NOT EXISTS calendar (
    employee_id integer,
    meet_id integer,
    FOREIGN KEY (employee_id) REFERENCES employee (employee_id) ON DELETE CASCADE,
    FOREIGN KEY (meet_id) REFERENCES meet (meet_id) ON DELETE CASCADE,
    UNIQUE (employee_id, meet_id)
);
