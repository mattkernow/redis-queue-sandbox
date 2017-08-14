CREATE TABLE public.migration_id
(
  queue_id integer NOT NULL,
  added_to_queue timestamp without time zone,
  written_to_table timestamp without time zone DEFAULT now(),
  CONSTRAINT pk_queue_id PRIMARY KEY (queue_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.migration_id
  OWNER TO postgres;
