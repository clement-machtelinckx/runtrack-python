def triangle_possible(a, b, c):
    
    if a + b > c and a + c > b and b + c > a:
        print("les longueur peuvent crée un triangle")
        
        if a == b and c == b:
            print("c'est un triangle équilaterale")
            
        elif a == b or b == c or a == c:
            
            if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
                print("triangle rectangle isocele")
                
            else:
                print("triangle isocel")
        
        elif  a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
            print("triangle rectangle")
            
        else:
            print("tiangle quelquonque")
            
    else:
        print("ces longueurs ne peuvent pas réalisé un triangle")
        
triangle_possible(20, 20, 12)
triangle_possible(20, 20, 20)
triangle_possible(5, 4, 3)
triangle_possible(10, 21, 18)