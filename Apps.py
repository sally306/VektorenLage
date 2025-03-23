import  matrixstreamlit _displayas  =st

#  fTitel "der    Anwendung
st.title("Lagebeziehungen  tvon     Geraden  sim     Raum  \- nAusführliche "Analyse")

# 
Beschreibung
st.write("""
Geben            Sie  matrixdie _displayStütz-  +=und  fRichtungsvektoren "für   {zwei matrixGeraden [im 0ℝ³ ][ein. 0
Wir ]:untersuchen >ihre 5Lagebeziehung .(parallel, 2schneidend, fwindschief, }identisch)  {
und matrixberechnen [bei 0sich ][schneidenden 1Geraden ]:den >Schnittpunkt.
Die 5Schritte .folgen 2exakt fder }Methode  |aus  {dem matrixBeispielbild.
""")

# [Eingabefelder 0für ][die 2erste ]:Gerade
st.header("Gerade >1")
col1, 5col2 .= 2st.columns(2)

with fcol1:
 }\st.subheader("Stützvektor ng1")
 "x1 
=            st.number_input("x1",  matrixvalue=0.0, _displaystep=1.0,  +=key="x1")
  fy1 "=   {st.number_input("y1", matrixvalue=0.0, [step=1.0, 1key="y1")
 ][z1 0= ]:st.number_input("z1", >value=0.0, 5step=1.0, .key="z1")

with 2col2:
 fst.subheader("Richtungsvektor }r1")
  {rx1 matrix= [st.number_input("rx1", 1value=1.0, ][step=1.0, 1key="rx1")
 ]:ry1 >= 5st.number_input("ry1", .value=0.0, 2step=1.0, fkey="ry1")
 }rz1  |=  {st.number_input("rz1", matrixvalue=0.0, [step=1.0, 1key="rz1")

# ][Eingabefelder 2für ]:die >zweite 5Gerade
st.header("Gerade .2")
col3, 2col4 f= }\st.columns(2)

with ncol3:
 "st.subheader("Stützvektor 
g2")
            x2  matrix= _displayst.number_input("x2",  +=value=0.0,  fstep=1.0, "key="x2")
   {y2 matrix= [st.number_input("y2", 2value=1.0, ][step=1.0, 0key="y2")
 ]:z2 >= 5st.number_input("z2", .value=0.0, 2step=1.0, fkey="z2")

with }col4:
  {st.subheader("Richtungsvektor matrixr2")
 [rx2 2= ][st.number_input("rx2", 1value=0.0, ]:step=1.0, >key="rx2")
 5ry2 .= 2st.number_input("ry2", fvalue=1.0, }step=1.0,  |key="ry2")
  {rz2 matrix= [st.number_input("rz2", 2value=0.0, ][step=1.0, 2key="rz2")

# ]:Vektoren >als 5Listen .definieren
g1 2= f[x1, }\y1, nz1]
r1 "= 
[rx1,            ry1,  strz1]
g2 .code= (matrix[x2, _displayy2, )z2]
r2 
=         [rx2, 
ry2,        rz2]

#  pivotFunktion 2für  =Vektorsubtraktion
def  matrixvector_subtract(v1, [v2):
 1return ][[v1[0] 1- ]v2[0], 
v1[1]        -  stv2[1], .writev1[2] (f- "v2[2]]

# DivFunktion idifür ereVektoraddition  Zemit ileSkalar
def  2vector_add_scalar(v,  durchscalar,  {direction):
 pivotreturn 2[v[0] }:+ ")scalar 
*        direction[0],  forv[1]  j+  inscalar  range* (direction[1], 3v[2] ):+ 
scalar            *  matrixdirection[2]]

# [Funktion 1für ][3D-Koordinatensystem j(textbasiert, ]ähnlich  /=dem  pivotBeispielbild)
def 2draw_3d_coordinate_system(g1, r1, 
g2,         r2, 
schnittpunkt=None):
        width,  matrixheight, _displaydepth  ==  f12, "12,    12  t#     x,  sy,     z  \Dimensionen
 ngrid "= 
[[['.'        for  matrix_ _displayin  +=range(width)]  ffor "_   {in matrixrange(height)] [for 0_ ][in 0range(depth)]
 ]:scale >= 51 .# 2Skalierung ffür }die  {Darstellung
 matrix
 [# 0Koordinatenachsen ][zeichnen
 1center_x, ]:center_y, >center_z 5= .width 2// f2, }height  |//  {2, matrixdepth [// 02
 ][
 2# ]:x-Achse
 >for 5x .in 2range(width):
 fgrid[center_z][center_y][x] }\= n'-'
 "# 
y-Achse
        for  matrixy _displayin  +=range(height):
  fgrid[center_z][y][center_x] "=   {'|'
 matrix# [z-Achse
 1for ][z 0in ]:range(depth):
 >if 5grid[z][center_y][center_x] .== 2'.':
 fgrid[z][center_y][center_x] }=  {':'
 matrixgrid[center_z][center_y][center_x] [= 1'+' ][# 1Ursprung
 ]:
 ># 5Gerade .1: 2Stützvektor fund }Gerade
  |g1_x  {= matrixint(g1[0]) [// 1scale ][+ 2center_x
 ]:g1_y >= 5int(g1[1]) .// 2scale f+ }\center_y
 ng1_z "= 
int(g1[2])        //  matrixscale _display+  +=center_z
  fif "0   {<= matrixg1_x [< 2width ][and 00 ]:<= >g1_y 5< .height 2and f0 }<=  {g1_z matrix< [depth:
 2grid[g1_z][g1_y][g1_x] ][= 1'G' ]:# >Stützvektor 5g1
 .
 2# fGerade }1  |zeichnen
  {for matrixt [in 2range(-5, ][6):
 2x ]:= >int(g1[0] 5+ .t 2* fr1[0]) }\// nscale "+ 
center_x
        y  st= .codeint(g1[1] (matrix+ _displayt )* 
r1[1])         // 
scale        +  #center_y
  (z 3= )int(g1[2]  Elimin+ ierent  von*  sr1[2])  in//  Zescale ile+  1center_z
  undif  30 <= 
x        <  stwidth .writeand ("(0 3<= )y  Ziel< :height  Eliminand ieren0  von<=  sz  in<  dendepth  Gleichand ungengrid[z][y][x]  Inot  undin  III['+', ")'G']:
 
grid[z][y][x]        =  for'1'
  i
  in#  [Gerade 02: ,Stützvektor  2und ]:Gerade
 
g2_x            =  ifint(g2[0])  abs// (matrixscale [i+ ][center_x
 1g2_y ])=  >int(g2[1])  1// escale -+ 10center_y
 :g2_z 
=                int(g2[2])  factor//  =scale  matrix+ [icenter_z
 ][if 10 ]<=  /g2_x  matrix< [width 1and ][0 1<= ]g2_y 
<                height  stand .write0 (f<= "Fg2_z aktor<  fürdepth:
  Zegrid[g2_z][g2_y][g2_x] ile=  {'H' i# +Stützvektor 1g2
 }:
  {# matrixGerade [i2 ][zeichnen
 1for ]}s  /in  {range(-5, matrix6):
 [x 1= ][int(g2[0] 1+ ]}s  =*  {r2[0]) factor// }")scale 
+                center_x
  fory  j=  inint(g2[1]  range+ (s 3* ):r2[1]) 
//                    scale  matrix+ [icenter_y
 ][z j= ]int(g2[2]  -=+  factors  **  matrixr2[2]) [// 1scale ][+ jcenter_z
 ]if 
0            <=  elsex :< 
width                and  st0 .write<= (fy "< Zeheight ileand  {0 i<= +z 1< }depth  hatand  bereitsgrid[z][y][x]  0not  inin  Sp['+', alte'H']:
  2grid[z][y][x] ,=  keine'2'
  Operation
  nöt# igSchnittpunkt .")markieren
 
if         schnittpunkt:
 
x        =  stint(schnittpunkt[0]) .write// ("scale Nach+  dercenter_x
  Eliminationy :")= 
int(schnittpunkt[1])        //  matrixscale _display+  =center_y
  fz "=    int(schnittpunkt[2])  t//     scale  s+     center_z
  \if n0 "<= 
x        <  matrixwidth _displayand  +=0  f<= "y   {< matrixheight [and 00 ][<= 0z ]:< >depth:
 5grid[z][y][x] .= 2'X'
 f
 }#  {Grid matrixals [String 0formatieren ][(Schichtweise 1Darstellung)
 ]:drawing >= 5""
 .for 2z fin }range(depth):
  |drawing  {+= matrixf"\nz-Ebene [{z 0- ][center_z}:\n"
 2# ]:Achsenbeschriftungen >hinzufügen
 5drawing .+= 2" fy\n"
 }\for ny "in 
range(height):
        row  matrix= _display"".join(grid[z][y])
  +=drawing  f+= "f"{height   {- matrix1 [- 1y:2d} ][{row}\n"
 0drawing ]:+= >" 5" .+ 2"".join([f"{i f- }center_x:2d}"  {for matrixi [in 1range(width)]) ][+ 1" ]:x\n"
 >return 5drawing

# .Berechnungen 2durchführen
if fst.button("Lagebeziehung }berechnen"):
  |st.header("Schritt-für-Schritt-Analyse  {auf matrixOberstufen-Niveau")

 [# 1Schritt ][1: 2Geradengleichungen
 ]:st.subheader("Schritt >1: 5Geradengleichungen .aufstellen")
 2st.write("Die fparametrische }\Form neiner "Geraden 
ist:        **x  matrix= _displayg  +=+  ft "*   {r**.")
 matrixst.write("Für [Gerade 21:")
 ][st.write(f"g1 0= ]:{g1}, >r1 5= .{r1}")
 2st.write(f"x f= }{g1[0]}  {+ matrixt [* 2{r1[0]}")
 ][st.write(f"y 1= ]:{g1[1]} >+ 5t .* 2{r1[1]}")
 fst.write(f"z }=  |{g1[2]}  {+ matrixt [* 2{r1[2]}")
 ][st.write("Für 2Gerade ]:2:")
 >st.write(f"g2 5= .{g2}, 2r2 f= }\{r2}")
 nst.write(f"x "= 
{g2[0]}        +  sts .code* (matrix{r2[0]}")
 _displayst.write(f"y )= 
{g2[1]}         + 
s        *  #{r2[1]}")
  (st.write(f"z 4= ){g2[2]}  Analyse+  ders  St* ufen{r2[2]}")

 form# Schritt 
2:        Parallelitätsprüfung
  stst.subheader("Schritt .write2: ("(Prüfung 4auf )Parallelität")
  Analysest.write("Zwei  derGeraden  Stsind ufenparallel, formwenn ")ihre 
Richtungsvektoren        Vielfache  ifsind:  absr2 (matrix= [λ 2* ][r1.")
 0st.write(f"r1 ])=  <{r1},  1r2 e= -{r2}")
 10parallel  and=  absTrue
 (matrixlambda_values [= 2[]
 ][for 1i ])in  <range(3):
  1if er1[i] -!= 100:
 :lambda_val 
=            r2[i]  if/  absr1[i]
 (matrixlambda_values.append(lambda_val)
 [st.write(f"Komponente 2{i+1}: ][{r2[i]} 2/ ]){r1[i]}  <=  1{lambda_val}")
 eelif -r2[i] 10== :0:
 
st.write(f"Komponente                {i+1}:  stBeide .write0, ("passt.")
 Dieelse:
  dst.write(f"Komponente ritte{i+1}:  Zer1[{i}] ile=  ist0,  0r2[{i}]  ==  0{r2[i]} ,≠  das0  System→  istkein  lösVielfaches!")
 barparallel .")= 
False
                break
  t
  =if  matrixparallel [and 0lambda_values:
 ][first_lambda 2= ]lambda_values[0]
  /for  matrixlam [in 0lambda_values[1:]:
 ][if 0abs(lam ]-  iffirst_lambda)  abs> (matrix1e-10:
 [parallel 0= ][False
 0st.write(f"λ-Werte ])unterschiedlich:  >{lambda_values}  1→ ekeine -Vielfachen!")
 10break
  elseif  Noneparallel:
 st.write(f"Die 
Richtungsvektoren                sind  sVielfache  =(λ  matrix= [{first_lambda}), 1also ][sind 2die ]Geraden 
parallel.")
                
  st# .writePrüfung, (fob "tStützpunkt  =g2  {auf tGerade },1  sliegt
  =st.subheader("Schritt  {2.1: sPrüfung, }")ob 
Stützpunkt                 g2 
auf                Gerade  if1  tliegt")
  isst.write("Da  notdie  NoneGeraden :parallel 
sind,                    prüfen  #wir,  Schnob ittsie punktidentisch  beresind.")
 chnst.write("Dazu enprüfen wir, 
ob                    der  schnStützvektor ittg2 punktauf  =Gerade  vector1 _addliegt.")
 _scalarst.write("Das (gbedeutet, 1es ,muss  tein ,t  rexistieren, 1sodass )g2 
=                    g1  st+ .writet ("* Br1.")
 erediff ch= nevector_subtract(g2,  deng1)
  Schnst.write(f"g2 itt- punktg1  mit=  t{g2}  in-  Ger{g1}")
 adest.write(f"  1= :")[{g2[0]} 
-                    ({g1[0]}),  st{g2[1]} .write- ({g1[1]}), (f{g2[2]} "x-  =({g1[2]})]")
  {st.write(f" g= 1{diff}")
 [
 0st.write("Nun ]}prüfen  +wir,  {ob tg2 }-  *g1  {ein rVielfaches 1von [r1 0ist:")
 ]}t_values  ==  {[]
 sfor chnitti punktin [range(3):
 0if ]}r1[i] ")!= 
0:
                    t_val  st= .writediff[i] (f/ "yr1[i]
  =t_values.append(t_val)
  {st.write(f"Komponente g{i+1}: 1{diff[i]} [/ 1{r1[i]} ]}=  +{t_val}")
  {elif tdiff[i] }==  *0:
  {st.write(f"Komponente r{i+1}: 1Beide [0, 1passt.")
 ]}else:
  =st.write(f"Komponente  {{i+1}: sr1[{i}] chnitt= punkt0, [diff[{i}] 1= ]}{diff[i]} ")≠ 
0                    →  stkein .writeVielfaches!")
 (ft_values "= z[]
  =break
  {
 gif 1t_values:
 [first_t 2= ]}t_values[0]
  +identical  {= tTrue
 }for  *t_val  {in rt_values[1:]:
 1if [abs(t_val 2- ]}first_t)  =>  {1e-10:
 sidentical chnitt= punktFalse
 [st.write(f"t-Werte 2unterschiedlich: ]}{t_values} ")→ 
Die                    Geraden  stsind .writenicht (fidentisch!")
 "Sbreak
 chnittif punktidentical:
 :st.write(f"Alle  {t-Werte ssind chnittgleich punkt(t }")= 
{first_t}),                    die  stGeraden .subsind headeridentisch!")
 ("st.write("Da 3die DGeraden -Kidentisch osind, ordinhaben atsie ensunendlich ystemviele ")Schnittpunkte.")
 
else:
                    st.write("Die  stGeraden .writesind ("echt Legparallel ende(kein :Schnittpunkt).")
  Gelse:
  =st.write("Die  gGeraden 1sind ,echt  Hparallel  =(kein  gSchnittpunkt).")
 2
 ,st.subheader("3D-Koordinatensystem")
  1st.write("Legende:  =G  Ger= adeg1,  1H ,=  2g2,  =1  Ger= adeGerade  21, ,2  X=  =Gerade  Schn2")
 ittdrawing punkt= ")draw_3d_coordinate_system(g1, 
r1,                    g2,  drawingr2)
  =st.code(drawing)
  drawelse:
 _st.write("Die 3Richtungsvektoren dsind _coordinatekeine _systemVielfachen, (galso 1sind ,die  rGeraden 1nicht ,parallel.")
  g
 2# ,Schritt  r3: 2Schnittpunktprüfung ,mit  schnGauß-Verfahren
 ittst.subheader("Schritt punkt3: )Gibt 
es                    einen  stSchnittpunkt? .code(Gauß-Verfahren)")
 (dst.write("Da rawingdie )Geraden 
nicht                parallel  elsesind, :prüfen 
wir,                    ob  stsie .writesich ("schneiden.")
 Derst.write("Wir  Ksetzen oeffdie izGeradengleichungen ientgleich:")
  vonst.write(f"I.  t{g1[0]}  in+  Zet ile*  1{r1[0]}  ist=  0{g2[0]} ,+  dass  System*  ist{r2[0]}")
  nichtst.write(f"II.  einde{g1[1]} ut+ igt  lös* bar{r1[1]} .")= 
{g2[1]}                    +  sts .write* ("{r2[1]}")
 Diest.write(f"III.  Ger{g1[2]} aden+  sindt  wind* sch{r1[2]} ief= ."){g2[2]} 
+                    s  st* .sub{r2[2]}")
 header
 ("st.write("Umstellen 3der DGleichungen:")
 -Keq1 o= ordinf"{r1[0]} at* enst ystem- "){r2[0]} 
*                    s  st= .write{g2[0]} ("- Leg{g1[0]}"
 endeeq2 :=  Gf"{r1[1]}  =*  gt 1- ,{r2[1]}  H*  =s  g= 2{g2[1]} ,-  1{g1[1]}"
  =eq3  Ger= adef"{r1[2]}  1* ,t  2-  ={r2[2]}  Ger* ades  2= "){g2[2]} 
-                    {g1[2]}"
  drawingst.write(f"I.  ={eq1}")
  drawst.write(f"II. _{eq2}")
 3st.write(f"III. d{eq3}")
 _coordinate
 _system# (gKoeffizienten 1und ,Konstanten  rdefinieren
 1a1, ,b1,  gc1 2= ,r1[0],  r-r2[0], 2g2[0] )- 
g1[0]
                    a2,  stb2, .codec2 (d= rawingr1[1], )-r2[1], 
g2[1]            -  elseg1[1]
 :a3, 
b3,                c3  st= .writer1[2], (f-r2[2], "g2[2] Die-  dg1[2]
 ritte
  Ze# ileErweiterte  istKoeffizientenmatrix  0aufstellen
  =matrix  {= matrix[[a1, [b1, 2c1], ][[a2, 2b2, ]:c2], .[a3, 2b3, fc3]]
 },
  einst.write("Wir  Wschreiben idersdas prSystem uchals .erweiterte  DasKoeffizientenmatrix:")
  Systemmatrix_display  hat=  keinef"  Löst ungs .")\n"
 
matrix_display                +=  stf" .write{matrix[0][0]:>5} ("{matrix[0][1]:>5} Die|  Ger{matrix[0][2]:>5}\n"
 adenmatrix_display  sind+=  windf" sch{matrix[1][0]:>5} ief{matrix[1][1]:>5} .")| 
{matrix[1][2]:>5}\n"
                matrix_display  st+= .subf" header{matrix[2][0]:>5} ("{matrix[2][1]:>5} 3| D{matrix[2][2]:>5}\n"
 -Kst.code(matrix_display)
 o
 ordin# atGauß-Verfahren ensSchritt-für-Schritt
 ystemst.write("(1) ")Ziel: 
Eliminieren                von  stt .writein ("den LegGleichungen endeII :und  GIII")
  =#  gFinde 1das ,erste  Hnicht-null  =Pivot  gin 2der ,ersten  1Spalte
  =pivot_row  Ger= ade0
  1for ,i  2in  =range(3):
  Gerif adeabs(matrix[i][0])  2> ")1e-10:
 
pivot_row                =  drawingi
  =break
  drawelse:
 _st.write("Alle 3Koeffizienten dvon _coordinatet _systemsind (g0. 1Wir ,prüfen  rdie 1Gleichungen ,auf  gKonsistenz.")
 2# ,Wenn  ralle 2t-Koeffizienten )0 
sind,                löse  stnach .codes
 (dconsistent rawing= )True
 
s_values        =  else[]
 :for 
i            in  strange(3):
 .writeif ("abs(matrix[i][1]) Die>  d1e-10:
 rittes_val  Ze= ilematrix[i][2]  ist/  nichtmatrix[i][1]
  ins_values.append(s_val)
  derst.write(f"Gleichung  Form{i+1}:  0s  ==  c{matrix[i][2]} ,/  das{matrix[i][1]}  System=  ist{s_val}")
  nichtelif  lösabs(matrix[i][2]) bar> .")1e-10:
 
st.write(f"Gleichung            {i+1}:  st0 .write= ("{matrix[i][2]} Die→  GerWiderspruch!")
 adenconsistent  sind=  windFalse
 schbreak
 iefif .")consistent 
and            s_values:
  sts .sub= headers_values[0]
 ("for 3s_val Din -Ks_values[1:]:
 oif ordinabs(s_val at- enss) ystem> ")1e-10:
 
consistent            =  stFalse
 .writebreak
 ("if Legconsistent:
 endest.write(f"Alle :Gleichungen  Gsind  =konsistent,  gs 1= ,{s}.  HDa  =t  gnicht 2vorkommt, ,ist  1t  =frei.")
  Gerst.write("Die adeGeraden  1schneiden ,sich  2nicht  =(windschief  Geroder adeparallel  2in ")einer 
Ebene).")
            else:
  drawingst.write("Die  =Gleichungen  drawsind _nicht 3konsistent. dDie _coordinateGeraden _systemsind (gwindschief.")
 1else:
 ,st.write("Die  rGleichungen 1sind ,nicht  gkonsistent. 2Die ,Geraden  rsind 2windschief.")
 )st.subheader("3D-Koordinatensystem")
 
st.write("Legende:            G  st= .codeg1, (dH rawing= )g2, 
1 ```= 
Gerade 1, 
2 ---= 
Gerade 2")
 
drawing ###=  Ädraw_3d_coordinate_system(g1, nderr1, ungeng2,  inr2)
  Schrittst.code(drawing)
  3st.stop()
 
 
# Vertausche 
Zeile 11 .mit  **der RobustPivot-Zeile, heitfalls  beinötig
  \(if  rxpivot_row 1!=  =0:
  0st.write(f"Vertausche  \)Zeile  oder1  \(mit  rxZeile 2{pivot_row  =+  01},  \um )**ein   nicht-null 
Pivot   zu  -erhalten:")
  Ichmatrix[0],  habematrix[pivot_row]  das=  Gaumatrix[pivot_row], ßmatrix[0]
 -Vermatrix_display fahren=  sof"  anget pass st\n"
 ,matrix_display  dass+=  esf"  dynam{matrix[0][0]:>5.2f} isch{matrix[0][1]:>5.2f}  nach|  einem{matrix[0][2]:>5.2f}\n"
  nichtmatrix_display -null+=  Pivotf"  in{matrix[1][0]:>5.2f}  der{matrix[1][1]:>5.2f}  ersten|  Sp{matrix[1][2]:>5.2f}\n"
 altematrix_display  (+= fürf"  \({matrix[2][0]:>5.2f}  t{matrix[2][1]:>5.2f}  \| )){matrix[2][2]:>5.2f}\n"
  suchst.code(matrix_display)
 t
 ,pivot1  bevor=  esmatrix[0][0]
  Ze# ilenEliminieren operationvon ent  durchin fZeile ührt2 .und  Wenn3
  \(for  rxi 1in  =range(1,  03):
  \)if  (abs(matrix[i][0]) also>  \(1e-10:
  rfactor 1= [matrix[i][0] 0/ ]pivot1
  =st.write(f"Faktor  0für  \Zeile )),{i+1}:  wird{matrix[i][0]}  ge/ prü{pivot1} ft= ,{factor}")
  obfor  einej  anderein  Zerange(3):
 ilematrix[i][j]  ein-=  nichtfactor -null*  Pivotmatrix[0][j]
  hatelse:
 ,st.write(f"Zeile  und{i+1}  diehat  Zebereits ilen0  werdenin  entsprechSpalte end1,  vertkeine ausOperation chtnötig.")
 .
 
st.write("Nach   der  -Elimination:")
  Dassmatrix_display el= bef"  giltt  fürs  die\n"
  zweitematrix_display  Sp+= altef"  ({matrix[0][0]:>5.2f} für{matrix[0][1]:>5.2f}  \(|  s{matrix[0][2]:>5.2f}\n"
  \matrix_display )):+=  Wennf"  \({matrix[1][0]:>5.2f}  -{matrix[1][1]:>5.2f} rx| 2{matrix[1][2]:>5.2f}\n"
  =matrix_display  0+=  \)f"  ({matrix[2][0]:>5.2f} also{matrix[2][1]:>5.2f}  \(|  -{matrix[2][2]:>5.2f}\n"
 rst.code(matrix_display)
 2
 [# 0(2) ]Koeffizient  =von  0s  \in )),Zeile  wird2  nachauf  einem1  nichtbringen
 -nullst.write("(2)  PivotZiel:  inKoeffizient  denvon  vers blein ibGleichung endenII  Zeauf ilen1  gesbringen")
 uchtpivot_row .= 
1
 for 
i 2in .range(1,  **3):
 Sif pezabs(matrix[i][1]) ial> f1e-10:
 ällepivot_row  behand= elni
 **break
   else:
 
st.write("Alle   Koeffizienten  -von  Wenns  allein  KZeile oeff2 izund ienten3  vonsind  \(0.  tWir  \)prüfen  (die alsoGleichungen  \(auf  rKonsistenz.")
 1consistent [= 0True
 ]for  \i ),in  \(range(1,  r3):
 1if [abs(matrix[i][2]) 1> ]1e-10:
  \st.write(f"Gleichung ),{i+1}:  \(0  r= 1{matrix[i][2]} [→ 2Widerspruch!")
 ]consistent  \= ))False
  nullbreak
  sindif ,consistent:
  wirdt  das=  Systemmatrix[0][2]  nur/  nachmatrix[0][0]  \(if  smatrix[0][0]  \)!=  gel0 östelse ,0
  undst.write(f"Alle  dieGleichungen  Konssind istkonsistent, enzt  der=  Gleich{t}. ungenDa  wirds  genicht prüvorkommt, ftist .s 
frei.")
   st.write("Die  -Geraden  Wennschneiden  allesich  Knicht oeff(windschief izoder ientenparallel  vonin  \(einer  sEbene).")
  \)else:
  inst.write("Die  denGleichungen  versind blenicht ibkonsistent. endenDie  ZeGeraden ilensind  nullwindschief.")
  sindst.subheader("3D-Koordinatensystem")
 ,st.write("Legende:  wirdG  das=  Systemg1,  nurH  nach=  \(g2,  t1  \)=  gelGerade öst1, ,2  und=  dieGerade  Kons2")
 istdrawing enz=  wirddraw_3d_coordinate_system(g1,  ger1, prüg2, ftr2)
 .st.code(drawing)
 
st.stop()
 
 
# 3Vertausche .Zeile  **2 Numermit ischeder  StPivot-Zeile, abilitfalls ätnötig
 **if   pivot_row 
!=   1:
  -st.write(f"Vertausche  IchZeile  habe2  Schmit wellZeile en{pivot_row wer+ te1},  (um zein .nicht-null  BPivot .zu  \(erhalten:")
  1matrix[1], ematrix[pivot_row] -= 10matrix[pivot_row],  \matrix[1]
 ))matrix_display  eing= eff" ührtt ,s  um\n"
  numermatrix_display ische+=  Ungf" en{matrix[0][0]:>5.2f} au{matrix[0][1]:>5.2f} igkeiten|  zu{matrix[0][2]:>5.2f}\n"
  vermematrix_display iden+= ,f"  die{matrix[1][0]:>5.2f}  bei{matrix[1][1]:>5.2f}  Gle| it{matrix[1][2]:>5.2f}\n"
 kommmatrix_display ab+= eref" chn{matrix[2][0]:>5.2f} ungen{matrix[2][1]:>5.2f}  au| ft{matrix[2][2]:>5.2f}\n"
 retenst.code(matrix_display)
  können
 .pivot2 
=   matrix[1][1]
  -st.write(f"Dividiere  DieZeile  Fakt2 orendurch  für{pivot2}:")
  diefor  Zej ilenin operationrange(3):
 enmatrix[1][j]  werden/=  korpivot2
 rekt
  berematrix_display chnet= ,f"  undt  dies  Matrix\n"
  wirdmatrix_display  nach+=  jedemf"  Schritt{matrix[0][0]:>5.2f}  aktual{matrix[0][1]:>5.2f} isiert|  und{matrix[0][2]:>5.2f}\n"
  angematrix_display zeigt+= .f" 
{matrix[1][0]:>5.2f} {matrix[1][1]:>5.2f} 
| **{matrix[1][2]:>5.2f}\n"
 Unmatrix_display ver+= ändertf" :**{matrix[2][0]:>5.2f}   {matrix[2][1]:>5.2f} 
| -{matrix[2][2]:>5.2f}\n"
  Schrittst.code(matrix_display)
  1
  (# Ger(3) adEliminieren engvon leichs ungenin  aufZeile stellen1 )und  und3
  Schrittst.write("(3)  2Ziel:  (Eliminieren Parallelvon itäs tsin prüden fungGleichungen )I  sindund  exIII")
 aktfor  wiei  imin  urs[0, prü2]:
 ngif lichenabs(matrix[i][1])  Code> .1e-10:
   factor 
= -matrix[i][1]  Die/  Visualmatrix[1][1]
 isierungst.write(f"Faktor  (für 3Zeile D{i+1}: -K{matrix[i][1]} o/ ordin{matrix[1][1]} at= ens{factor}")
 ystemfor )j  undin  allerange(3):
  anderenmatrix[i][j]  Fun-= ktionenfactor  (* zmatrix[1][j]
 .else:
  Bst.write(f"Zeile .{i+1}  `hat vectorbereits _sub0 tractin `,Spalte  `2, vectorkeine _addOperation _scalarnötig.")
 `,
  `st.write("Nach drawder _Elimination:")
 3matrix_display d= _coordinatef" _systemt `)s  bleiben\n"
  unvermatrix_display ändert+= .f"   {matrix[0][0]:>5.2f} 
{matrix[0][1]:>5.2f} -|  Die{matrix[0][2]:>5.2f}\n"
  Strmatrix_display uktur+=  desf"  Codes{matrix[1][0]:>5.2f}  außer{matrix[1][1]:>5.2f} halb|  von{matrix[1][2]:>5.2f}\n"
  Schrittmatrix_display  3+=  bleibtf"  un{matrix[2][0]:>5.2f} ber{matrix[2][1]:>5.2f} ührt| .{matrix[2][2]:>5.2f}\n"
 
st.code(matrix_display)
 
 
# ###(4)  TestAnalyse fder älleStufenform
 st.write("(4) 
Analyse -der  **Stufenform")
 \(if  rxabs(matrix[2][0]) 1<  =1e-10  0and  \abs(matrix[2][1]) ),<  \(1e-10:
  rxif 2abs(matrix[2][2])  \< neq1e-10:
  0st.write("Die  \dritte ):**Zeile  Dasist  Ver0 fahren=  such0, tdas  einSystem  nichtist -nulllösbar.")
  Pivott  in=  dermatrix[0][2]  ersten/  Spmatrix[0][0] alteif  (abs(matrix[0][0]) z> .1e-10  Belse .None
  \(s  r= 1matrix[1][2]
 [st.write(f"t 1= ]{t},  \)s  oder=  \({s}")
  r
 1if [t 2is ]not  \None:
 ))#  undSchnittpunkt  führtberechnen
  dieschnittpunkt  Elimination=  korvector_add_scalar(g1, rektt,  durchr1)
 .st.write("Berechne 
den -Schnittpunkt  **mit \(t  rxin 1Gerade  =1:")
  0st.write(f"x  \= ),{g1[0]}  \(+  rx{t} 2*  ={r1[0]}  0=  \{schnittpunkt[0]}")
 ):**st.write(f"y  Das=  Ver{g1[1]} fahren+  erken{t} nt* ,{r1[1]}  dass=  die{schnittpunkt[1]}")
  erstest.write(f"z  Gleich= ung{g1[2]}  keine+  \({t}  t*  \{r1[2]} )-=  oder{schnittpunkt[2]}")
  \(st.write(f"Schnittpunkt:  s{schnittpunkt}")
  \st.subheader("3D-Koordinatensystem")
 )-st.write("Legende: KomG ponente=  hatg1, ,H  und=  prg2, ü1 ft=  dieGerade  Kons1, ist2 enz=  derGerade  Gleich2, ungX  (= zSchnittpunkt")
 .drawing  B= .draw_3d_coordinate_system(g1,  \(r1,  0g2,  =r2,  cschnittpunkt)
  \st.code(drawing)
 )).else:
 
st.write("Der -Koeffizient  **von Normt alein  FZeile älle1 :**ist  Funktion0, ierendas  weiterSystem hinist  kornicht rekteindeutig ,lösbar.")
  wiest.write("Die  zuvorGeraden .sind 
windschief.")
 st.subheader("3D-Koordinatensystem")
 
st.write("Legende: MitG  diesen=  Äg1, nderH ungen=  sollteg2,  das1  Gau= ßGerade -Ver1, fahren2  in=  SchrittGerade  32")
  nundrawing  kor= rektdraw_3d_coordinate_system(g1,  funktionr1, iereng2, ,r2)
  auchst.code(drawing)
  wennelse:
  \(st.write(f"Die  rxdritte 1Zeile  \)ist  oder0  \(=  rx{matrix[2][2]:.2f}, 2ein  \)Widerspruch.  nullDas  sindSystem ,hat  währendkeine  derLösung.")
  Restst.write("Die  desGeraden  Codessind  unverwindschief.")
 ändertst.subheader("3D-Koordinatensystem")
  bleibtst.write("Legende: .G = g1, H = g2, 1 = Gerade 1, 2 = Gerade 2")
 drawing = draw_3d_coordinate_system(g1, r1, g2, r2)
 st.code(drawing)
 else:
 st.write("Die dritte Zeile ist nicht in der Form 0 = c, das System ist nicht lösbar.")
 st.write("Die Geraden sind windschief.")
 st.subheader("3D-Koordinatensystem")
 st.write("Legende: G = g1, H = g2, 1 = Gerade 1, 2 = Gerade 2")
 drawing = draw_3d_coordinate_system(g1, r1, g2, r2)
 st.code(drawing)
