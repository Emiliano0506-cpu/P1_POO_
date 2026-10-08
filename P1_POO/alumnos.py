class alumnos:
  
      nombre = ""
      edad = 0
      calificacion = 0

      def MostrarDatos (self):
          print(f"Nombre: {self.nombre}")
          print(f"Edad: {self.edad}")
          print(f"Calificacion: {self.calificacion}")


      def estaAprobado (self ):
            if self.calificacion >= 6:
                print("El alumno esta aprobado")
            else:
                print("El alumno esta reprobado")

alumno1=alumnos()
alumno1.nombre = "Juan"
alumno1.edad = 20
alumno1.calificacion = 8
alumno1.MostrarDatos()
alumno1.estaAprobado()

alumno2=alumnos()
alumno2.nombre = "Maria"
alumno2.edad = 19
alumno2.calificacion = 7
alumno2.MostrarDatos()
alumno2.estaAprobado()