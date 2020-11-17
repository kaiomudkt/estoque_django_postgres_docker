CREATE OR REPLACE FUNCTION log() RETURNS TRIGGER AS $$
	BEGIN 
		IF (TG_RELNAME = 'catalogo') then
			IF(TG_OP = 'UPDATE') then
				INSERT INTO log (id_tabela, id_tupla, metodo, data) 
					values (TG_RELNAME, OLD.id, 'UPDATE', CURRENT_TIMESTAMP);
			END IF;
			IF(TG_OP = 'DELETE') then
				INSERT INTO log (id_tabela, id_tupla, metodo, data) 
					values (TG_RELNAME, OLD.id, 'DELETE', CURRENT_TIMESTAMP);
			END IF;
			IF(TG_OP = 'INSERT') then
				INSERT INTO log (id_tabela, id_tupla, metodo, data) 
					values (TG_RELNAME, NEW.id, 'DELETE', CURRENT_TIMESTAMP);
			END IF;

		ELSIF (TG_RELNAME = 'fornecedor') then
			IF(TG_OP = UPDATE) then
				INSERT INTO log () values ();
			END IF;
		END IF;

	END;
$$ LANGUAGE PLPGSQL;


CREATE TRIGGER log
BEFORE UPDATE or INSERT or DELETE ON produto or fornecedor
FOR EACH ROW EXECUTE PROCEDURE log();