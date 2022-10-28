class Pais():

    def __init__(self, nombre, habitantes, idioma, fecha_independencia):
        self.nombre = nombre
        self.habitantes = habitantes
        self.idioma = idioma
        self.fecha_independencia = fecha_independencia

    def valor_per_capita(self):
        if self.nombre == "Mexico":
            return self.habitantes * 25 * 1.19
        elif self.nombre == "Costa Rica":
            return self.habitantes * 28 * 1.13
        elif self.nombre == "USA":
            return self.habitantes * 32 * 1.23
        else:
            return self.habitantes * 18 * 1.26

    def bienvenida(self):
        if self.nombre == "Mexico":
            return "Hola, mundo!"
        elif self.nombre == "Costa Rica":
            return "¡Pura vida!"
        elif self.nombre == "USA":
            return "¡Welcome"
        elif self.nombre == "Brasil":
            return "Bem-vindo"
        
        
        
        
