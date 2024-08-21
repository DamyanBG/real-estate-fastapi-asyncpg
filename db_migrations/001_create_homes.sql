CREATE SEQUENCE IF NOT EXISTS public.homes_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1
    OWNED BY homes.id;

ALTER SEQUENCE public.homes_id_seq
    OWNER TO postgres;

CREATE TABLE IF NOT EXISTS public.homes
(
    id integer NOT NULL DEFAULT nextval('homes_id_seq'::regclass),
    title character varying(150) COLLATE pg_catalog."default" NOT NULL,
    city character varying(150) COLLATE pg_catalog."default" NOT NULL,
    neighborhood character varying(255) COLLATE pg_catalog."default" NOT NULL,
    address character varying(255) COLLATE pg_catalog."default" NOT NULL,
    price integer,
    year integer,
    CONSTRAINT homes_pkey PRIMARY KEY (id)
);
