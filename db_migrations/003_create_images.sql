CREATE SEQUENCE IF NOT EXISTS public.images_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.images_id_seq
    OWNER TO postgres;

CREATE TABLE IF NOT EXISTS public.images
(
    id integer  NOT NULL DEFAULT nextval('images_id_seq'::regclass),
    file_name character varying COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.images
    OWNER to postgres;

ALTER SEQUENCE public.images_id_seq
    OWNED BY public.images.id;