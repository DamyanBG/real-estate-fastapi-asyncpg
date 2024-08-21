CREATE TYPE public.userrole AS ENUM
    ('user', 'admin', 'guest');

ALTER TYPE public.userrole
    OWNER TO postgres;

CREATE TYPE public.authprovider AS ENUM
    ('internal', 'google');

ALTER TYPE public.authprovider
    OWNER TO postgres;

CREATE SEQUENCE IF NOT EXISTS public.users_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.users_id_seq
    OWNER TO postgres;


CREATE TABLE IF NOT EXISTS public.users
(
    id integer NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    first_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    email character varying(255) COLLATE pg_catalog."default" NOT NULL,
    phone_number character varying(100) COLLATE pg_catalog."default" NOT NULL,
    password character varying(255) COLLATE pg_catalog."default",
    role userrole NOT NULL,
    auth_provider authprovider NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT users_email_key UNIQUE (email)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to postgres;

ALTER SEQUENCE public.users_id_seq
    OWNED BY public.users.id;