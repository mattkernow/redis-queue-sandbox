CREATE TABLE public.migration_id
(
  queue_id integer NOT NULL DEFAULT nextval('id_of_something_queue_id_seq'::regclass),
  added_to_queue timestamp without time zone,
  written_to_table timestamp without time zone,
  CONSTRAINT pk_queue_id PRIMARY KEY (queue_id)
)
WITH (
  OIDS=FALSE
);
