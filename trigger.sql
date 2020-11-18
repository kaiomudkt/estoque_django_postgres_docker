CREATE OR REPLACE FUNCTION log() RETURNS TRIGGER AS $$
	BEGIN
        IF (TG_OP = 'UPDATE') then
            INSERT INTO log_log (id_tabela, id_tupla, metodo, data)
                values (TG_RELNAME, OLD.id, 'UPDATE', CURRENT_TIMESTAMP);
            RETURN OLD;
        ELSIF (TG_OP = 'DELETE') then
            INSERT INTO log_log (id_tabela, id_tupla, metodo, data)
                values (TG_RELNAME, OLD.id, 'DELETE', CURRENT_TIMESTAMP);
            RETURN OLD;
        ELSIF (TG_OP = 'INSERT') then
            INSERT INTO log_log (id_tabela, id_tupla, metodo, data)
                values (TG_RELNAME, NEW.id, 'INSERT', CURRENT_TIMESTAMP);
            RETURN NEW;
        END IF;
	END;

$$ LANGUAGE PLPGSQL;


CREATE TRIGGER log
BEFORE UPDATE or INSERT or DELETE ON catalogo_catalogo
FOR EACH ROW EXECUTE PROCEDURE log();