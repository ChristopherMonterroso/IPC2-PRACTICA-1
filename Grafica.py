
import graphviz
import os
class graficar:
    def __init__(self,elementos) -> None:
        self.elementos=elementos
        self.crear()
    def crear(self):
        
        RutaPng="Control de ordenes"
        text="""
            digraph X{
                rankdir= BT
                node[shape=none fontname=Helvetica]\n"""
        for i in range(len(self.elementos)):
            text+="""n"""+str(i)+"""
            [ label = <
                <table>
                    <tr><td bgcolor=\"lightgray\">Cliente:</td>           <td bgcolor=\"lightgray\">"""+str(self.elementos[i][0])+"""</td></tr>
                    <tr><td bgcolor=\"lightyellow\">Especialidad:</td>   <td bgcolor=\"lightyellow\">"""+str(self.elementos[i][1])+"""</td></tr>
                    <tr><td bgcolor=\"aliceblue\">Tiempo de orden:</td>     <td bgcolor=\"aliceblue\">"""+str(self.elementos[i][2])+"""minutos</td></tr>
                    <tr><td bgcolor=\"darkseagreen1\">Tiempo total:</td>     <td bgcolor=\"darkseagreen1\">""" + str(self.elementos[i][3])+""" minutos</td></tr>
    
                </table>
            > ];"""
        text+="\n n"+str(len(self.elementos))+"""
        [ label = <
            <table>
                <tr><td bgcolor="white">Tiempo total de espera:</td><td bgcolor="white">"""+str(self.elementos[len(self.elementos)-1][3])+""" minutos</td></tr>
             </table>
         > ];"""

        if len(self.elementos)>0:
            for i in range(len(self.elementos)):
                text+="""\n n"""+str(i)+"""->n"""+str(i+1)+""
        text+="}"
        try:

            src = graphviz.Source(text,format="png")
            src.render(RutaPng)
            if os.path.exists(RutaPng):
                os.remove(RutaPng)
            os.startfile(str(RutaPng)+".png")
            print("Atención: Se guardo el archivo con el nombre: "+str(RutaPng)+".png")
        except :
            print("Error")
