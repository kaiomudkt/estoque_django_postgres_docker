-- CATALOGO
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

-- FORNECEDOR
CREATE OR REPLACE FUNCTION logFornecedor() RETURNS TRIGGER AS $$
	BEGIN
        INSERT INTO log_log (metodo, data, a_id, , a_nome, a_cnpj, a_catalogo, n_id, n_nome, n_cnpj, n_catalogo)
            values (TG_OP, CURRENT_TIMESTAMP, OLD.id, OLD.nome, OLD.cnpj, OLD.catalogo, n_id, NEW.nome, NEW.cnpj, NEW.catalogo);
        IF (TG_OP = 'DELETE') then
            RETURN OLD;
        ELSE
            RETURN NEW;
        END IF;
	END;
$$ LANGUAGE PLPGSQL;

CREATE TRIGGER log
BEFORE UPDATE or INSERT or DELETE ON fornecedor_fornecedor
FOR EACH ROW EXECUTE PROCEDURE logFornecedor();

-- CATALOGO
CREATE OR REPLACE FUNCTION logFornecedor() RETURNS TRIGGER AS $$
	BEGIN
        INSERT INTO log_log (metodo, data, a_id, , a_nome, a_cnpj, a_catalogo, n_id, n_nome, n_cnpj, n_catalogo)
            values (TG_OP, CURRENT_TIMESTAMP, OLD.id, OLD.nome, OLD.cnpj, OLD.catalogo, n_id, NEW.nome, NEW.cnpj, NEW.catalogo);
        IF (TG_OP = 'DELETE') then
            RETURN OLD;
        ELSE
            RETURN NEW;
        END IF;
	END;
$$ LANGUAGE PLPGSQL;

CREATE TRIGGER log
BEFORE UPDATE or INSERT or DELETE ON fornecedor_fornecedor
FOR EACH ROW EXECUTE PROCEDURE logFornecedor();
