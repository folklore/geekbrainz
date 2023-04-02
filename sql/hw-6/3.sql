CREATE OR REPLACE FUNCTION check_community_name_length_func() RETURNS TRIGGER
    LANGUAGE plpgsql
AS $$
DECLARE
    min_length int := 5;
BEGIN
    IF LENGTH(NEW.name) < min_length THEN
      RAISE EXCEPTION 'Name length of community should be greater than %', min_length;
    END IF;

    RETURN NEW;
END; $$;

CREATE TRIGGER check_community_name_length_trig
    BEFORE INSERT ON communities FOR EACH ROW
    EXECUTE PROCEDURE check_community_name_length_func();

-- INSERT INTO communities(name, admin_user_id) VALUES('asd', 1);
-- ERROR:  Name length of community should be greater than 5
-- CONTEXT:  PL/pgSQL function check_community_name_length_func() line 6 at RAISE
