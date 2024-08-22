CREATE SEQUENCE IF NOT EXISTS public.temp_images_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.temp_images_id_seq
    OWNER TO postgres;

CREATE TABLE IF NOT EXISTS public.temp_images
(
    id integer  NOT NULL DEFAULT nextval('temp_images_id_seq'::regclass),
    file_name character varying COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.temp_images
    OWNER to postgres;

ALTER SEQUENCE public.temp_images_id_seq
    OWNED BY public.temp_images.id;


ALTER TABLE IF EXISTS public.images
ADD COLUMN home_id INTEGER NOT NULL;

ALTER TABLE IF EXISTS public.images
    ADD CONSTRAINT image_home_id_fkey FOREIGN KEY (home_id)
    REFERENCES public.homes (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

