BEGIN;


CREATE TABLE IF NOT EXISTS public.account_customuser
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    password character varying(128) COLLATE pg_catalog."default" NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) COLLATE pg_catalog."default" NOT NULL,
    first_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    email character varying(254) COLLATE pg_catalog."default" NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    gender character varying(50) COLLATE pg_catalog."default",
    date_of_birth date,
    occupation character varying(50) COLLATE pg_catalog."default",
    business_owner boolean,
    income_per_month character varying(50) COLLATE pg_catalog."default",
    type_of_business character varying(50) COLLATE pg_catalog."default",
    date_of_establishment date,
    CONSTRAINT account_customuser_pkey PRIMARY KEY (id),
    CONSTRAINT account_customuser_username_key UNIQUE (username)
);

CREATE TABLE IF NOT EXISTS public.account_smeregistration
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    business_name character varying(50) COLLATE pg_catalog."default",
    business_id character varying(50) COLLATE pg_catalog."default",
    email character varying(50) COLLATE pg_catalog."default",
    type_of_business character varying(50) COLLATE pg_catalog."default",
    date_of_establishment date,
    user_id bigint NOT NULL,
    CONSTRAINT account_smeregistration_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.coarse_coarse
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    image character varying(100) COLLATE pg_catalog."default",
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    CONSTRAINT coarse_coarse_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.coarse_content_coarsecontent
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    notes text COLLATE pg_catalog."default" NOT NULL,
    video character varying(100) COLLATE pg_catalog."default",
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    coarse_id bigint NOT NULL,
    CONSTRAINT coarse_content_coarsecontent_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.coarse_enrollment_coarseenrollment
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    status character varying(10) COLLATE pg_catalog."default" NOT NULL,
    progress numeric(3, 3),
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    coarse_id bigint,
    user_id bigint NOT NULL,
    CONSTRAINT coarse_enrollment_coarseenrollment_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.financial_service_financialserviceprovider
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    services text COLLATE pg_catalog."default" NOT NULL,
    logo character varying(100) COLLATE pg_catalog."default",
    link character varying(100) COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    CONSTRAINT financial_service_financialserviceprovider_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.financial_service_investmentservice
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    business_type character varying(100) COLLATE pg_catalog."default" NOT NULL,
    min_investment numeric(10, 2),
    expected_return_rate numeric(5, 2),
    eligibility_criteria text COLLATE pg_catalog."default",
    min_income_required numeric(10, 2),
    service_provider_id bigint,
    CONSTRAINT financial_service_investmentservice_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.financial_service_loanservice
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    business_type character varying(100) COLLATE pg_catalog."default" NOT NULL,
    min_loan_amount numeric(10, 2),
    max_loan_amount numeric(10, 2),
    interest_rate numeric(5, 2),
    eligibility_criteria text COLLATE pg_catalog."default",
    min_income_required numeric(10, 2),
    service_provider_id bigint,
    CONSTRAINT financial_service_loanservice_pkey PRIMARY KEY (id)
);
END;