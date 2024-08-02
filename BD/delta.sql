-- Insertar Categorías
INSERT INTO Categorias (nombre, descripcion) VALUES 
('Llantas', 'Faros', 'Rines', 'Escapes'),
('Pilleri', 'Hella',  'BBS',  'Sparco'),
('Perfomance', 'Racing');

-- Insertar Proveedores
INSERT INTO Proveedores (nombre, contacto, telefono, direccion) VALUES 
('Pilleri', 'Pilleri@proveedora.com', '123456789', 'Calle Falsa 123'),
('Sparco', 'Sparcomexico@proveedorb.com', '987654321', 'Avenida Siempreviva 742');
('Hella',  'hellla@proveedord.com', '919288',  'Cerrada 192');

-- Insertar Productos
INSERT INTO Productos (nombre, descripcion, precio, cantidad, categoria_id, proveedor_id) VALUES 
('Llantas', 'Serie', 1200.00, 10, 1, 1),
('Llantas',  'Serie', 1600.00, 11, 1, 2)
('Faros', 'faros amarillos', 20.00, 50, 2, 2),
('Faros', 'faros led', 25.00, 55, 3, 5),
('Rines', 'BBS negros', 3.00, 100, 3, 1),
('Rines', 'BBS dorados',  4.00, 150, 4, 1);

-- Insertar Movimientos de Inventario
INSERT INTO Movimientos (producto_id, cantidad, tipo) VALUES 
(1, 5, 'entrada'),
(2, 10, 'salida'),
(3, 20, 'entrada'),
(1, 30, 'salida'),
(2, 40, 'entrada');


