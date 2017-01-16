drop table if exists user_data;

create table user_data (
  id integer primary key autoincrement,
  username text not null,
  color text not null,
  pet text not null
);
