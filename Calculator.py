print("----------------------------------------------------") 
print("----------------------------------------------------") 
print("------------------Calculator------------------------")
print("----------------------------------------------------")
print("----------------------------------------------------")
ch="y"
while (ch=="y"):
    print("Choose any of the operations by entering they're Sr.no: ") 
    print("1. Addition") 
    print("2. Subtraction") 
    print("3. Multiplication") 
    print("4. Powers") 
    print("5. Root")    
    print("6. Percentage")
    print("7. Quadratic Equation")
    print("8. Conversions")
    print("9. 1/x")
    print("10. Currency Exchange")
    print("11. Temperature")
    print("12. Area of 2D shapes")
    print("13. Tables") 
    c=input("Enter your operation: ") 
#Square
    if c=="4": 
        sqr=int(input("Enter the Base number: ")) 
        sqr1=int(input("Enter your power: ")) 
        print("Your answer: ", sqr**sqr1) 
        
    #Root
    elif c=="5": 
        root=float(input("Enter your Base number: ")) 
        root1=float(input("Enter your root number: ")) 
        Trial=root//root 
        print("Your root:", Trial) 
        
    #Percentage
    elif c=="6":
        p=float(input("Enter the numerator: ")) 
        p2=float(input("Enter the denominator: ")) 
        print("Your percentage: ", (p/p2)*100,"%") 
        
    #Quadractic Equation Roots
    elif c=="7": 
        a2=int(input("Enter a value for a: ")) 
        b=int(input("Enter a value for b: ")) 
        c=int(input("Enter a value for c: ")) 
        D=b**2 -4*a2*c 
        if D==0: 
            print("Your Quadratic equation is equal to 0") 
        elif D>0: 
            print("Your Quadratic equation has two roots") 
        elif D<0: 
            print("Your Quadratic equation has no roots")
        eq1=-b+(b**2 -D)**0.5/(2*a2) 
        eq2= -b-(b**2 -D)**0.5/(2*a2)
        print("The roots are: ",eq1, eq2 ) 
        
    #Conversions
    elif c=="8": 
        print("Which of the following metrics would you like to choose") 
        print("Weights") 
        print("Distance") 
        Conversions=input("Enter your choice: ") 
        if Conversions=="Distance": 
            print("The following conversions are available:") 
            print("cm to m") 
            print("m to cm") 
            print("m to km") 
            print("km to m") 
            print("cm to km")
            print("km to cm")
            print("cm to mm")
            print("mm to cm") 
            con=input("Enter any of the conversions: ") 
            if con=="cm to m": 
                w=int(input("Enter a number in cm: "))
                ans=w/100 
                print("Your values in metres", ans ,"m") 
            elif con=="m to cm": 
                x=int(input("Your values in metres: "))
                ans2=x*100
                print("Your value: ", ans2,"cm") 
            elif con=="m to km": 
                y=int(input("Your value in metre: "))
                ans3=y/1000
                print("Your value: ", ans3, "km") 
            elif con=="km to m": 
                z=int(input("Your value in km: "))
                ans4=con*1000
                print("Your value: ", ans4, "m: ")  
            elif con=="cm to km": 
                h=int(input("Enter value in cm: "))
                ans6=h/100000
                print("Your value", ans6, "km") 
            elif con=="km to cm": 
                h2=int(input("Your value in km: ")) 
                ans7=h2*100000
                print("Your value: ", ans7, "cm")
            elif con=="cm to mm": 
                h3=int(input("Enter the value im cm: ")) 
                ans8=h3*10 
                print("Your value in cm: ", ans8, "mm") 
            elif con=="mm to cm": 
                h4=int(input("Your value in mm: "))
                ans9=h4/10
                print("Your value: ", ans9, "cm") 
            input("To continue press Ctrl+C and re-run the program")
        elif Conversions=="Weights": 
            print("The following conversions are avaiable: ") 
            print("g to kg") 
            print("kg to g") 
            p=input("Enter any one of the conversions: ") 
            if p=="g to kg": 
                p1=int(input("Enter the weight in g: "))
                pC=p1/1000 
                print("Your weight in kilograms: ", pC, "kg") 
            elif p=="kg to g": 
                p2=int(input("Enter the weight in kg: "))
                pC2=p2*1000 
                print("Your weight in grams: ", pC2, "g")
            
#1/x
    elif c=="9": 
        R=int(input("Enter value of x: ")) 
        ans5= 1/R
        print("Your result: ", ans5) 
        
        
#Currency Exchange 
    elif c=="10": 
        print("Which of the following Exchanges would you like to make")
        print("OMR to INR") 
        print("INR to OMR") 
        print("OMR to USD") 
        print("USD to OMR") 
        print("INR to USD") 
        print("USD to INR") 
        EX=input("Enter any one of the options: ") 
        if EX=="OMR to INR": 
            E=float(input("Enter amount in OMR:"))
            Ex=E*205 
            print("Your amount in INR,", Ex, "rupees") 
        elif EX=="INR to OMR":
            E1=float(input("Enter amount in INR: ")) 
            Ex2=E1/205 
            print("Your amount in OMR,", Ex2, "OMR") 
        elif EX=="OMR to USD": 
            E2=float(input("Enter you amount in OMR: "))
            Ex3=E2*2.6 
            print("Your amount in USD,", Ex3, "$") 
        elif EX=="USD to OMR":
            E3=float(input("Your amount in USD: ")) 
            Ex4=E3/2.6
            print("Your amount in OMR,", Ex4, "OMR") 
        elif EX=="USD to INR": 
            E4=float(input("Enter Your amount in USD: "))
            Ex5=E4/0.013
            print("Your amount in INR, ", Ex5, "rupees") 
        elif EX=="INR to USD": 
            E5=float(input("Your amount in INR: ")) 
            Ex6=E5*0.013
            print("Your amount in USD, ", Ex6, "$")  
        
#Temperature
    elif c=="11": 
        print("Choose any one of the conversions") 
        print("Celsius to Farenheit") 
        print("Farenheit to Celsius") 
        t=input("Enter the intials of the conversion: ") 
        if t=="C to F": 
            T1=float(input("Enter temperature in Celsius: "))
            t1=(T1*9/5)+32 
            print("Your temperature in Farenheit:", t1, "°F") 
        
        elif t=="F to C": 
            T2=float(input("Enter temperature in Farenheit: ")) 
            t2=(T2-32)*5/9 
            print("Your temperature in Celsius", t2, "°C")
         
    
#Area of 2D Shapes
    elif c=="12": 
        print("Which of the following Shape's area would you like to find") 
        print("Square") 
        print("Circle") 
        print("Rectangle") 
        print("Triangle (only 90°)") 
        A=input("Enter one of the shapes: ")
        if A=="Square": 
            Sq=float(input("Enter the length of one side of the square: ")) 
            SA= Sq*Sq 
            print("The area of the square: ", SA) 
        elif A=="Circle": 
            C=float(input("Enter the radius of the circle: ")) 
            CA= 2*3.14*C 
            print("The area of the circle is: ", CA)
        elif A=="Rectangle": 
            l=float(input("Enter the length of the rectangle: ")) 
            B=float(input("Enter the breadth of the rectangle: "))
            RA=l*B
            print("The area of the rectangle is: ", RA) 
        elif A=="Triangle": 
            B2=float(input("Enter the length of the base of the triangle: ")) 
            h5=float(input("Enter the height of the triange: ")) 
            TA=0.5*B2*h5
            print("The area of the triangle is:", TA) 
             
#Tables 
    elif  c=="13": 
        n=int(input("Enter the number for which you would like to have tables for: "))
        for i in range (1,11):
            print(n, "x", i, "=", n*i) 
         
    
    
#Simple Operations 
    if c=="1":
        a=float(input("Enter your number: ")) 
        b=float(input("Enter your second number: ")) 
        print("Your sum: ", a+b)
    elif c=="2": 
        a=float(input("Enter your number: ")) 
        b=float(input("Enter your second number: "))
        print("Your answer:",  a-b) 
    elif c=="3": 
        a=float(input("Enter your number: ")) 
        b=float(input("Enter your second number: "))
        print("Your product: ", a*b) 
    ch=input("Type y to continue: ")


