-- CATALOGO
CREATE OR REPLACE FUNCTION logCatalogo() RETURNS TRIGGER AS $$
	BEGIN
        INSERT INTO log_logcatalogo (a_id_tupla, n_id_tupla, metodo, data, a_nome, n_nome, a_descricao, n_descricao,
                a_preco_id, n_preco_id)
            values (OLD.id, NEW.id, TG_OP, CURRENT_TIMESTAMP, OLD.nome, new.nome, OLD.descricao, NEW.descricao,
                OLD.preco_id, NEW.preco_id);
        IF (TG_OP = 'DELETE') then
            RETURN OLD;
        ELSE
            RETURN NEW;
        END IF;
	END;
$$ LANGUAGE PLPGSQL;

CREATE TRIGGER log_catalogo
BEFORE UPDATE or INSERT or DELETE ON catalogo_catalogo
FOR EACH ROW EXECUTE PROCEDURE logCatalogo();

-- FORNECEDOR
CREATE OR REPLACE FUNCTION logFornecedor() RETURNS TRIGGER AS $$
	BEGIN
        INSERT INTO log_logfornecedor (a_id_tupla, n_id_tupla, metodo, data, a_nome, n_nome, a_cnpj, n_cnpj)
            values (OLD.id, NEW.id, TG_OP, CURRENT_TIMESTAMP, OLD.nome, new.nome, OLD.cnpj, NEW.cnpj);
        IF (TG_OP = 'DELETE') then
            RETURN OLD;
        ELSE
            RETURN NEW;
        END IF;
	END;
$$ LANGUAGE PLPGSQL;

CREATE TRIGGER log_fornecedor
BEFORE UPDATE or INSERT or DELETE ON catalogo_fornecedor
FOR EACH ROW EXECUTE PROCEDURE logFornecedor();

