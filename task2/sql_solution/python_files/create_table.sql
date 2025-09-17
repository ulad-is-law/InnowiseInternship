CREATE TABLE IF NOT EXISTS production_data (
    plant VARCHAR(20),
    fin_material_id INTEGER,
    fin_material_release_type VARCHAR(10),
    fin_material_production_type VARCHAR(20),
    fin_production_quantity NUMERIC(12, 2),
    prod_material_id INTEGER,
    prod_material_release_type VARCHAR(10),
    prod_material_production_type VARCHAR(20),
    prod_material_production_quantity NUMERIC(12, 2),
    component_id INTEGER,
    component_material_release_type VARCHAR(10),
    component_material_production_type VARCHAR(20),
    component_consumption_quantity NUMERIC(12, 2),
    year INTEGER
);