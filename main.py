from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "RUTINA OPTIMIZADA DIARIA Y SEMANAL - NAHUEL PIERINI", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, ln=True)
        self.ln(3)

    def add_table(self, data, col_widths):
        self.set_font("Arial", size=10)
        th = self.font_size + 2  # Altura de cada fila

        for row in data:
            # Verificamos si queda espacio suficiente
            if self.get_y() + th > self.page_break_trigger:
                self.add_page()

            for i, datum in enumerate(row):
                self.cell(col_widths[i], th, str(datum), border=1)
            self.ln(th)


if __name__ == '__main__':
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()

    # Objetivo
    pdf.chapter_title("OBJETIVO GENERAL")
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 10,
                   "Organizar las actividades de estudio, trabajo, recreacion, salud y tareas del hogar en una rutina diaria y semanal que maximice el enfoque, reduzca el burnout y potencie el desarrollo profesional y personal.")
    pdf.ln()

    # Matriz de categorías
    pdf.chapter_title("MATRIZ DE CATEGORIAS")
    matriz_data = [
        ["Actividad", "Tipo", "Energia", "Importancia", "Satisfaccion", "Horas/sem"],
        ["ReactJS / NodeJS / Java / etc.", "Trabajo", "Alta", "Muy alta", "Media/Alta", "20-25"],
        ["Redes / Cisco / Ciberseguridad", "Estudio", "Media", "Alta", "Media", "5-7"],
        ["Ingles", "Estudio", "Media", "Alta", "Media", "10-14"],
        ["Musica / DJ / Sintetizadores", "Recreacion", "Alta", "Media", "Muy alta", "6-8"],
        ["Fisica / Matematica / Ocultismo", "Recreacion", "Media", "Media", "Alta", "2-4"],
        ["Ejercicio (7x7 + cardio)", "Salud", "Alta", "Alta", "Alta", "5-7"],
        ["Comer / cocinar / limpiar", "Basico", "Baja", "Alta", "Neutro", "14-16"],
        ["Dormir nocturno + siesta", "Salud", "-", "Vital", "Alta", "49-56"],
        ["Pasear animales", "Recreacion", "Baja", "Media", "Alta", "2-3"]
    ]
    pdf.add_table(matriz_data, [50, 25, 20, 25, 30, 25])
    pdf.ln()

    # Rutina diaria base
    pdf.chapter_title("RUTINA DIARIA BASE (LUNES A VIERNES)")
    rutina_diaria = [
        ["Hora", "Actividad"],
        ["07:30 - 08:00", "Despertar, higiene, desayuno liviano"],
        ["08:00 - 08:45", "Ejercicio (7x7 Fausto)"],
        ["08:45 - 09:30", "Ducha, orden rapido, revisar tareas"],
        ["09:30 - 12:30", "Trabajo tecnico (programacion, backend, etc.)"],
        ["12:30 - 13:30", "Almuerzo + descanso"],
        ["13:30 - 15:00", "Estudio (Ciberseguridad, Inglés, Redes)"],
        ["15:00 - 16:30", "Proyecto personal / app / portfolio"],
        ["16:30 - 17:00", "Siesta corta o meditacion"],
        ["17:00 - 18:00", "Merienda y pausa activa"],
        ["18:00 - 19:00", "Practica creativa (musica, fisica, etc.)"],
        ["19:00 - 20:00", "Cocinar, comer, lavar platos"],
        ["20:00 - 21:00", "Recreacion libre"],
        ["21:00 - 21:30", "Higiene, apagar pantallas"],
        ["21:30 - 23:30", "Dormir"]
    ]
    pdf.add_table(rutina_diaria, [50, 140])
    pdf.ln()

    # Guardar PDF
    pdf_path = "C:\\Users\\Nahue\\Downloads\\Rutina_Optima_Nahuel_Tablas.pdf"
    pdf.output(pdf_path)
    print("PDF generado correctamente en:", pdf_path)