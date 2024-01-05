class Parameters:
    """
   A Simple Mustache Parameter Parser.
   When you neet to export the workflow to an API format to use in an external tool, frequently you
   neet to locate and transform the variables to mustache format. Such as {{prompt}} or {{seed}}.
   This tool aims to help those who wants to parse this values directly to a node, that is easier to locate
   and mantain. Export directly your worflows in API format and use the mustache syntax to search and replace the values
   without loosing your original file.
   
    """
   
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "key":("STRING",{"multiline":False,}),
                "parameter": ("STRING",
                        {
                            "multiline":False,
                        }),

                "test":("STRING",{"multiline":False,}),
                "output":(["String","Int","Float"],{"default":"String"}),
            },
        }

    RETURN_TYPES = ("STRING","INT","FLOAT",)
    RETURN_NAMES = ("String","Int","Float")

    FUNCTION = "parameter"

    CATEGORY = "SimpleTools"

    def parameter(self,key,parameter, test,output):
        out = parameter
        if parameter != '': 
            if parameter[0]=="{":
                out = test

        if output == "String":
            strout = out
            intout = None
            floatout = None
        if output == "Int":
            strout = None
            intout = int(out)
            floatout = None
        if output == "Float":
            strout = None
            intout = None
            floatout = float(out)

        print("Parameter Key : "+key)
        print("Test : "+test)
        print("Parameter : "+parameter)
        print("Output : "+ out)
        
        return(strout,intout,floatout,)


NODE_CLASS_MAPPINGS = {
    "Parameters":Parameters
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Parameters": "Simple Mustache Parameter Switcher"
}

