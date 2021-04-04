from django.db import models
import datetime

class Paciente(models.Model):
    nombres_p = models.CharField(max_length=30)
    apellidos_p = models.CharField(max_length=30)
    rut_p = models.CharField(max_length=10)
    sexo_p = models.CharField(max_length=1)
    telefono_p = models.CharField(max_length=12)
    fecha_nac_p = models.DateField()
    estado_p = models.IntegerField()

    def edad_dias(self):
        hoy = datetime.date.today()
        dias = hoy - self.fecha_nac_p

        return dias

    def calcular_edad(self):
        # Obtenemos la fecha de hoy:   hoy = date.today()
        # Sustituimos el año de self.fecha_nac_p por el actual:
        hoy = datetime.date.today()      
        try: 
            cumpleanios = self.fecha_nac_p.replace(year=hoy.year) 
        # En caso de que la fecha de self.fecha_nac_p es 29 de 
        # febrero y el año actual no sea bisiesto: 
        except ValueError: 
            # Le restamos uno al día de self.fecha_nac_p para que quede en 28:       
            cumpleanios = self.fecha_nac_p.replace(year=hoy.year, day=self.fecha_nac_p.day - 1) 
        # Cálculo final: 
        if cumpleanios > hoy:          
            return hoy.year - self.fecha_nac_p.year - 1 
        else: 
            return hoy.year - self.fecha_nac_p.year 
        
    def sexo(self):
        if(self.sexo_p == 'F'):
            return 'Femenino'
        elif(self.sexo_p == 'M'):
            return 'Masculino'
        else:
            return 'No presenta registro'        

class FichaM(models.Model):
    dia_fhc_fm = models.IntegerField()
    mes_fch_fm = models.IntegerField()
    anio_fch_fm = models.IntegerField()
    paciente_fm = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    diagnostico_fm = models.TextField()
    motivo_fm = models.TextField()
    
