CREATE TABLE Departamento (
  codigo_departamento INT PRIMARY KEY,
  departamento VARCHAR(100) NOT NULL
);

CREATE TABLE Municipio (
  codigo_municipio INT PRIMARY KEY,
  municipio VARCHAR(100) NOT NULL,
  codigo_departamento INT,
  poblacion INT,
  FOREIGN KEY (codigo_departamento) REFERENCES Departamento(codigo_departamento)
);

CREATE TABLE DatosCovid (
  id INT PRIMARY KEY,
  codigo_municipio INT,
  fecha DATE NOT NULL,
  casos_confirmados INT,
  casos_recuperados INT,
  muertes INT,
  FOREIGN KEY (codigo_municipio) REFERENCES Municipio(codigo_municipio)
);
