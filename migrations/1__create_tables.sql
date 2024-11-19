CREATE DATABASE IF NOT EXISTS eyeviation;

CREATE TABLE IF NOT EXISTS eyeviation.users (
  id VARCHAR(36) PRIMARY KEY,
  username VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS eyeviation.weapons (
  id VARCHAR(36) PRIMARY KEY,
  model VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS eyeviation.customizations (
  id VARCHAR(36) PRIMARY KEY,
  customization_type VARCHAR(255) NOT NULL,
  customization_model VARCHAR(255) NOT NULL,
  CONSTRAINT unique_customization_type_per_model UNIQUE (customization_type, customization_model)
);

CREATE TABLE IF NOT EXISTS eyeviation.weapons_to_customizations (
  weapon_id VARCHAR(36) NOT NULL,
  customization_id VARCHAR(36) NOT NULL,
  FOREIGN KEY (weapon_id) REFERENCES eyeviation.weapons(id),
  FOREIGN KEY (customization_id) REFERENCES eyeviation.customizations(id),
  PRIMARY KEY (weapon_id, customization_id)
);


CREATE TABLE IF NOT EXISTS eyeviation.saved_weapons (
  id VARCHAR(36) PRIMARY KEY,
  user_id VARCHAR(36) NOT NULL,
  weapon_id VARCHAR(36) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES eyeviation.users(id),
  FOREIGN KEY (weapon_id) REFERENCES eyeviation.weapons(id),
  INDEX user_id_idx (user_id)
);

CREATE TABLE IF NOT EXISTS eyeviation.saved_customizations (
  id VARCHAR(36) PRIMARY KEY,
  user_id VARCHAR(36) NOT NULL,
  saved_weapon_id VARCHAR(36) NOT NULL,
  customization_id VARCHAR(36) NOT NULL,
  slot_type VARCHAR(255) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES eyeviation.users(id),
  FOREIGN KEY (saved_weapon_id) REFERENCES eyeviation.saved_weapons(id),
  FOREIGN KEY (customization_id) REFERENCES eyeviation.customizations(id),
  CONSTRAINT unique_slot_per_weapon UNIQUE (saved_weapon_id, slot_type),
  INDEX saved_weapon_id_idx (saved_weapon_id)
);
