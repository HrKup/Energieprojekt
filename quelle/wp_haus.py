from figs import *
def badge(ax,x,y,k):
    ax.add_patch(Circle((x,y),0.42,fc=INK,ec='white',lw=1.5,zorder=10)); ax.text(x,y,str(k),ha='center',va='center',color='white',fontsize=13,fontweight='bold',zorder=11)
def coil(ax,x0,x1,y0,y1,n,color,lw=3):
    ys=np.linspace(y0,y1,n); xs=[x0 if i%2==0 else x1 for i in range(n)]; ax.plot(xs,ys,color=color,lw=lw,solid_joinstyle='round',zorder=4)
def wp_haus():
    fig,ax=plt.subplots(figsize=(11,7.4)); ax.set_xlim(-1.6,22); ax.set_ylim(-5.0,13.4); ax.axis('off')
    PH='#E8590C'; PC='#1971C2'; WH='#C92A2A'; WC='#4DABF7'
    # Boden, Himmel
    ax.add_patch(Rectangle((-1.6,-0.3),23.6,1.3,fc='#E9DCC9',ec='none'))
    ax.add_patch(Rectangle((-1.6,1.0),10.2,12.2,fc='#E7F5FF',ec='none'))
    ax.text(-1.2,12.4,'draußen: kalte Luft, z. B. 0 °C',fontsize=13,color=PC,fontweight='bold')
    # Haus
    ax.add_patch(Rectangle((8.6,1.0),12.6,7.4,fc='#FFF4E6',ec=INK,lw=2.5))
    ax.add_patch(Polygon([(8.0,8.4),(14.9,12.6),(21.8,8.4)],fc='#FFE8CC',ec=INK,lw=2.5))
    ax.add_patch(Rectangle((8.6,5.0),12.6,0.25,fc='#CED4DA',ec=INK,lw=1))
    ax.text(14.9,10.0,'im Haus: 20 °C',ha='center',fontsize=13,color=WH,fontweight='bold')
    # Außengerät
    ax.add_patch(FancyBboxPatch((1.0,1.2),5.2,5.6,boxstyle='round,pad=0.1',fc='#F8F9FA',ec=INK,lw=2))
    ax.text(2.2,7.2,'Außengerät',ha='center',fontsize=13,fontweight='bold',color=INK)
    ax.add_patch(Circle((2.6,4.6),1.25,fc='white',ec=INK,lw=1.5))
    for a in (90,210,330):
        r=np.radians(a); ax.add_patch(Ellipse((2.6+0.55*np.cos(r),4.6+0.55*np.sin(r)),1.0,0.4,angle=a,fc='#ADB5BD',ec=INK,lw=1))
    coil(ax,1.25,1.75,1.6,6.4,11,PC)  # Verdampfer-Lamellen links
    badge(ax,1.5,0.6,1)
    # Luft rein
    for y in (3.4,4.6,5.8): arrow(ax,(-1.0,y),(1.1,y),color='#3BC9DB',lw=3,ms=20)
    ax.text(-0.6,8.3,'Umweltwärme\naus der Luft',fontsize=11,color='#0C8599',ha='left',va='bottom',fontweight='bold')
    # Verdichter
    ax.add_patch(Circle((5.0,5.3),0.75,fc='#FFE066',ec=INK,lw=1.8,zorder=5)); badge(ax,5.0,6.5,2)
    
    # Strom
    arrow(ax,(7.6,8.4),(5.75,6.0),color='#F2C200',lw=4,ms=22)
    ax.text(7.7,8.5,'Strom',ha='center',va='bottom',fontsize=12,fontweight='bold',color='#B08900')
    # Ventil
    vx,vy=5.0,2.2
    ax.add_patch(Polygon([(vx-0.55,vy+0.4),(vx-0.55,vy-0.4),(vx+0.55,vy+0.4),(vx+0.55,vy-0.4)],closed=True,fc='white',ec=INK,lw=1.5,zorder=5)); badge(ax,vx,1.25,4)
    # Inneneinheit mit Verflüssiger
    ax.add_patch(FancyBboxPatch((9.4,1.3),2.8,3.0,boxstyle='round,pad=0.08',fc='#F8F9FA',ec=INK,lw=2))
    ax.text(10.8,4.45,'Innengerät',ha='center',fontsize=11,fontweight='bold')
    coil(ax,9.8,10.5,3.5,1.8,9,PH); badge(ax,9.4,1.3,3)
    # Kältemittel-Leitungen
    ax.plot([1.75,1.75,4.25],[6.4,6.4,5.3] if False else [6.4,6.4,6.4],color=PC,lw=0)
    ax.plot([1.75,4.25],[6.4,6.4],color=PC,lw=4,zorder=3); ax.plot([4.25,4.25],[6.4,5.55],color=PC,lw=4,zorder=3)  # Gas kalt zum Verdichter
    ax.plot([5.75,7.2,7.2,9.8,9.8],[5.3,5.3,3.5,3.5,3.5],color=PH,lw=4.5,zorder=3)  # heißes Gas ins Haus
    ax.plot([10.5,10.5,8.0],[1.8,1.6,1.6],color='#F783AC',lw=4,zorder=3); ax.plot([8.0,8.0,5.55],[1.6,2.2,2.2],color='#F783AC',lw=4,zorder=3)  # flüssig zurück zum Ventil
    ax.plot([4.45,3.4,3.4,1.25],[2.2,2.2,1.6,1.6],color=PC,lw=4,zorder=3)  # kalt in den Verdampfer
    arrow(ax,(6.2,5.3),(7.0,5.3),color=PH,lw=0,ms=22); arrow(ax,(8.3,3.5),(9.1,3.5),color=PH,lw=0,ms=22)
    arrow(ax,(7.6,1.6),(6.9,1.6),color='#F783AC',lw=0,ms=0.1) 
    arrow(ax,(7.0,2.2),(6.2,2.2),color='#F783AC',lw=0,ms=22); arrow(ax,(3.2,1.6),(2.4,1.6),color=PC,lw=0,ms=22)
    arrow(ax,(2.6,6.4),(3.5,6.4),color=PC,lw=0,ms=22)
    ax.text(7.4,5.65,'heiß',fontsize=10,color=PH,ha='center',fontweight='bold'); ax.text(2.9,2.65,'sehr kalt',fontsize=10,color=PC,ha='center',fontweight='bold'); ax.text(7.7,2.55,'flüssig',fontsize=10,color='#D6336C',ha='center',fontweight='bold')
    # Heizkreis
    def heizk(x,y):
        ax.add_patch(Rectangle((x,y),2.4,1.6,fc='white',ec=INK,lw=1.5,zorder=4))
        for i in range(7): ax.plot([x+0.2+i*0.33]*2,[y+0.15,y+1.45],color=GREY,lw=1.2,zorder=5)
        for k in range(3): 
            xs=np.linspace(x+0.4+k*0.8,x+0.4+k*0.8,2); ax.plot(x+0.3+k*0.8+0.15*np.sin(np.linspace(0,6.3,20)),np.linspace(y+1.8,y+2.7,20),color=WH,lw=1.6,zorder=5)
    heizk(17.6,1.6); heizk(17.6,5.6)
    ax.plot([12.2,13.5,13.5,17.6],[3.2,3.2,2.4,2.4],color=WH,lw=3.5); ax.plot([13.5,13.5,17.6],[3.2,6.4,6.4],color=WH,lw=3.5)
    ax.plot([12.2,14.2,14.2,17.6],[1.8,1.8,1.9,1.9],color=WC,lw=3.5); ax.plot([14.2,14.2,17.6],[1.9,5.9,5.9],color=WC,lw=3.5)
    arrow(ax,(15.4,2.4),(16.4,2.4),color=WH,lw=0,ms=20); arrow(ax,(15.4,6.4),(16.4,6.4),color=WH,lw=0,ms=20)
    arrow(ax,(16.4,1.9),(15.4,1.9),color=WC,lw=0,ms=20); arrow(ax,(16.4,5.9),(15.4,5.9),color=WC,lw=0,ms=20)
    ax.text(17.4,3.3,'Heizkörper',ha='right',fontsize=10.5); ax.text(17.4,7.1,'Heizkörper',ha='right',fontsize=10.5)
    ax.text(15.8,4.3,'Heizungswasser',ha='center',fontsize=10.5,color=WH,fontweight='bold')
    # Bauteil-Namen
    ax.text(1.0,0.6,'Verdampfer',ha='right',va='center',fontsize=10.5,fontweight='bold')
    ax.text(5.0,7.25,'Verdichter',ha='center',va='center',fontsize=10.5,fontweight='bold')
    ax.text(5.55,1.25,'Ventil',ha='left',va='center',fontsize=10.5,fontweight='bold')
    ax.text(11.35,2.6,'Ver-\nflüssiger',ha='center',va='center',fontsize=10.5,fontweight='bold')
    # Schritte
    st=['1  Verdampfer: Das sehr kalte Kältemittel nimmt Wärme aus der Außenluft auf und verdampft.',
        '2  Verdichter: Strom treibt ihn an. Er presst das Gas zusammen, dabei wird es heiß.',
        '3  Verflüssiger: Im Haus gibt das heiße Gas seine Wärme an das Heizungswasser ab und wird wieder flüssig.',
        '4  Ventil: Der Druck sinkt, das Kältemittel wird sehr kalt und fließt wieder zum Verdampfer.']
    for i,t in enumerate(st): ax.text(-1.2,-0.9-i*0.75,t,fontsize=11.5,va='center',color=INK)
    # Legende Leitungen
    for i,(c,t) in enumerate([(PC,'Kältemittel kalt'),('#F783AC','Kältemittel flüssig'),(PH,'Kältemittel heiß'),(WH,'Heizungswasser warm'),(WC,'Heizungswasser abgekühlt')]):
        x=-1.2+(i%3)*7.4; y=-4.0-(i//3)*0.7
        ax.plot([x,x+0.8],[y,y],color=c,lw=4,solid_capstyle='butt'); ax.text(x+1.0,y,t,va='center',fontsize=10)
    save(fig,'wp_haus')
wp_haus()
