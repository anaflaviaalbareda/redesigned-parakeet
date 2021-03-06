-- MySQL Script generated by MySQL Workbench
-- Fri Jul 24 02:22:36 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

-- -----------------------------------------------------
-- Table `Dulce`.`Categoria`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Categoria` ;

CREATE TABLE IF NOT EXISTS `Categoria` (
  `idCategoria` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Descripcion` LONGTEXT NULL,
  PRIMARY KEY (`idCategoria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dulce`.`Producto`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Producto` ;

CREATE TABLE IF NOT EXISTS `Producto` (
  `idProducto` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Descripcion` LONGTEXT NOT NULL,
  `Short` VARCHAR(105) NOT NULL,
  `Foto` LONGTEXT NOT NULL,
  `Destacado` TINYINT NULL,
  `Precio` INT NOT NULL,
  `Unidad` VARCHAR(45) NOT NULL,
  `Categoria 1` INT NULL,
  `Categoria 2` INT NULL,
  PRIMARY KEY (`idProducto`),
  INDEX `fk_Producto_Categoria_idx` (`Categoria 1` ASC),
  INDEX `fk_Producto_Categoria1_idx` (`Categoria 2` ASC),
  CONSTRAINT `fk_Producto_Categoria`
    FOREIGN KEY (`Categoria 1`)
    REFERENCES `Categoria` (`idCategoria`)
    ON DELETE SET NULL
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Producto_Categoria1`
    FOREIGN KEY (`Categoria 2`)
    REFERENCES `Categoria` (`idCategoria`)
    ON DELETE SET NULL
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
