from manim import * 

class ShowGraph(Scene):
    def func(self, x):
        return  ((x**3)+ 3*(x**2) - 6*x - 12)/4
    
    def construct(self):
        plane = NumberPlane(
            x_range=[-2, 13, 1],
            y_range=[-2, 6, 1]
        )
        
        graph = FunctionGraph(
            self.func,
            color=RED
        )
        
        self.add(plane)
        self.play(Create(graph, run_time=2))

        dot_A = Dot(
            
        )