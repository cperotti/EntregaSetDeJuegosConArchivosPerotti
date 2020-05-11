import PySimpleGUI as sg
import json 

import hangman
import reversegam
import tictactoeModificado

datosJugadores = {}

def cargarDatosUsuario(datosJugadores,nombre,nombreJuego):
	datosJugadores[nombre]={'Juego':nombreJuego}
	with open('datosJugadores.txt', 'a') as archivo:
		json.dump(datosJugadores, archivo,indent=2)
		archivo.close()
		                   
def main(args):
	sigo_jugando = True
	while sigo_jugando:
		layout = [[sg.Text('Selecciones el juego que quiera jugar: ')],
		          [sg.Text('Nombre Jugador: '), sg.Input(key='nombre')],
	              [sg.Text('Ahorcado    '),sg.Button('Jugar1')],
                  [sg.Text('TA-TE-TI     '), sg.Button('Jugar2' )],
                  [sg.Text('Otello         '), sg.Button('Jugar3')],
                  [sg.Button('Salir')]]	
		window = sg.Window('Menú de juegos').Layout(layout).Finalize() 
		event, values = window.Read()
		
		if event == None:
			break
		elif event == 'Jugar1':
			if values['nombre'] == '':
				sg.Print('No ingresaste nombre de usuario!')
			else:
				hangman.main()
				nombreJuego = 'Ahorcado'
				nombre = values['nombre']
				cargarDatosUsuario(datosJugadores,nombre,nombreJuego)
		elif event == 'Jugar2':
			if values['nombre'] == '':
				sg.Print('No ingresaste nombre de usuario!')
			else:
				tictactoeModificado.main()
				nombreJuego = 'TA-TE-TI'
				nombre = values['nombre']
				cargarDatosUsuario(datosJugadores,nombre,nombreJuego)
		elif event == 'Jugar3':
			if values['nombre'] == '':
				sg.Print('No ingresaste nombre de usuario!')
			else:
				reversegam.main()
				nombreJuego = 'Otello'
				nombre = values['nombre']
				cargarDatosUsuario(datosJugadores,nombre,nombreJuego)
		elif event == 'Salir':
			sigo_jugando = False
			window.close()
					
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
