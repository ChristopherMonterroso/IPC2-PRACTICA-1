text= """ 
        digraph X{
                rankdir= LR
                node[shape=none fontname=Helvetica]\n"""

for i in range(3):
    text+="""\n n"""+str(i)+"""
    [ label = <
        <table>
            <tr><td bgcolor="lightgray">Cliente:</td><td bgcolor="lightgray">Chris</td></tr>
            <tr><td bgcolor="lightyellow">Especialidad:</td>   <td bgcolor="lightyellow">Salchicha</td></tr>
            <tr><td bgcolor="aliceblue">Tiempo de orden:</td>     <td bgcolor="aliceblue">2 minutos</td></tr>
            <tr><td bgcolor="darkseagreen1">Tiempo total:</td>     <td bgcolor="darkseagreen1">2 minutos</td></tr>
        </table>
    > ];"""
text+="\n n"+str(3)+"""
    [ label = <
        <table>
            <tr><td bgcolor="lightgray">Tiempo total:</td><td bgcolor="lightgray">6 minutos</td></tr>
        </table>
    > ];"""


for i in range(3):
    text+="""\n n"""+str(i)+"""->n"""+str(i+1)+""
text+="\n}"

print(text)