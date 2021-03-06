-- MySQL Script generated by MySQL Workbench
-- Sat Jan 23 14:43:22 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema poke_baza
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema poke_baza
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `poke_baza` DEFAULT CHARACTER SET utf8 ;
USE `poke_baza` ;

-- -----------------------------------------------------
-- Table `poke_baza`.`Trener`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `poke_baza`.`Trener` (
  `trener_id` INT(11) NOT NULL,
  `Imie` VARCHAR(45) NOT NULL,
  `Nazwisko` VARCHAR(45) NOT NULL,
  `Plec` VARCHAR(45) NOT NULL,
  `Data_urodzenia` DATE NOT NULL,
  PRIMARY KEY (`trener_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `poke_baza`.`podstawowe_staty`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `poke_baza`.`podstawowe_staty` (
  `idStatystyki` INT NOT NULL,
  `pod_hp` INT(11) NOT NULL,
  `pod_atk` INT(11) NOT NULL,
  `pod_def` INT(11) NOT NULL,
  `pod_sp_atk` INT(11) NOT NULL,
  `pod_sp_def` INT(11) NOT NULL,
  `pod_speed` INT(11) NOT NULL,
  PRIMARY KEY (`idStatystyki`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `poke_baza`.`wersja_gry`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `poke_baza`.`wersja_gry` (
  `wersja_id` INT(11) NOT NULL,
  `wersja_nazwa` VARCHAR(45) NOT NULL,
  `Trener_trener_id` INT(11) NOT NULL,
  PRIMARY KEY (`wersja_id`),
  INDEX `fk_wersja_gry_Trener1_idx` (`Trener_trener_id` ASC) ,
  CONSTRAINT `fk_wersja_gry_Trener1`
    FOREIGN KEY (`Trener_trener_id`)
    REFERENCES `poke_baza`.`Trener` (`trener_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `poke_baza`.`typy`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `poke_baza`.`typy` (
  `typ_id` INT NOT NULL,
  `typ_nazwa` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`typ_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `poke_baza`.`pokemon`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `poke_baza`.`pokemon` (
  `pok_id` INT(11) NOT NULL,
  `pok_nazwa` VARCHAR(45) NOT NULL,
  `pok_waga` INT(11) NOT NULL,
  `pok_wzrost` INT(11) NOT NULL,
  `Plec` VARCHAR(45) NOT NULL,
  `Trener_trener_id` INT(11) NOT NULL,
  `podstawowe_staty_idStatystyki` INT NOT NULL,
  `wersja_gry_wersja_id` INT(11) NOT NULL,
  `typy_typ_id` INT NOT NULL,
  PRIMARY KEY (`pok_id`, `Trener_trener_id`, `podstawowe_staty_idStatystyki`, `wersja_gry_wersja_id`, `typy_typ_id`),
  INDEX `fk_pokemon_Trener_idx` (`Trener_trener_id` ASC) ,
  INDEX `fk_pokemon_podstawowe_staty1_idx` (`podstawowe_staty_idStatystyki` ASC) ,
  INDEX `fk_pokemon_wersja_gry1_idx` (`wersja_gry_wersja_id` ASC) ,
  INDEX `fk_pokemon_typy1_idx` (`typy_typ_id` ASC) ,
  CONSTRAINT `fk_pokemon_Trener`
    FOREIGN KEY (`Trener_trener_id`)
    REFERENCES `poke_baza`.`Trener` (`trener_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pokemon_podstawowe_staty1`
    FOREIGN KEY (`podstawowe_staty_idStatystyki`)
    REFERENCES `poke_baza`.`podstawowe_staty` (`idStatystyki`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pokemon_wersja_gry1`
    FOREIGN KEY (`wersja_gry_wersja_id`)
    REFERENCES `poke_baza`.`wersja_gry` (`wersja_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pokemon_typy1`
    FOREIGN KEY (`typy_typ_id`)
    REFERENCES `poke_baza`.`typy` (`typ_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `poke_baza`.`ruchy`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `poke_baza`.`ruchy` (
  `ruch_id` INT(11) NOT NULL,
  `ruch_nazwa` VARCHAR(45) NOT NULL,
  `ruch_sila` SMALLINT(6) NOT NULL,
  `ruch_koszt` SMALLINT(6) NOT NULL,
  `ruch_celnosc` SMALLINT(6) NOT NULL,
  `pokemon_pok_id` INT(11) NOT NULL,
  `typy_typ_id` INT NOT NULL,
  PRIMARY KEY (`ruch_id`, `typy_typ_id`),
  INDEX `fk_ruchy_pokemon1_idx` (`pokemon_pok_id` ASC) ,
  INDEX `fk_ruchy_typy1_idx` (`typy_typ_id` ASC) ,
  CONSTRAINT `fk_ruchy_pokemon1`
    FOREIGN KEY (`pokemon_pok_id`)
    REFERENCES `poke_baza`.`pokemon` (`pok_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ruchy_typy1`
    FOREIGN KEY (`typy_typ_id`)
    REFERENCES `poke_baza`.`typy` (`typ_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
