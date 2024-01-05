class ResolutionSolver:
   """
            It helps calculating with and height to be used depending on the base resolution of the model.
            It calculates by any aspect ratios, such as 1:1, 2:3, 16:9 and so on, so don't need to recauculate
            every time, just adjust the base resolution you want to use, like 512, 768, 1024 or others.
        """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        
        return {
            "required": {
                "base": ("INT",{"display":"number"}),
                "aspect": ("STRING",
                        {
                            "multiline":False
                        }),

                "format":(["Portrait","Landscape"],{"default":"Portrait"}),
            },
        }

    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("Width","Height",)

    FUNCTION = "solve"

    #OUTPUT_NODE = False

    CATEGORY = "SimpleTools"

    def solve(self,base, aspect,format):
        res = base * base
        if isinstance(aspect,dict):
            print(aspect["string"])
            s = aspect["string"]
            s = s.split(":")
            print(s)
        else:
            s = aspect.split(":")
        h = int(s[0])
        v = int(s[1])
        a = v/h
        hor = int((pow(res / a,0.5))/8)*8
        ver = int((res/hor)/8)*8

        if format=='Landscape':
            return (hor,ver,)
        
        return(ver,hor,)



# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ResolutionSolver":ResolutionSolver
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionSolver": "Simple Latent Resolution Solver"
}

