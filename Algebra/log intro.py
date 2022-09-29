import numpy
from manim import *
import math
import manimpango

"""
Title: What is "log"?

This. is log. If you've ever played around with an advanced calculator, you've probably come across this 
button labeled with the silly name "log". You may have , by chance, realized that this "button"
essentially just returns the number of zero's that there are in the number that you subsequently
input after. Let's call this subsequent number "the argument".
"""

class LogIntro(Scene):
    def construct(self):
        waitVar = 5
        logEx = MathTex(
            r"\log \left(",
            r"1",
            r"000",
            r"\right)",
            r"= 3"
        ).scale(1.5)
        logEx[4].color = BLUE

        firstEx = MathTex(r"\log ()").scale(5)
        self.add(firstEx)
        self.wait(8)
        self.play(Circumscribe(firstEx))
        self.wait(6)

        def UpAndAway(mobject, t):
            mobject.move_to([0, t*2, 0])
            mobject.set_opacity(1-t)

        theArgument = Text('"Argument"', font_size=30, color=YELLOW)
        theArgument.next_to(logEx, UP*2)
        self.play(UpdateFromAlphaFunc(firstEx, UpAndAway, run_time=1), Write(logEx[:4])) 
        self.wait(1)      
        self.play(Indicate(logEx[2], run_time=3))
        self.play(Write(logEx[4]))
        self.wait(2)
        self.play(Circumscribe(logEx[1:3]), Write(theArgument), run_time=4)
        self.play(FadeOut(theArgument), run_time=0.5)

        logEx2 = MathTex(
            r"\log \left(1",
            r"000000",
            r"\right)",
            r"=6"
        ).scale(1.5)
        logEx2[3].color = BLUE
        
        self.wait(2)
        self.play(logEx.animate.shift(UP))
        logEx2.next_to(logEx, DOWN)
        
        self.play(Write(logEx2[:3]))

        self.play(Indicate(logEx2[1], run_time=3))
        self.play(Write(logEx2[3]))

        #to the power of ten demo

        ofTenDemo1 = MathTex(
            r"\log \left(1000\right)",
            r"=\log \left(10^3\right)",
            r"= 3"
        ).scale(1.5)
        ofTenDemo1[1].color =GREEN
        ofTenDemo1[2].color =BLUE

        ofTenDemo2 = MathTex(
            r"\log (1000000)",
            r"=\log (10 ^ 6)",
            r"=6"
        ).scale(1.5)
        ofTenDemo2[1].color =GREEN
        ofTenDemo2[2].color =BLUE

        ofTenDemo1.move_to(logEx.get_center())
        ofTenDemo2.move_to(logEx2.get_center())
        self.wait(6)
        self.play(ReplacementTransform(logEx, ofTenDemo1), ReplacementTransform(logEx2, ofTenDemo2))
        self.wait(5)

        #argument that is not a power of 10

        logEx3 = MathTex(
            r"\log(500)",
            r"=\log (10^{2.6989...})",
            r"=2.6989..."
        ).next_to(ofTenDemo2, DOWN).scale(1.5)
        logEx3[1].color=GREEN
        logEx3[2].color=BLUE

        logEx4 = MathTex(
            r"\log(50) ", 
            r" = \log(10^{1.6989...}) ",
            r"= 1.6989..."
            ).next_to(logEx3, DOWN).scale(1.5)
        logEx4[1].color=GREEN
        logEx4[2].color=BLUE


        self.play(Write(logEx3), Write(logEx4), run_time=2)
        self.wait(6)

        logExamples = VGroup(ofTenDemo1, ofTenDemo2, logEx3, logEx4)
    
        self.play(logExamples.animate.shift(UP*2))

        #less than 10

        logEx5 = MathTex(
            r"\log(1)", r" = \log(10^0)", r"=0"
        )
        logEx5[1].color=GREEN
        logEx5[2].color=BLUE

        logEx6 = MathTex(
            r"\log(0.1)", r"=\log(10^{-1})", r"=-1"
        )
        logEx6[1].color=GREEN
        logEx6[2].color=BLUE

        logExamples2 = VGroup(logEx5, logEx6).arrange(DOWN).next_to(logExamples, DOWN*2.1).scale(1.5)
        self.play(Write(logExamples2))
        self.wait(waitVar)
        
        logAllExamples=VGroup(ofTenDemo1, ofTenDemo2, logEx3, logEx4, logEx5, logEx6)
        self.play(logAllExamples.animate.scale(0.7))
        self.play(logAllExamples.animate.shift(UP*0.5))
        #generalize as function

        logFunc = MathTex(r"f(x)=\log (x)")
        logFunc.scale(1.5).next_to(logAllExamples, DOWN)
        self.play(Write(logFunc))
        self.wait(3)

        self.play(FadeOut(logAllExamples))

        ax = Axes(tips=False, y_axis_config={"include_numbers": True, "font_size": 30}, 
        x_axis_config={"include_numbers": True, "font_size": 35}, x_range=[0, 100, 10], y_range=[-3, 3])
        natLogEx = ax.plot(lambda x: np.log10(x), x_range=[0.0001, 100, 0.01], color=BLUE)
        self.play(logFunc.animate.shift(RIGHT*2.5, UP*2.5), Create(ax, run_time=1), Create(natLogEx, run_time=2))
  
        myDot = Dot(point=[ax.input_to_graph_point(x=1, graph=natLogEx)], radius=0.065)
        myDot2 = Dot(point=[ax.input_to_graph_point(x=10, graph=natLogEx)], radius=0.065)
        myDot3 = Dot(point=[ax.input_to_graph_point(x=100, graph=natLogEx)], radius=0.065)
        myLabel1 = Tex("(1, 0)", font_size=25).move_to([myDot.get_x() + 0.3, myDot.get_y()-0.2, 0])
        myLabel2 = Tex("(10, 1)", font_size=25).move_to([myDot2.get_x()+0.1, myDot2.get_y()-0.25, 0])
        myLabel3 = Tex("(100, 2)", font_size=25).move_to([myDot3.get_x() + 0.1, myDot3.get_y()+0.2, 0])

        a = VGroup(myDot, myDot2, myDot3)
        b = VGroup(myLabel1, myLabel2, myLabel3)
        self.play(Create(a), Write(b))
        self.wait(3)
        self.play(FadeOut(a, b, logFunc, ax, natLogEx))


"""
If the argument given is 1000, it is 3, if it is 1000000, it is 6, and so on.
That's only part of it though. this funky expression is actually saying "10 to the what power equals the argument?"
So, if the argument is 1000, that equates to 10 ^ 3. 10^ exactly 3rd power is equal to the argument, so the expression is equal to 3.  
The power does not have to be an integer, it can also be a rational or irrational number.

So this expression can take in an argument that is not an integer power of 10, but *any* number that is a power of 10.

This so called log can be represented as a function, again, saying 10 to the what power equals x? 

The plotted graph of our function checks out. For example, f(x) at x = 1 is 0, because 10 ^ 0 is 1,
f(x) at x = 10 is 1, and f(x) at x = 100 is 2. 
notice how the function is undefined at x values less than 0? this is because there is no y that can make a negative x.
for instance, if x was -1, no matter how hard you try, you will find that there is no power of 10 that can make a -1.
"""

class OfDifferentBases(Scene):
    def construct(self):

        bassFiveEx = MathTex(r"5^", r"x", r"=", r"25")
        bassFiveEx[0].color=GREEN
        bassFiveEx[1].color=BLUE
        bassFiveEx[3].color=PURPLE
        bassTwoEx = MathTex(r"2^", r"x", r"=", r"1/16")
        bassTwoEx[0].color=GREEN
        bassTwoEx[1].color=BLUE
        bassTwoEx[3].color=PURPLE
        bassThreeEx = MathTex(r"3^", r"x", r"=", r"19683")
        bassThreeEx[0].color=GREEN
        bassThreeEx[1].color=BLUE
        bassThreeEx[3].color=PURPLE
        differentBases = VGroup(bassFiveEx, bassTwoEx, bassThreeEx).arrange(DOWN)

        logBassFiveEx = MathTex(r"\log", r"_5", r"(25)", r"=", r"x", r"=", r"2")
        logBassFiveEx[1].color=GREEN
        logBassFiveEx[2].color=PURPLE
        logBassFiveEx[4].color=BLUE
        logBassFiveEx[6].color=BLUE
        logBassTwoEx = MathTex(r"\log", r"_2", r" (1/16)", r"=", r"x", r"=", r"-4")
        logBassTwoEx[1].color=GREEN
        logBassTwoEx[2].color=PURPLE
        logBassTwoEx[4].color=BLUE
        logBassTwoEx[6].color=BLUE
        logBassThreeEx = MathTex(r"\log", r"_3", r" (19683)", r"=", r"x", r"=", r"9")
        logBassThreeEx[1].color=GREEN
        logBassThreeEx[2].color=PURPLE
        logBassThreeEx[4].color=BLUE
        logBassThreeEx[6].color=BLUE
        logBases = VGroup(logBassFiveEx, logBassTwoEx, logBassThreeEx).arrange(DOWN)

        natLogEx = MathTex(r"\log_", r"{10}", r"(100)", r"=", r"2 \quad", r"\Rightarrow \quad \log 100=2").next_to(logBases, DOWN)
        natLogEx[1].color = GREEN
        natLogEx[2].color=PURPLE
        natLogEx[4].color=BLUE
        natLogEx[5].color=GREEN
        natLogEx.shift(RIGHT*2)

        bassLabel = Tex('"Base"', font_size=30, color=YELLOW).move_to([bassFiveEx.get_x()-0.95, bassFiveEx.get_y()+0.46, 0])
        bassCircle = Circle(radius=0.2, color=YELLOW).move_to(logBassFiveEx[1].get_center())

        self.play(Write(differentBases))
        self.wait(10)

        def TransformThenWrite(mobject1, mobject2, mobject3, lagRatio=0):
            self.play(Transform(mobject1, mobject2))
            self.wait(lagRatio)
            self.play(Write(mobject3))

        self.play(Transform(differentBases[0], logBases[0][:5]))
        self.wait(3)
        self.play(Flash(logBases[0][1]), run_time=2)
        self.wait(3)
        self.play(Write(bassLabel), Create(bassCircle))
        self.wait(4)
        self.play(FadeOut(bassLabel, bassCircle))
        self.wait(2)
        self.play(Write(logBases[0][5:7]))
        
        self.wait(1)

        TransformThenWrite(differentBases[1], logBases[1][:5], logBases[1][5:7], 2)
        self.wait(2)
        TransformThenWrite(differentBases[2], logBases[2][:5], logBases[2][5:7], 2)

        #natlog
        self.wait(2)
        self.play(Write(natLogEx[:5]))
        self.wait(3)
        self.play(natLogEx[:5].animate.shift(LEFT * 2))
        natLogEx[5].shift(LEFT*2)
        self.play(Write(natLogEx[5]))
        self.wait(4)
        natLogExclamation = Tex("Common Logs!").next_to(natLogEx, DOWN)
        natLogExclamation.color=GREEN
        self.play(Write(natLogExclamation))
        self.wait(5)
        self.play(FadeOut(natLogEx, differentBases, logBases, natLogExclamation))
        self.wait(2)

        #different functions
        ax = Axes(tips=False, y_axis_config={"include_numbers": True, "font_size": 30}, 
        x_axis_config={"include_numbers": True, "font_size": 35}, x_range=[0, 50, 5], y_range=[-5, 5])
        natLogGraph = ax.plot(lambda x: math.log10(x), x_range=[0.0000001, 50, 0.01], color=BLUE)
        log5Graph = ax.plot(lambda x: math.log(x, 5), x_range=[0.00001, 50, 0.01], color=BLUE)
        log3Graph = ax.plot(lambda x: math.log(x, 3), x_range=[0.0001, 50, 0.01], color=BLUE)
        log2Graph = ax.plot(lambda x: math.log(x, 2), x_range=[0.0001, 50, 0.01], color=BLUE)
        whatGraphIsThis = MathTex(r"f(x)=\log (x)", r" f(x)=\log_5 (x)", r" f(x)=\log_3 (x)", r" f(x)=\log_2 (x)")
        for i in range(4):
            whatGraphIsThis[i].move_to([-3.9, -0.87, 0])

        waitInterval=1
        self.play(Create(ax, run_time=1), Create(natLogGraph, run_time=2), Write(whatGraphIsThis[0], run_time=0.5))
        self.wait(waitInterval)
        self.play(ReplacementTransform(natLogGraph, log5Graph), ReplacementTransform(whatGraphIsThis[0], whatGraphIsThis[1]))
        self.wait(waitInterval)
        self.play(ReplacementTransform(log5Graph, log3Graph), ReplacementTransform(whatGraphIsThis[1], whatGraphIsThis[2]))
        self.wait(waitInterval)
        self.play(ReplacementTransform(log3Graph, log2Graph), ReplacementTransform(whatGraphIsThis[2], whatGraphIsThis[3]))
        self.wait(1)
        self.play(FadeOut(log2Graph, whatGraphIsThis[3], ax))

"""
But as it turns out, this isn't the full extent of what a logarithm is.
We should also be able to find whatever number that, to a power, would equal the argument, right?
For example, we can also find 5 to whatever power that equals 25, 2 to whatever power that equals 1/16, 3 to 
whatever power that equals 19683, and so on. 
So, lets extend our definition of the logarithm.
(examples)

We express this concept in the logarithmic world by writing a subscript next to the letter g of log.
The subscript is referred to as the base. Easy enough to remember, right?
these expressions are telling us to find a number that, when the base is equipped with that certain number as a power,
the base would equal the argument. For example, in the first equation we want to find 5 to what power would equal 
the argument. This is the full definition of a logarithm.

We read the logarithms by saying, log base a of b.
Hence, if the base is 5, we read "log base 5 of 25 is x, which is 2."
or if the base is 2, we read "log base 2 of 1/16 is x, which is -4."
if the base is 3, we read "log base 3 of 19683 is x, which is 9."

But if our base is 10, conventionally we *omit* the 10. That is why there is nothing wrong with the
expressions that I showed you at the beginning of the video.
These expressions, where the bass is 10, are called "common logs." Because it is so common in some areas of math, 
namely engineering, to take a logarithm of base 10, we have an entire name for them.

Here are the new functions that you can make with this additional superpower of adding a base to the logarithm.
With some thought, I think we can see why exactly making the base smaller would actually *increase* the y value instead
of decreasing it. We will cover more about this in the next video.
"""

class WorkedExample(Scene):
    def construct(self):
        question = Tex("What is ", "$\\log_4 (32)$", "? Pause the video and try it yourself!")
        question.move_to([0, 3.5, 0])

        self.wait(2)
        self.play(Write(question), run_time=2)
        self.wait(3)

        #solution
        questionTrans = MathTex(r"\log_4 (32)").move_to([0, 1.5, 0])
        questionPartTwo = MathTex(r"=\log_4 \left(", r" 4\cdot4\cdot2", r"\right)").next_to(questionTrans, DOWN)
        questionPartTwo[1].color = PURPLE
        questionPartThree = MathTex(r"=\log_4 \left(", r"4^2\cdot2", r"\right)").move_to(questionPartTwo.get_center())
        questionPartThree[1].color=PURPLE
        questionPartFour = MathTex(r"=\log_4 \left(", r"4^2\cdot4^{0.5}", r"\right)").move_to(questionPartTwo.get_center())
        questionPartFour[1].color=PURPLE
        questionPartFive = MathTex(r"=\log_4 \left(", r"4^{2.5}", r"\right)").move_to(questionPartTwo.get_center())
        questionPartFive[1].color=PURPLE  
        questionParts = VGroup(questionTrans, questionPartTwo, questionPartThree, questionPartFour, questionPartFive)

        self.play(FadeOut(question[0:3:2]), question[1].animate.move_to([0, 1.5, 0]))
        self.play(ReplacementTransform(question[1], questionTrans[0]))
        self.wait(2)
        self.play(Write(questionPartTwo))
        self.wait(2)
        self.play(ReplacementTransform(questionPartTwo, questionPartThree))
        self.wait(2)
        self.play(ReplacementTransform(questionPartThree, questionPartFour))
        self.wait(2)
        self.play(ReplacementTransform(questionPartFour, questionPartFive))
        self.wait(2)

        #its likely that I will cut this out, and instead do an unsmooth transition with no fading if I think it looks better
        self.play(FadeOut(questionTrans, questionPartFive))




"""
**What is log_4(32)? Pause the video and try it yourself!**

asking what the log bass 4 of 32 is equivalent to saying 4 to *what* power equals 32?
so, after looking at this problem, we can see that the answer HAs to be between 2 and 3.
If log bass 4 of x is 2, then x is 16, and if log bass 4 of x is 3, then x is 64.
In this problem, x, which is 32, is greater than 16 and less tham 64.

lets break this problem apart. log bass 4 of 32 is the same thing as taking log bass 4 of 4 * 4 * 2. 
So we are essentially trying to find 4 to the *what* power equals 4 * 4 * 2. well, we know that 4 to the power 
of 2 is 4 * 4. and we also know, hopefully, that 4 to the power of 1/2 is the square root of 4, or 2.
So, log_4(32) is the same thing as log_4(4^2.5)
therefore, log_4(32) is 2.5.

So, it might be good intuition to think of it like this. The logarithm is just asking you how many times
you have to multiply that base by itself to reach the argument. If we are asked to find the natural log of 100, 
we have to multiply 10 twice, so the natural log of 100 is 2. And in this example, we have to multiply 4 exactly 
2.5 times, so the log base 4 of 32 is 2.5. This intuition gets a little convoluted once we have an irrational 
number of times that we have to multiply the base by itself. as shown earlier, its sort of hard to wrap your head 
around the fact that 10 multiplied by itself, 1.6989 times is 50... but I think it does make some sense even after that. 
"""

class SupposeWeHave(Scene):
    def construct(self):
        textA = Tex("Logarithms <3 Exponentials!", color=LIGHT_PINK)

        suppose = MathTex("y=2^x", color = BLUE).move_to([2.5, 2.3, 0])
        inverse=MathTex("x=2^y", color = GREEN).next_to(suppose, DOWN*2)
        inverse2=MathTex("y=\log_2 x", color=GREEN).move_to(inverse.get_center())

        ax = Axes(tips=False, y_axis_config={"include_numbers": True, "font_size": 25}, 
        x_axis_config={"include_numbers": True, "font_size": 25}, x_range=[-5, 50, 10], y_range=[-5, 50, 10])
        logGraph=ax.plot(lambda x: math.log2(x), x_range=[0.0001, 50, 0.01], color = GREEN)
        expGraph=ax.plot(lambda x: 2 ** x, x_range= [-50, 5.6438], color = BLUE)

        self.play(Write(textA))
        self.wait(10)
        
        self.remove(textA) 
        self.play(Create(ax, run_time=1), Create(logGraph, run_time=2), Create(expGraph, run_time=2))

        self.play(Write(suppose))
        self.wait(2)
        self.play(Write(inverse))
        self.wait(2)
        self.play(Transform(inverse, inverse2))
        self.wait(2)



"""
The final thing that I want to chime into this introduction is that exponential and logarithmic functions are best friends.
For one thing, whenever we need to solve logarithmic equations,
we can use the tools of exponents to aid the process. Conversely, we will also see that logarithms are an extremely 
handy tool in solving expoNENtial equations in the videos to come. But for another, exponential and logarithmic 
functions are inverses of each other. To illustrate, suppose we have 2 ^ x as a given exponential function. 
in this equation, the y is whatever 2 ^ x is. In its inverse, the x would be whatever 2 ^ y is. Rearranging, 
this is the same thing as the equation log_2(x) = y In other words, the logarithmic function IS the inverse of an
exponential function. That's all folks! that is your fundamentals of logarithms for you. 
In the videos to come, I will show you the transformations of the logarithmic function,
the properties of the logarithmic function, and this special constant, e. See you there!
"""


class SmileyFace(Scene):
    def construct(self):
        tex = Text(":D", font="Open Sans")
        self.add(tex)
        self.wait(1)

class Thumbnail(Scene):
    def construct(self):
        ax = Axes(tips=False, y_axis_config={"include_numbers": False, "font_size": 30}, 
        x_axis_config={"include_numbers": False, "font_size": 30}, x_range=[-5, 50, 10], y_range=[-5, 50, 10])
        ax.shift(LEFT * 0.2)
        logGraph=ax.plot(lambda x: math.log2(x), x_range=[0.0001, 50, 0.01], color = GREEN)
        expGraph=ax.plot(lambda x: 3 ** x, x_range= [-50, 3.56087679], color = LIGHT_PINK)
        matTex = MathTex(r"\log_A \left(A", r"^{x}", r"\right) = ", "x", font_size=150).shift(RIGHT*0.6)
        matTex[1].color=BLUE
        matTex[3].color=BLUE
        self.add(matTex)
        self.add(ax, logGraph, expGraph)

class ThumbnailTake2(Scene):
    def construct(self):
        ax = Axes(tips=False, y_axis_config={"include_numbers": False, "font_size": 30}, 
        x_axis_config={"include_numbers": False, "font_size": 30}, x_range=[-5, 50, 10], y_range=[-5, 50, 10])
        ax.shift(LEFT * 0.2)
        logGraph=ax.plot(lambda x: math.log2(x), x_range=[0.0001, 50, 0.01], color = GREEN)
        expGraph=ax.plot(lambda x: 3 ** x, x_range= [-50, 3.56087679], color = LIGHT_PINK)
        matTex = MathTex(r"\log \left(100", r"^{2}", r"\right) = ", "2", font_size=150).shift(RIGHT*0.6)
        matTex[1].color=BLUE
        matTex[3].color=BLUE
        self.add(matTex)
        self.add(ax, logGraph, expGraph)

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = SmileyFace()
    scene.render()
