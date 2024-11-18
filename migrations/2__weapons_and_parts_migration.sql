USE eyeviation;

-- Insert weapons
INSERT INTO weapons (id, model) VALUES
('f47ac10b-58cc-4372-a567-0e02b2c3d479', 'Glock 17'),
('550e8400-e29b-41d4-a716-446655440000', 'M4'),
('6ba7b810-9dad-11d1-80b4-00c04fd430c8', 'FN Minimi');

-- Insert customizations (grouped by type)
-- Sights
INSERT INTO customizations (id, customization_type, customization_model) VALUES
('7ba7b810-9dad-11d1-80b4-00c04fd430c8', 'sight', 'Mepro - MPO PRO-F'),
('8ba7b810-9dad-11d1-80b4-00c04fd430c8', 'sight', 'Mepro - Hunter 4x'),
('9ba7b810-9dad-11d1-80b4-00c04fd430c8', 'sight', 'Mepro - MMX 3');

-- Laser Pointers
INSERT INTO customizations (id, customization_type, customization_model) VALUES
('a1a7b810-9dad-11d1-80b4-00c04fd430c8', 'laser', 'Nightstick - TSM11G'),
('b2a7b810-9dad-11d1-80b4-00c04fd430c8', 'laser', 'Wilcox - RAAM GSS'),
('c3a7b810-9dad-11d1-80b4-00c04fd430c8', 'laser', 'Wilcox - Raid Xe');

-- Grip Handles
INSERT INTO customizations (id, customization_type, customization_model) VALUES
('d4a7b810-9dad-11d1-80b4-00c04fd430c8', 'grip', 'MCK - Micro Conversion Kit Gen 2'),
('e5a7b810-9dad-11d1-80b4-00c04fd430c8', 'grip', 'Law - Grip-Pod Forgerip'),
('f6a7b810-9dad-11d1-80b4-00c04fd430c8', 'grip', 'BravoCo - Vertical Grip Mod 3');

-- Barrel Attachments
INSERT INTO customizations (id, customization_type, customization_model) VALUES
('g7a7b810-9dad-11d1-80b4-00c04fd430c8', 'barrel', 'Banish - Banish 45'),
('h8a7b810-9dad-11d1-80b4-00c04fd430c8', 'barrel', 'Midwest - Muzzle Break'),
('i9a7b810-9dad-11d1-80b4-00c04fd430c8', 'barrel', 'Midwest - Blast Diverter');

-- Insert weapon-customization relationships
-- Glock 17 compatibilities
INSERT INTO weapons_to_customizations (weapon_id, customization_id) VALUES
('f47ac10b-58cc-4372-a567-0e02b2c3d479', '7ba7b810-9dad-11d1-80b4-00c04fd430c8'),  -- Mepro - MPO PRO-F
('f47ac10b-58cc-4372-a567-0e02b2c3d479', 'a1a7b810-9dad-11d1-80b4-00c04fd430c8'),  -- Nightstick - TSM11G
('f47ac10b-58cc-4372-a567-0e02b2c3d479', 'd4a7b810-9dad-11d1-80b4-00c04fd430c8'),  -- MCK - Micro Conversion Kit
('f47ac10b-58cc-4372-a567-0e02b2c3d479', 'g7a7b810-9dad-11d1-80b4-00c04fd430c8');  -- Banish - Banish 45

-- M4 compatibilities
INSERT INTO weapons_to_customizations (weapon_id, customization_id) VALUES
('550e8400-e29b-41d4-a716-446655440000', '8ba7b810-9dad-11d1-80b4-00c04fd430c8'),  -- Mepro - Hunter 4x
('550e8400-e29b-41d4-a716-446655440000', '9ba7b810-9dad-11d1-80b4-00c04fd430c8'),  -- Mepro - MMX 3
('550e8400-e29b-41d4-a716-446655440000', 'b2a7b810-9dad-11d1-80b4-00c04fd430c8'),  -- Wilcox - RAAM GSS
('550e8400-e29b-41d4-a716-446655440000', 'e5a7b810-9dad-11d1-80b4-00c04fd430c8'),  -- Law - Grip-Pod
('550e8400-e29b-41d4-a716-446655440000', 'h8a7b810-9dad-11d1-80b4-00c04fd430c8');  -- Midwest - Muzzle Break

-- FN Minimi compatibilities
INSERT INTO weapons_to_customizations (weapon_id, customization_id) VALUES
('6ba7b810-9dad-11d1-80b4-00c04fd430c8', '9ba7b810-9dad-11d1-80b4-00c04fd430c8'),  -- Mepro - MMX 3
('6ba7b810-9dad-11d1-80b4-00c04fd430c8', 'c3a7b810-9dad-11d1-80b4-00c04fd430c8'),  -- Wilcox - Raid Xe
('6ba7b810-9dad-11d1-80b4-00c04fd430c8', 'f6a7b810-9dad-11d1-80b4-00c04fd430c8'),  -- BravoCo - Vertical Grip
('6ba7b810-9dad-11d1-80b4-00c04fd430c8', 'i9a7b810-9dad-11d1-80b4-00c04fd430c8');  -- Midwest - Blast Diverter